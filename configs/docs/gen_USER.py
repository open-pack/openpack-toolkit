"""Generate ./docs/USER.md
"""
from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_USERS = [
    "debug",
    "pilot-challenge",
]


def main():
    files = sorted(Path("../user").iterdir())

    users = []
    for path in files:
        if path.suffix != ".yaml":
            continue
        logger.info(f"load user config from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        users.append(data)

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("USER.md.jinja")
    code = template.render(users=users)

    # write a python script
    path = Path("../../docs/USER.md")
    logger.info(f"write docs/USER.md to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
