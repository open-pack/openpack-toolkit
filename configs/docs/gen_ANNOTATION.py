"""Generate ./docs/ANNOTATION.md
"""
from logging import DEBUG, basicConfig, getLogger
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

basicConfig(level=DEBUG)
logger = getLogger(__name__)

TARGET_ANNOTATIONS = [
    "openpack-operations",
    "openpack-actions",
    "activity-1s",
]


def main():

    annotations = dict()
    for annot_name in TARGET_ANNOTATIONS:
        path = Path(f"../dataset/annotation/{annot_name}.yaml")
        logger.info(f"load DataStreamConfig from {path}")
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        data["act_set_name"] = data["name"].replace("-", "_").upper()
        annotations[annot_name] = data

    # build python script with jinja2
    env = Environment(
        loader=FileSystemLoader("./templates"),
        trim_blocks=True
    )

    template = env.get_template("ANNOTATION.md.jinja")
    code = template.render(annotations=annotations)

    # write a python script
    path = Path("../../docs/ANNOTATION.md")
    logger.info(f"write docs/ANNOTATIONM.md to {path}")
    with open(path, "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
