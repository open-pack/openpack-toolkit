import argparse
from logging import INFO, basicConfig, getLogger
from pathlib import Path

from ..download._helpers import download_openpack_from_zenodo

LATEST_VERSION_ON_ZENODO = "v0.2.1"

basicConfig(level=INFO)
logger = getLogger(__name__)


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dataset-dir",
        required=True,
        type=Path,
        help="Path to dataset directory. Downloaded data will be stored under the directory.")
    parser.add_argument(
        "-v",
        "--version",
        default=LATEST_VERSION_ON_ZENODO,
        type=str,
        help=f"Target dataset version. Default: {LATEST_VERSION_ON_ZENODO}")
    parser.add_argument(
        "-s",
        "--streams",
        default="atr-qags,openpack-operations",
        type=str,
        help=(
            "A list of data stream names that you want to download. "
            "Stream names must be separated by commas. "
            "Defaul: atr-qags,openpack-operations"
        ))

    return parser


def entry_func():
    parser = make_parser()
    args = parser.parse_args()

    streams = args.streams.split(",")

    logger.info("Donwload OpenPack dataset from zenodo.")
    logger.info(f" - dataset_dir : {args.dataset_dir}")
    logger.info(f" - version     : {args.version}")
    logger.info(f" - streams     : {streams}")

    download_openpack_from_zenodo(
        args.dataset_dir,
        streams=streams,
        version=args.version)


if __name__ == "__main__":
    entry_func()
