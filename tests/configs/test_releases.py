import pytest
from omegaconf import OmegaConf

from openpack_toolkit.configs import releases


@pytest.mark.parametrize("conf", (
    releases.RELEASE_CONFIG_V0_2_0,
    releases.RELEASE_CONFIG_V0_2_1,
))
def test_releases__ReleaseConfigs__01(conf):
    print(OmegaConf.to_yaml(conf))
