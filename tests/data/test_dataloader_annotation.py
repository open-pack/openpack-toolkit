from pathlib import Path

from openpack_toolkit.data.const import (
    CLASS_ID_KEY_NAME,
    END_UNIX_TIME_KEY_NAME,
    START_UNIX_TIME_KEY_NAME,
)
from openpack_toolkit.data.dataloader.annotation import load_annotation_csv

pytest_plugins = "tests.data.dataset_fixtures"


def test_load_annotation_csv(operation_labels_path: Path):
    df = load_annotation_csv(operation_labels_path)

    assert START_UNIX_TIME_KEY_NAME in df.columns
    assert END_UNIX_TIME_KEY_NAME in df.columns
    assert CLASS_ID_KEY_NAME in df.columns
