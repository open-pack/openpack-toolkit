from pathlib import Path

from openpack_toolkit.download._helpers import download_openpack_from_zenodo


def test_download_openpack_from_zenodo__01(tmpdir):
    rootdir = Path(tmpdir, "data", "datasets")
    rootdir.mkdir(exist_ok=True, parents=True)

    path = Path(rootdir)
    print("path:", path, list(path.iterdir()))

    streams = [
        # "atr-qags",
        # "e4-all",
        # "kinect-2d-kpt",
        "activity-1s",
    ]
    version = "v0.3.0"

    download_openpack_from_zenodo(rootdir, streams=streams, version=version)

    path = Path(rootdir, "openpack", version, "U0102")
    for f in path.iterdir():
        print("-", f)
