# OpenPack Dataset Toolkit (optk)

![OpenPack Challenge Logo](./img/OpenPackCHALLENG-black.png)

[![Test](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml)
[![API Docs - GitHub Pages](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml)

"OpenPack Dataset" is a new large-scale multi modal dataset of manual packing process.
OpenPack is an open access logistics-dataset for human activity recognition, which contains human movement and package information from 16 distinct subjects.
This repository provide utilities to explore our exciting dataset.

## Install

We provide some utility functions as python package. You can install via pip with the following command.

```bash
# Pip
pip install openpack-toolkit

# Poetry
poetry add  openpack-toolkit
```

## Links

- [Homepage](https://open-pack.github.io/) (External Site)
- [zenodo](https://doi.org/10.5281/zenodo.5909086)
- [API Docs](https://open-pack.github.io/openpack-toolkit/openpack_toolkit/)
- [PyPI](https://pypi.org/project/openpack-toolkit/)
- [openpack-torch](https://github.com/open-pack/openpack-torch)

## Docs

### Dataset

- [Subjects & Recording Scenarios](./docs/USER.md)
- [Activity Class Definition](./docs/ANNOTATION.md)
- [Modality](./docs/DATA_STREAM.md)
- [Data Split (Train/Val/Test/Submission)](./docs/DATA_SPLIT.md)

### Task

- Work Operation Recognition
  - [OpenPack Challenge](./docs/OPENPACK_CHALLENGE/)

## Examples

### Tutorial

[Getting Started (Notebook)](./samples/OpenPack_GettingStarted.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-toolkit/blob/main/samples/OpenPack_GettingStarted.ipynb)

### Work Activity Recognition (PyTorch)

PyTorch code samples for work operation prediction task is available.
See [openpack-torch](https://github.com/open-pack/openpack-torch) for more dietail.

- [U-Net with Accelration Data](https://github.com/open-pack/openpack-torch/tree/main/examples/unet)
- [ST-GCN with Keypoints Data](https://github.com/open-pack/openpack-torch/tree/main/examples/st-gcn)

## Download Dataset

```bash
optk-download -d ../data/datasets -v v0.2.0 -s atr-qags,openpack-operations

# If you are a user of poetry,
poetry run optk-download -d ../data/datasets -v v0.2.0 -s atr-qags,openpack-operations
```

Help:

```bash
$ poetry run optk-download -d ../data/datasets -h
usage: optk-download [-h] -d DATASET_DIR [-v VERSION] [-s STREAMS]

optional arguments:
  -h, --help            show this help message and exit
  -d DATASET_DIR, --dataset-dir DATASET_DIR
                        Path to dataset directory. Downloaded data will be stored under the directory
  -v VERSION, --version VERSION
                        Target dataset version. Default: v0.2.0
  -s STREAMS, --streams STREAMS
                        A list of data stream names that you want to download. Stream names must be separated by commas. Defaul: atr-qags,openpack-operations
```

### Dataset Structure

[v0.2.0](https://zenodo.org/record/6697990)

```txt
../data/datasets/
└── openpack
    └── v0.2.0
        ├── U0102
        │   ├── annotation
        │   │   └── openpack-operations
        │   │       ├── S0100.csv
        │   │       ├── S0200.csv
        │   │       ├── S0300.csv
        │   │       ├── S0400.csv
        │   │       └── S0500.csv
        │   ├── atr
        │   │   ├── atr01
        │   │   │   ├── S0100.csv
        │   │   │   ├── S0200.csv
        │   │   │   ├── S0300.csv
        │   │   │   ├── S0400.csv
        │   │   │   └── S0500.csv
        │   │   ├── atr02
        │   │   │   ├── S0100.csv
        │   │   │   ├── S0200.csv
        │   │   │   ├── S0300.csv
        │   │   │   ├── S0400.csv
        │   │   │   └── S0500.csv
        │   │   ├── atr03
        │   │   │   ├── S0100.csv
        │   │   │   ├── S0200.csv
        │   │   │   ├── S0300.csv
        │   │   │   ├── S0400.csv
        │   │   │   └── S0500.csv
        │   │   └── atr04
        │   │       ├── S0100.csv
        │   │       ├── S0200.csv
        │   │       ├── S0300.csv
        │   │       ├── S0400.csv
        │   │       └── S0500.csv
        │   └── kinect
        │       └── 2d-kpt
        │           └── mmpose-hrnet-w48-posetrack18-384x288-posewarper-stage2
        │               ├── U0102
        │               │   └── single
        │               │       ├── S0100.json
        │               │       ├── S0200.json
        │               │       ├── S0300.json
        │               │       ├── S0400.json
        │               │       └── S0500.json
        │               └── single
        │                   ├── S0100.json
        │                   ├── S0200.json
        │                   ├── S0300.json
        │                   ├── S0400.json
        │                   └── S0500.json

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        └── zenodo
            ├── U0102__annotation.zip
            ├── U0102__atr.zip
            ├── U0102__kinect__2d-kpt.zip
            ├── U0103__annotation.zip
            ├── U0103__atr.zip
            ├── U0103__kinect__2d-kpt.zip
            ├── U0105__annotation.zip
            ├── U0105__atr.zip
            ├── U0105__kinect__2d-kpt.zip
            ├── U0106__annotation.zip
            ├── U0106__atr.zip
            └── U0106__kinect__2d-kpt.zip
```

## License

openpack-toolkit has a MIT license, as found in the [LICENSE](./LICENCE) file.

NOTE: [OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
