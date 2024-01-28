# OpenPack Dataset Toolkit (optk)

![OpenPack Dataset Logo](./img/OpenPackDataset-black.png)

[![Test](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/test.yaml)
[![API Docs - GitHub Pages](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/open-pack/openpack-toolkit/actions/workflows/deploy-docs.yaml)

["OpenPack Dataset"](https://open-pack.github.io) is a new large-scale multi-modal dataset of the manual packing process.
OpenPack is an open-access logistics dataset for human activity recognition, which contains human movement and package information from 16 distinct subjects.
This repository provides utilities to explore our exciting dataset.

## Install

```bash
# Pip
pip install openpack-toolkit

# Poetry
poetry add  openpack-toolkit
```

Note that the supported dataset version is `>=1.0.0`.

## Docs

- Work Operation Recognition
  - [OpenPack Challenge 2022](./docs/OPENPACK_CHALLENGE/)

Note: Technical documents of the OpenPack dataset are available at [GitHub: openpack-dataset/docs](https://github.com/open-pack/openpack-dataset/tree/main/docs).

## OpenPack Dataset

See [OpenPack Dataset Homepage](https://open-pack.github.io/) or [GitHub: openpack-dataset](https://github.com/open-pack/openpack-dataset) for the details of our dataset.
To download our dataset, visit [this download instruction page](https://github.com/open-pack/openpack-dataset/blob/main/docs/DOWNLOAD.md).

## Examples

### Tutorial

- [Download and Visualization (Notebook)](./samples/OpenPack_DataVisualization.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-pack/openpack-toolkit/blob/main/samples/OpenPack_DataVisualization.ipynb)

### Work Activity Recognition (PyTorch)

PyTorch code samples for the work operation prediction task are available.
See [openpack-torch](https://github.com/open-pack/openpack-torch) for more details.

### Timestamp

Each data point is associated with a millisecond-precision unix timestamp.
The following is a snippet that converts a timestamp (an `int` value) into a `datatime.datetime()` object with timezone.

```python
import datetime


def timestamp_to_datetime(ts: int) -> datetime.datetime:
  """Convert unix timestamp (milli-second precision) into datatime object. """
  timezone_jst = datetime.timezone(datetime.timedelta(hours=9))
  dt = datetime.datetime.fromtimestamp(ts / 1000).replace(tzinfo=timezone_jst)
  return dt

def datetime_to_timestamp(dt: datetime.datetime) -> int:
  """Convert a datetime object into a milli-second precision timestamp."""
  return int(dt.timestamp() * 1000)


ts = 1634885786000

dt_out =  timestamp_to_datetime(ts)
ts_out = datetime_to_timestamp(dt_out)
print(f"datetime: {dt_out}")  # datetime: 2021-10-22 15:56:26+09:00
print(f"timestamp: {ts_out}")  # timestamp: 1634885786000
assert ts_out == ts
```

## Links

- [Homepage](https://open-pack.github.io/) (External Site)
  - [OpenPack Challenge 2022](https://open-pack.github.io/challenge2022) (External Site)
- [zenodo](https://doi.org/10.5281/zenodo.5909086)
- [API Docs](https://open-pack.github.io/openpack-toolkit/openpack_toolkit/)
- [PyPI](https://pypi.org/project/openpack-toolkit/)
- [openpack-dataset](https://github.com/open-pack/openpack-dataset)
- [openpack-torch](https://github.com/open-pack/openpack-torch)

## License

openpack-toolkit has the MIT license, as found in the [LICENSE](./LICENCE) file.

NOTE: [OpenPack Dataset](https://doi.org/10.5281/zenodo.5909086) itself is available under [Creative Commons Attribution Non Commercial Share Alike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license.
However, [OpenPack Dataset (+RGB) License](./docs/OPENPACK_DATASET_RGB_LICENSE.md) is applied to "OpenPack Dataset (+RGB)" which includes RGB data.
