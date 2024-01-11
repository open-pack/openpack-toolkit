import datetime
from enum import Enum
from logging import getLogger
from pathlib import Path

import pandas as pd

from openpack_toolkit import DATASET_VERSION

logger = getLogger(__name__)

PATH_KEY_NAME = "path"
ST_MTIME_KEY_NAME = "st_mtime"  # last modification time
ST_CTIME_KEY_NAME = "st_ctime"  # Time of most recent metadata change expressed in seconds.
ST_SIZE_KEY_NAME = "size_bytes"
ST_SIZE_HUMAN_READABLE_KEY_NAME = "size"
IS_DIR_KEY_NAME = "is_dir"
FILE_EXISTS_KEY_NAME = "file_exists"

LATEST_VERSION_ON_ZENODO = DATASET_VERSION


class DatasetRepo(Enum):
    ZENODO = "zenodo"
    GOOGLE_DRIVE = "GoogleDrive"
    GOOGLE_DRIVE_RGB = "GoogleDriveRGB"

    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]


class DatasetVersion(Enum):
    VERSION_0_3_0 = "v0.3.0"
    VERSION_1_0_0 = "v1.0.0"

    @classmethod
    def get_names(cls) -> list:
        return [i.name for i in cls]

    @classmethod
    def get_values(cls) -> list:
        return [i.value for i in cls]


class DatasetStatus(Enum):
    OK = 0
    DATASET_DIR_DOES_NOT_EXISTS = 1
    HAS_MISSING_FILE = 2


# TODO: How should I manage file indexes?
OPENPACK_DATASET_INDEX_LIST: dict[tuple[str, str], str] = {
    (
        DatasetVersion.VERSION_1_0_0.value,
        DatasetRepo.ZENODO.value,
    ): "https://raw.githubusercontent.com/open-pack/openpack-dataset/main/release/v1.0.0/file_index_OpenPack_v1.0.0_zenodo.csv",
}


def path_bfs(path: Path, results: list) -> list:
    """List dirs and files with DFS. Stop search when S0XXX files are detected.
    Args:
        path (str): -
        targets (list): list of the target directory.
    Returns:
        list: list of Path objects.
    """
    logger.debug(f">> DFS Current Location: {path}")

    # Base Case
    if path.is_file() or (path.stem in ("S0100", "S0200", "S0300", "S0400", "S0500")):
        results.append(path)
        return results

    for path_child in path.iterdir():
        results = path_bfs(path_child, results)
    return results


def convert_file_size(size, unit="KB"):
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
    i = units.index(unit.upper())
    size_ = size / 1024**i

    if size_ > 1000.0:
        return convert_file_size(size, unit=units[i + 1])
    return f"{size_:.2f} {units[i]}"


def make_dataset_file_index(
    openpack_rootdir: Path,
    dataset_version: str,
    return_full_metrics: bool = False,
) -> pd.DataFrame:
    rootdir = Path(openpack_rootdir, dataset_version)
    if not rootdir.exists():
        raise FileNotFoundError(f"Dataset directory does not exists: {rootdir}")

    # List up files.
    logger.info(f"Making file index. rootdir={rootdir}")
    results = path_bfs(rootdir, [])
    logger.info(f"{len(results)} files/dirs are found.")

    # Get stats
    df = []
    for p in results:
        record = {
            PATH_KEY_NAME: str(p.relative_to(rootdir)),
            ST_SIZE_HUMAN_READABLE_KEY_NAME: convert_file_size(p.stat().st_size),
            IS_DIR_KEY_NAME: p.is_dir(),
        }
        if return_full_metrics:
            mtime = datetime.datetime.fromtimestamp(p.stat().st_mtime)
            ctime = datetime.datetime.fromtimestamp(p.stat().st_ctime)

            record.update(
                {
                    ST_SIZE_KEY_NAME: p.stat().st_size,
                    ST_MTIME_KEY_NAME: mtime,
                    ST_CTIME_KEY_NAME: ctime,
                }
            )
        df.append(record)
    df = pd.DataFrame(df).sort_values([PATH_KEY_NAME]).reset_index(drop=True)

    if return_full_metrics:
        cols = [
            PATH_KEY_NAME,
            ST_SIZE_KEY_NAME,
            ST_SIZE_HUMAN_READABLE_KEY_NAME,
            ST_MTIME_KEY_NAME,
            ST_CTIME_KEY_NAME,
            IS_DIR_KEY_NAME,
        ]
        df = df[cols]
    return df


def get_dataset_file_index_uri(
    version: str = LATEST_VERSION_ON_ZENODO,
    data_repo: str = DatasetRepo.ZENODO.value,
):
    if version not in DatasetVersion.get_values():
        raise ValueError(f"Invalid dataset version: {version}")
    if data_repo not in DatasetRepo.get_values():
        raise ValueError(f"Invalid data repository name: {data_repo}")

    key = (version, data_repo)
    uri = OPENPACK_DATASET_INDEX_LIST.get(key)
    if uri is None:
        raise NotImplementedError(f"{version}@{data_repo} is not supported yet.")

    return uri


def check_files_exists(
    openpack_rootdir: Path,
    openpack_version: str,
    file_index_uri: str,
) -> tuple[DatasetStatus, pd.DataFrame]:
    df_file_index = pd.read_csv(file_index_uri)
    logger.info(f"Loading of file index was success. {len(df_file_index)} files should be there.")

    rootdir = Path(openpack_rootdir, openpack_version)
    if not rootdir.exists():
        raise FileNotFoundError(f"Dataset directory does not exists: {rootdir}")

    # Check file one by one
    logger.info(f"Check files under {Path(openpack_rootdir, openpack_version)} ...")
    df_file_index[FILE_EXISTS_KEY_NAME] = None
    for idx, row in df_file_index.iterrows():
        path = Path(openpack_rootdir, openpack_version, row[PATH_KEY_NAME])
        df_file_index.loc[idx, FILE_EXISTS_KEY_NAME] = True if path.exists() else False

    missing_files = df_file_index[df_file_index[FILE_EXISTS_KEY_NAME] == False]
    if len(missing_files) == 0:
        status_code = DatasetStatus.OK
    else:
        status_code = DatasetStatus.HAS_MISSING_FILE

    return status_code, df_file_index
