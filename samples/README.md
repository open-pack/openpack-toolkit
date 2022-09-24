# Samples

## Notebooks

### Download and Visualization

- [`OpenPack_DataVisualization.ipynb`](./samples/OpenPack_DataVisualization.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-toolkit/blob/main/samples/OpenPack_DataVisualization.ipynb)

This notebook shows how to donwload and setup the OpenPack dataset and visualize some of them.
You can run this noetbook in colab from the link above.

## Sample Data  (`openpack/`)

There is a sample data in `openpack/`. The sample include data from S0500 of U0102.
You can see the file structures and the file format with these  data.

NOTE: This is a sample data. When you do research, please download the latest version from zenodo.

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
