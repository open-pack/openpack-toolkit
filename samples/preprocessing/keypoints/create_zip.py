import argparse
import zipfile
from logging import getLogger
from pathlib import Path

from tqdm import tqdm

logger = getLogger(__name__)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge 3D keypoints with operation labels")
    parser.add_argument(
        "--dataset-dir", type=Path, required=True, help="Path to the target preprocessed dataset directory."
    )
    parser.add_argument(
        "--file-suffix", type=str, default=".csv", help="suffix of target files."
    )
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="Path to the output directory")
    return parser


def main(args: argparse.Namespace):
    preproc_dataset_rootdir: Path = args.dataset_dir
    preproc_dataset_name: str = args.dataset_dir.name

    logger.info(
        f"Make ziped file of the preprocesed dataset ({preproc_dataset_name}) for Zenodo."
    )

    # Select streams
    files = sorted([p for p in args.dataset_dir.iterdir() if p.name.endswith(args.file_suffix)])
    logger.info(f"{len(files)} files are found.")

    # Creat zip file
    zip_path = Path(args.output_dir, f"{preproc_dataset_name}.zip")
    logger.info(f"Make zip file to {zip_path}")
    if zip_path.exists():
        logger.warning("A zip file already exists. Remove exisiting one.")
        zip_path.unlink()
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    zp = zipfile.ZipFile(zip_path, "w")
    for path in tqdm(files, total=len(files)):
        arcname = Path(preproc_dataset_name, path.relative_to(preproc_dataset_rootdir))
        zp.write(path, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)
    zp.close()


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)

