from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_USERS = [
    "U0101",
    "U0102",
    "U0103",
    "U0104",
    "U0105",
    "U0106",
    "U0107",
    "U0108",
    "U0109",
    "U0110",
    "U0111",
    "U0201",
    "U0202",
    "U0203",
    "U0204",
    "U0205",
    "U0206",
    "U0207",
    "U0208",
    "U0209",
    "U0210",
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
