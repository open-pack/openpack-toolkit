# Python-based Data Downloader

Shell script-based data downloader is prepared in [open-pack/openpack-dataset](https://github.com/open-pack/openpack-dataset/blob/main/docs/DOWNLOAD.md).
However, it does not support downloading data from Google Drive and it is not easy to configure.
This download tool provides another option to set up datasets in your environment.

## How to use

```bash
poetry run python download.py
```

### Tracke data lineage with Weight and Biases

(Optional) Create an artifact of the OpenPack Dataset on the cloud repository.

```bash
poetry run python create_wandb_artifact.py zenodo
```

Download the dataset into your local using WandB.

```bash
wandb login
poetry run python download_local.py --use-wandb
```
