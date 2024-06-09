import zipfile
from pathlib import Path

import click
import requests
from loguru import logger
from tqdm import tqdm

# TODO: Import metadta from configs.
ZENODO_URLS = {
    "v1.1.0": "https://zenodo.org/records/11059235",
    "v1.0.0": "https://zenodo.org/records/8145223",
}
USERS = (
    "U0101",
    "U0102",
)
# _DEFAULT_OUTPUT_DIR = "../../data/datasets/openpack/"
_DEFAULT_OUTPUT_DIR = "./data/datasets/openpack/"


def download_file_with_progress_bar(src_uri: str, dest_path: Path):
    if dest_path.exists():
        logger.warning(f"Zip file ({dest_path}) already exists. Skip downloading.")
        return

    logger.info(f"Download zip file from {src_uri} and save it to {dest_path}.")
    response = requests.get(src_uri, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as f:
        with tqdm(
            desc=str(dest_path), total=total_size, unit="iB", unit_scale=True, unit_divisor=1024
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
    logger.info(f"Finish downloading zip file to {dest_path}.")


def extract_zip(zip_file_path: Path, extract_path: Path):
    logger.info(f"Extract {zip_file_path} to {extract_path}.")
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    return extract_path


def download_and_extract_single_user_from_zenodo(openpack_dir: Path, version: str, user_id: str):
    logger.info(f"Download and extract data of {user_id} from Zenodo.")
    # Prepare a download URI
    base_uri = ZENODO_URLS[version]
    uri = f"{base_uri}/files/{user_id}.zip?download=1"

    # Prepare a path to save a zip file and extract files
    zip_path = openpack_dir / version / "zip" / "zenodo" / f"{user_id}.zip"
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    user_dir = openpack_dir / version / user_id
    user_dir.mkdir(parents=True, exist_ok=True)

    # Download and extract a zip file
    download_file_with_progress_bar(uri, zip_path)
    extract_zip(zip_path, user_dir)


@click.command()
@click.option(
    "-v",
    "--version",
    type=click.Choice(ZENODO_URLS.keys()),
    default="v1.1.0",
    help="Version of the dataset to download.",
)
@click.option(
    "-o",
    "--openpack-dir",
    type=click.Path(exists=True),
    default=_DEFAULT_OUTPUT_DIR,
    help="a root directory to download datasets.",
)
def main(version: str, openpack_dir: Path):
    print(openpack_dir)

    for user_id in USERS:
        download_and_extract_single_user_from_zenodo(Path(openpack_dir), version, user_id)


if __name__ == "__main__":
    main()
