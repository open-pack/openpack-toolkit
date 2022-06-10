from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import autopep8
import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_ANNOTATIONS = [
    "openpack-operations",
    "openpack-actions",
]


def main():
    # load configs
    params = dict(annotations=dict())
    for annot in TARGET_ANNOTATIONS:
        path = Path("../dataset/annotation", f"{annot}.yaml")
        logger.info(f"load dataset/annotation config from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        params["annotations"][annot] = data

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("dataset.annotations.py.jinja")
    code = template.render(**params)
    code = autopep8.fix_code(
        code,
        options={"max_line_length": 100}
    )
    print(code)

    # write a python script
    path = Path("../../openpack_toolkit/configs/datasets/annotations.py")
    logger.info(f"write configs/dataset/annotations.py to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
