from pathlib import Path

from openpack_toolkit.download._helpers import download_openpack_from_zenodo


def test_download_openpack_from_zenodo__01():
    rootdir = Path("../data/datasets")
    streams = [
        "atr-qags",
        "openpack-operations",
    ]
    version = "v0.2.0"

    download_openpack_from_zenodo(rootdir, streams=streams, version=version)
