import datetime
from logging import getLogger
from pathlib import Path


import pandas as pd

logger = getLogger(__name__)

PATH_KEY_NAME = "path"
ST_MTIME_KEY_NAME = "st_mtime"  # last modification time
ST_CTIME_KEY_NAME = "st_ctime"  # Time of most recent metadata change expressed in seconds.
ST_SIZE_KEY_NAME = "size_bytes"
ST_SIZE_HUMAN_READABLE_KEY_NAME = "size"
IS_DIR_KEY_NAME = "is_dir"


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
):
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
