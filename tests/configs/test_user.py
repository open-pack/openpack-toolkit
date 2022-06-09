import pytest
from omegaconf import OmegaConf

from openpack_toolkit.configs import users


@pytest.mark.parametrize("conf", (
    users.U0102,
    users.U0103,
    users.U0105,
    users.U0106,
    users.U0107,
))
def test_users__UserConfigs__01(conf):
    print(OmegaConf.to_yaml(conf))
