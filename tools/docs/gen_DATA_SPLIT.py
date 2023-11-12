"""Generate ./docs/DATA_SPLIT.md
"""
from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from omegaconf import OmegaConf

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_DATA_SPLIT = [
    "debug",
    "pilot-challenge",
    "openpack-challenge-2022",
]


def main():

    splits = []
    for split_name in TARGET_DATA_SPLIT:
        path = Path(f"../../configs/dataset/split/{split_name}.yaml")
        logger.info(f"load DataSplitConfig from {path}")
        with open(path, "r") as f:
            data = OmegaConf.create(yaml.safe_load(f))
        splits.append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("DATA_SPLIT.md.jinja")
    code = template.render(splits=splits)

    # write a python script
    path = Path("../../docs/DATA_SPLIT.md")
    logger.info(f"write docs/DATA_SPLIT.md to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
