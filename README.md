# OpenPack Dataset Toolkit (optk)

![OpenPack Challenge Logo](./img/OpenPackCHALLENG-black.png)

[![Test](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml)
[![API Docs - GitHub Pages](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml)

"OpenPack Dataset" is a new large-scale multi modal dataset of manual packing process.
OpenPack is an open access logistics-dataset for human activity recognition, which contains human movement and package information from 17 distinct subjects.
This repository provide utilities to explore our exciting dataset.

## Setup

We provide some utility functions as python package. You can install via pip with the following command.

```bash
# Pip
pip install openpack-toolkit

# Poetry
poetry add  openpack-toolkit
```

## Documentation

- [Dataset Page](https://open-pack.github.io/)
- [API Docs](https://open-pack.github.io/openpack-toolkit/openpack_toolkit/)

### Dataset Descriptions

- [Subjects & Recording Scenarios](./docs/USER.md)
- [Activity Class Definition](./docs/ANNOTATION.md)
- [Modality](./docs/DATA_STREAM.md)
- [Data Split (Train/Val/Test/Submission)](./docs/DATA_SPLIT.md)

## Examples (PyTorch)

See [openpack-torch](https://github.com/open-pack/openpack-torch) for more dietail.

- [U-Net with Accelration Data](https://github.com/open-pack/openpack-torch/tree/main/examples/unet)
- [ST-GCN with Keypoints Data](https://github.com/open-pack/openpack-torch/tree/main/examples/st-gcn)

## License

openpack-toolkit has a MIT license, as found in the [LICENSE](./LICENCE) file.

----

## Generate Document

```bash
pdoc --html --output-dir docs --force openpack_toolkit/
```
