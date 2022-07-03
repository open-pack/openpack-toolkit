from pathlib import Path

from openpack_toolkit.download._helpers import download_openpack_from_zenodo


def test_download_openpack_from_zenodo__01(tmpdir):
    rootdir = Path(tmpdir, "data", "datasets")
    rootdir.mkdir(exist_ok=True, parents=True)

    streams = [
        # "atr-qags",
        # "kinect-2d-kpt",
        "openpack-operations",
    ]
    version = "v0.2.0"

    download_openpack_from_zenodo(rootdir, streams=streams, version=version)
