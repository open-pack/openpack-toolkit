import socket
import zipfile
from pathlib import Path

import click
import requests
import wandb
from loguru import logger
from tqdm import tqdm

from tools.download.const import (
    OPENPACK_DATASET_NAME_ON_LOCAL_TEMPLATE,
    OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE,
    OPENPACK_USERS,
    WANDB_ARTIFACT_TYPE_DATASET,
    WANDB_JOB_TYPE_DOWNLOAD_DATASET,
    WANDB_PROJECT_NAME_LOCAL,
    WANDB_PROJECT_NAME_PUBLIC,
    ZENODO_URLS,
)

# _DEFAULT_OUTPUT_DIR = "../../data/datasets/openpack/"
_DEFAULT_OPENPACK_DIR = Path().cwd() / "data" / "datasets" / "openpack"


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
    extract_path.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)


def download_from_zenodo(
    version: str, user_id: str, zip_dir: Path, remote_artifact: wandb.Artifact = None
):
    """Download a zip file from Zenodo. If the wandb is active, download using the artifact."""
    if remote_artifact is not None:
        zip_path = remote_artifact.get_entry(f"{user_id}.zip").download(
            root=zip_dir, skip_cache=True
        )
    else:
        base_uri = ZENODO_URLS[version]
        uri = f"{base_uri}/files/{user_id}.zip?download=1"
        zip_path = zip_dir / f"{user_id}.zip"
        download_file_with_progress_bar(uri, zip_path)
    return zip_path


def extract_zip_from_zenodo(zip_path: Path, user_dir: Path, local_artifact: wandb.Artifact = None):
    """Extract a zip file downloaded from zenodo to the user_directory."""
    user_id = user_dir.name
    logger.info(f"Extract zip file for {user_id}.")
    extract_zip(zip_path, user_dir)

    # Log local data to WandB.
    # Create artifact references for each data stream.
    if local_artifact is not None:
        logger.info(f"Log streams of {user_id} to WandB.")
        for sensor_dir in user_dir.iterdir():
            for stream_dir in sensor_dir.iterdir():
                local_artifact.add_reference(
                    f"file://{stream_dir.absolute()}",
                    name=f"{user_id}/{sensor_dir.name}/{stream_dir.name}",
                )


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
    default=_DEFAULT_OPENPACK_DIR,
    help="a root directory to download datasets.",
)
@click.option(
    "--use-wandb",
    "--wandb",
    is_flag=True,
    show_default=True,
    default=True,
    help="Log artifact with wandb.",
)
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Run in debug mode.")
def main(version: str, openpack_dir: Path, use_wandb: bool = True, debug: bool = False):
    # Init wandb.
    if use_wandb is not None:
        project_name = WANDB_PROJECT_NAME_LOCAL
        if debug:
            project_name += "-debug"
        wandb_run = wandb.init(project=project_name, job_type=WANDB_JOB_TYPE_DOWNLOAD_DATASET)
        remote_artifact = wandb_run.use_artifact(
            f"{WANDB_PROJECT_NAME_PUBLIC}/{OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE}:latest".format(
                version=version
            )
        )
        local_artifact = wandb.Artifact(
            name=OPENPACK_DATASET_NAME_ON_LOCAL_TEMPLATE.format(
                version=version, hostname=socket.gethostname()
            ),
            type=WANDB_ARTIFACT_TYPE_DATASET,
            description=f"OpenPack Dataset ({version}) on {socket.gethostname()}",
        )
    else:
        wandb_run, remote_artifact, local_artifact = None, None, None

    # Init dataset directories.
    openpack_dir = Path(openpack_dir)
    zip_dir = openpack_dir / version / "zip" / "zenodo"
    zip_dir.mkdir(parents=True, exist_ok=True)
    users = OPENPACK_USERS
    if debug:
        users = users[:2]

    # Download and extract data for the first two users.
    for user_id in users:
        zip_path = download_from_zenodo(version, user_id, openpack_dir, remote_artifact)

        user_dir = openpack_dir / user_id
        extract_zip_from_zenodo(zip_path, user_dir, local_artifact=local_artifact)

    # Save the artifact to W&B
    wandb_run.log_artifact(local_artifact)
    wandb_run.finish()


if __name__ == "__main__":
    main()
