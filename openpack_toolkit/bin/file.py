import argparse
from logging import INFO, basicConfig, getLogger
from pathlib import Path

from openpack_toolkit import DATASET_VERSION
from openpack_toolkit.validation.file import make_dataset_file_index

LATEST_VERSION_ON_ZENODO = DATASET_VERSION
DEFAULT_OUTPUT_DIR = Path(".")

DATA_REPO_ZENODO = "zenodo"
DATA_REPO_GOOGLE_DRIVE = "GoogleDrive"
DATA_REPO_GOOGLE_DRIVE_RGB = "GoogleDriveRGB"


basicConfig(level=INFO)
logger = getLogger(__name__)


def make_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    # == Make File Index ==
    parser_make_index = subparsers.add_parser(
        "make-index", help="Make file index of the OpenPack dataset. See `make-index -h`"
    )
    parser_make_index.set_defaults(handler=entry_func_make_index)
    parser_make_index.add_argument(
        "-r",
        "--rootdir",
        required=True,
        type=Path,
        help="OpenPack dataset directory.",
    )
    parser_make_index.add_argument(
        "-v",
        "--version",
        default=LATEST_VERSION_ON_ZENODO,
        type=str,
        help=f"dataset version. (Default: {LATEST_VERSION_ON_ZENODO})",
    )
    parser_make_index.add_argument(
        "--data-repo",
        default=DATA_REPO_ZENODO,
        type=str,
        help=(
            f"dataset version. (Default: {DATA_REPO_ZENODO}, "
            f"Option: {DATA_REPO_ZENODO}, {DATA_REPO_GOOGLE_DRIVE}, {DATA_REPO_GOOGLE_DRIVE_RGB})"
        ),
    )
    parser_make_index.add_argument(
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


def entry_func():
    parser = make_parser()
    args = parser.parse_args()

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    entry_func()
