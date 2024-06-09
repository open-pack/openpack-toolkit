"""Create wandb artifact of the original OenPack dataset.
"""

import click
import wandb

from tools.download.const import (
    OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE,
    OPENPACK_USERS,
    WANDB_ARTIFACT_TYPE_DATASET,
    WANDB_JOB_TYPE_DOWNLOAD_DATASET,
    WANDB_PROJECT_NAME,
    ZENODO_URLS,
)


@click.group()
def cli():
    pass


def create_wandb_artifacts_zenodo(version: str):
    wandb_run = wandb.init(project=WANDB_PROJECT_NAME, job_type=WANDB_JOB_TYPE_DOWNLOAD_DATASET)
    artifact = wandb.Artifact(
        name=OPENPACK_DATASET_NAME_ON_ZENODO_TEMPLATE.format(version=version),
        type=WANDB_ARTIFACT_TYPE_DATASET,
    )

    # Add files to the artifact
    base_uri = ZENODO_URLS[version]
    for user_id in OPENPACK_USERS:
        uri = f"{base_uri}/files/{user_id}.zip?download=1"
        artifact.add_reference(uri, name=f"{user_id}.zip")

    # Save the artifact to W&B
    wandb_run.log_artifact(artifact)
    wandb_run.finish()


@cli.command()
@click.option(
    "-v",
    "--version",
    type=click.Choice(ZENODO_URLS.keys()),
    default="v1.1.0",
    help="Version of the dataset to download.",
)
def zenodo(version: str):
    click.echo(f"Create a WandB artifact for zenodo ({version}).")
    create_wandb_artifacts_zenodo(version)


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
