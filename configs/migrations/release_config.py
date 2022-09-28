import json
from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader
from omegaconf import OmegaConf

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_RELEASE_VERSIONS = [
    "v0-2-0",
    "v0-2-1",
    "v0-3-0",
]


def main():
    # load configs
    releases = []
    for release in TARGET_RELEASE_VERSIONS:
        path = Path("../release", f"{release}.yaml")
        logger.info(f"load release config from {path}")
        with open(path, "r") as f:
            data = OmegaConf.to_container(OmegaConf.create(yaml.safe_load(f)))

        data["streams_str"] = json.dumps(data["streams"], indent=4)
        releases.append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("releases.py.jinja")
    code = template.render({"releases": releases})
    code = autopep8.fix_code(code)
    print(code)

    # write a python script
    path = Path("../../openpack_toolkit/configs/releases.py")
    logger.info(f"write configs/releases.py to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
