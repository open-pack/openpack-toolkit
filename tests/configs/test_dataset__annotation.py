import pytest
from omegaconf import OmegaConf

from openpack_toolkit.configs import datasets


@pytest.mark.parametrize("conf", (
    datasets.annotations.OPENPACK_OPERATIONS_ANNOTATION,
    datasets.annotations.OPENPACK_ACTIONS_ANNOTATION,
))
def test_users__AnnotConfigs__01(conf):
    print(OmegaConf.to_yaml(conf))
