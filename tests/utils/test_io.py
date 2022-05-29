from pathlib import Path

from openpack_toolkit.utils.io import cleanup_dir


def test_cleanup_dir__01(tmpdir):
    subdir = Path(tmpdir, "sub1")
    subdir.mkdir()
    Path(subdir, "sub2").mkdir()
    Path(subdir, "sub3").mkdir()
    with open(Path(subdir, "hydra-main.log"), "w") as f:
        f.write("test")

    cleanup_dir(subdir, exclude="hydra")
    assert len(list(subdir.iterdir())) == 1
