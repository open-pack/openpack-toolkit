import argparse
from logging import INFO, basicConfig, getLogger
from pathlib import Path

from openpack_toolkit import DATASET_VERSION
from openpack_toolkit.validation.file import (
    FILE_EXISTS_KEY_NAME,
    DatasetRepo,
    DatasetStatus,
    check_files_exists,
    get_dataset_file_index_uri,
    make_dataset_file_index,
)

basicConfig(level=INFO)
logger = getLogger(__name__)

LATEST_VERSION_ON_ZENODO = DATASET_VERSION
DEFAULT_OUTPUT_DIR = Path(".")


def make_parser():
    def _add_common_params(parser: argparse.ArgumentParser):
        parser.add_argument(
            "-r",
            "--rootdir",
            required=True,
            type=Path,
            help="OpenPack dataset directory.",
        )
        parser.add_argument(
            "-v",
            "--version",
            default=LATEST_VERSION_ON_ZENODO,
            type=str,
            help=f"dataset version. (Default: {LATEST_VERSION_ON_ZENODO})",
        )
        parser.add_argument(
            "--data-repo",
            default=DatasetRepo.ZENODO.value,
            type=str,
            help=(
                f"dataset version. (Default: {DatasetRepo.ZENODO.value}, "
                f"Option: {DatasetRepo.ZENODO.value}, {DatasetRepo.GOOGLE_DRIVE.value}, "
                f"{DatasetRepo.GOOGLE_DRIVE_RGB.value})"
            ),
        )
        return parser

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    # == Make File Index ==
    parser_make_index = subparsers.add_parser(
        "make-index", help="Make file index of the OpenPack dataset. See `make-index -h`"
    )
    parser_make_index.set_defaults(handler=entry_func_make_index)
    parser_make_index = _add_common_params(parser_make_index)
    parser_make_index.add_argument(
        "--output-dir",
        required=False,
        default=DEFAULT_OUTPUT_DIR,
        type=Path,
        help=f"output directory. (Default: {DEFAULT_OUTPUT_DIR})",
    )

    # == Check Files ==
    parser_check = subparsers.add_parser("check", help="Check downloaded files. See `check -h`")
    parser_check.set_defaults(handler=entry_func_check)
    parser_check = _add_common_params(parser_check)
    parser_check.add_argument(
        "--output-dir",
        required=False,
        default=DEFAULT_OUTPUT_DIR,
        type=Path,
        help=f"output directory. (Default: {DEFAULT_OUTPUT_DIR})",
    )
    return parser


def entry_func_make_index(args: argparse.Namespace):
    df = make_dataset_file_index(args.rootdir, args.version)
    logger.info(f"File Index:\n{df}")

    path = Path(args.output_dir, f"file_index_OpenPack_{args.version}_{args.data_repo}.csv")
    logger.info(f"Save file index to {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def entry_func_check(args: argparse.Namespace):
    file_index_uri = get_dataset_file_index_uri(args.version, args.data_repo)
    logger.info(f"Get file index from {file_index_uri}")

    status_code, df_file_index = check_files_exists(args.rootdir, args.version, file_index_uri)

    path = Path(
        args.output_dir, f"file_index_OpenPack_{args.version}_{args.data_repo}_check_result.csv"
    )
    logger.info(f"Save check results to {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    df_file_index.to_csv(path, index=False)

    if status_code == DatasetStatus.HAS_MISSING_FILE:
        df_missing_files = df_file_index[df_file_index[FILE_EXISTS_KEY_NAME] == False]
        logger.warning(
            f"{len(df_missing_files)} files ({len(df_missing_files)/len(df_file_index)*100:.1f}%)"
            f" are missing.\n{df_missing_files}"
        )
    else:
        logger.info("No missing files! It's ready to use!")


def entry_func():
    parser = make_parser()
    args = parser.parse_args()

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    entry_func()
