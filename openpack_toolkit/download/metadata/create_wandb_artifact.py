"""Create wandb artifact of the original OenPack dataset.
"""

from __future__ import annotations

from pathlib import Path

import attrs
import cattrs
import click
import wandb
from loguru import logger
from omegaconf import OmegaConf

from openpack_toolkit.download.const import (
    OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE,
    OPENPACK_USERS,
    WANDB_ARTIFACT_TYPE_DATASET,
    WANDB_JOB_TYPE_DOWNLOAD_DATASET,
    WANDB_PROJECT_NAME_PUBLIC,
    ZENODO_URLS,
)

OPENPACK_CACHE_DIR = Path(".cache/")
OPERNPACK_ZIP_DIR_ZENODO = OPENPACK_CACHE_DIR / "zenodo"

_DEFAULT_OUTPUT_DIR = Path("./outputs")
_DEFAULT_OUTPUT_PATH_ZENODO = _DEFAULT_OUTPUT_DIR / "dataset_metadata_zenodo.yaml"

# =============
#  Data Models
# =============


@attrs.define
class WebsiteList:
    project: str = "https://open-pack.github.io/"
    github: str = "https://github.com/open-pack/openpack-dataset"
    release_note: str = "https://github.com/open-pack/openpack-dataset/tree/main/release/{version}"


@attrs.define
class DatasetObjectMetadata:
    file_name: str
    file_type: str
    parent_dir: Path
    source: str | None = None  # URI of the object that contains this object.
    subject: str | None = None
    session: str | None = None


@attrs.define
class DatasetMetadata:
    name: str
    version: str
    repository: str
    repository_url: str
    website: WebsiteList = WebsiteList()
    objects: list[DatasetObjectMetadata] = attrs.field(factory=list)

    def __attrs_post_init__(self):
        self.website.release_note = self.website.release_note.format(version=self.version)


def get_converter() -> cattrs.Converter:
    converter = cattrs.Converter()
    converter.register_structure_hook(Path, Path)
    converter.register_unstructure_hook(Path, str)
    return converter


# ====================
#  Metadata Generator
# ====================


def create_metadata_zenodo(version: str) -> DatasetMetadata:
    metadata = DatasetMetadata(
        name=OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE.format(version=version),
        version=version,
        repository="zenodo",
        repository_url=ZENODO_URLS[version],
    )

    # Add files to the metadata
    base_uri = ZENODO_URLS[version]
    for user_id in OPENPACK_USERS:
        uri = f"{base_uri}/files/{user_id}.zip?download=1"
        obj_metadata = DatasetObjectMetadata(
            file_name=f"{user_id}.zip",
            file_type="zip",
            parent_dir=OPERNPACK_ZIP_DIR_ZENODO,
            source=uri,
        )
        metadata.objects.append(obj_metadata)

    return metadata


def create_wandb_artifacts_zenodo(version: str):
    wandb_run = wandb.init(
        project=WANDB_PROJECT_NAME_PUBLIC, job_type=WANDB_JOB_TYPE_DOWNLOAD_DATASET
    )
    artifact = wandb.Artifact(
        name=OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE.format(version=version),
        type=WANDB_ARTIFACT_TYPE_DATASET,
        description=(
            f"OpenPack Dataset ({version}) on zenodo. "
            "Visit https://open-pack.github.io/ for more details."
        ),
        metadata={
            "website": "https://open-pack.github.io/",
            "GitHub": "https://github.com/open-pack/openpack-dataset",
            "version": version,
            "release_note": f"https://github.com/open-pack/openpack-dataset/tree/main/release/{version}",
            "repository": "zenodo",
            "repository_url": ZENODO_URLS[version],
        },
    )

    # Add files to the artifact
    base_uri = ZENODO_URLS[version]
    for user_id in OPENPACK_USERS:
        uri = f"{base_uri}/files/{user_id}.zip?download=1"
        artifact.add_reference(uri, name=f"{user_id}.zip")

    # Save the artifact to W&B
    wandb_run.log_artifact(artifact)
    wandb_run.finish()


# ==========
#  Commands
# ==========


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-v",
    "--version",
    type=click.Choice(ZENODO_URLS.keys()),
    default="v1.1.0",
    help="Version of the dataset to download.",
)
@click.option(
    "-o",
    "--output-path",
    type=click.Path(file_okay=True, path_type=Path),
    default=_DEFAULT_OUTPUT_PATH_ZENODO,
    show_default=True,
    help="output file path.",
)
def zenodo(version: str, output_path: Path):
    click.echo(f"Create a WandB artifact for zenodo ({version}).")
    # create_wandb_artifacts_zenodo(version)
    metadata = create_metadata_zenodo(version)

    converter = get_converter()
    metadata_dict = converter.unstructure(metadata)
    print(OmegaConf.to_yaml(metadata_dict))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as f:
        OmegaConf.save(metadata_dict, f)
    logger.info(f"Saved metadata to {output_path}")


@cli.command()
@click.option(
    "-v",
    "--version",
    type=click.Choice(ZENODO_URLS.keys()),
    default="v1.1.0",
    help="Version of the dataset to download.",
)
def gdrive(version: str):
    click.echo(f"Create a WandB artifact for Google Drive ({version}).")


def main():
    cli()


if __name__ == "__main__":
    main()
