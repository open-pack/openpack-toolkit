from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_USERS = [
    "U0102",
    "U0103",
    "U0105",
    "U0106",
    "U0107",
]


def main():
    # load configs
    params = dict(users=[])
    for user in TARGET_USERS:
        path = Path("../user", f"{user}.yaml")
        logger.info(f"load user config from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        params["users"].append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("user.py.jinja")
    code = template.render(**params)
    code = autopep8.fix_code(code)

    # write a python script
    path = Path("../../openpack_toolkit/configs/users.py")
    logger.info(f"write configs/user.py to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
