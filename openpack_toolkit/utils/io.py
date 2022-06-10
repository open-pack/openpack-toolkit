import shutil
from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)


def cleanup_dir(path: Path, exclude: str = None) -> None:
    """Remove files and directories in the selected.

    Keep files generated by hydra.

    Args:
        path (Path): path to the target directory.
        exclude (str): keep files and directories whose name contains the given string.
    """
    if not path.is_dir():
        raise ValueError(f"path is expected to be a directory, but got {path}")
    logger.debug(f"clean up {path}")

    for p in path.iterdir():
        if "hydra" in p.name:
            continue
        elif p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink(missing_ok=False)
    return
