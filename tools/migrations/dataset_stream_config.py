from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_STREAM = [
    # -- IMU --
    "atr-acc",
    "atr-qags",
    "e4-acc",
    "e4-bvp",
    "e4-eda",
    "e4-temp",
    # -- Keypoint --
    "kinect-2d-kpt",
    "kinect-3d-kpt",
    "kinect-depth2",
    # -- RS02 --
    "rs02-depth",
    # -- System --
    "system-ht-original",
    "system-order-sheet",
    "system-printer",
]


def main():
    # load configs
    params = dict(streams=[])
    for stream in TARGET_STREAM:
        path = Path("../../configs/dataset/stream", f"{stream}.yaml")
        logger.info(f"load dataset/stream config from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        params["streams"].append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("dataset.stream.py.jinja")
    code = template.render(**params)
    code = autopep8.fix_code(
        code,
        options={"max_line_length": 100}
    )

    # write a python script
    path = Path("../../openpack_toolkit/configs/datasets/streams.py")
    logger.info(f"write configs/dataset/streams.py to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
