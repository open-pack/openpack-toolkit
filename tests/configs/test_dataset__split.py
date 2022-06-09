import pytest
from omegaconf import OmegaConf

from openpack_toolkit.configs import datasets


@pytest.mark.parametrize("conf", (
    datasets.splits.DEBUG_SPLIT,
    datasets.splits.PILOT_CHALLENGE_SPLIT,
))
def test_users__DataSplitConfigs__01(conf):
    print(OmegaConf.to_yaml(conf))
