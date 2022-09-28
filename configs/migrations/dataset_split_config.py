from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader
from omegaconf import OmegaConf

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_SPLITS = [
    "debug",
    "pilot-challenge",
    "openpack-challenge-2022",
]


def main():
    # load configs
    params = dict(splits=dict())
    for split in TARGET_SPLITS:
        path = Path("../dataset/split", f"{split}.yaml")
        logger.info(f"load dataset/split config from {path}")
        with open(path, "r") as f:
            data = OmegaConf.create(yaml.safe_load(f))
        params["splits"][split] = data

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("dataset.split.py.jinja")
    code = template.render(**params)
    code = autopep8.fix_code(
        code,
        options={"max_line_length": 100}
    )
    print(code)

    # write a python script
    path = Path("../../openpack_toolkit/configs/datasets/splits.py")
    logger.info(f"write configs/dataset/splits.py to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
