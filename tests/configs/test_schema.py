import pytest
from omegaconf import DictConfig, OmegaConf

from openpack_toolkit.configs._schema import SessionConfig, UserConfig


@pytest.fixture()
def sessions():
    sessions = {
        "S0100": SessionConfig(
            duration="51m2s",
            end="2021-10-22 12:10:19.887000",
            start="2021-10-22 11:19:17.749000"
        ),
        "S0200": SessionConfig(
            duration="39m30s",
            end="2021-10-22 13:10:35.265000",
            start="2021-10-22 12:31:04.594000",
        )
    }
    return sessions


def test_SessionsConfig__01(sessions):
    conf = OmegaConf.create(sessions)
    print(OmegaConf.to_yaml(conf))

    assert isinstance(conf, DictConfig)


def test_UserConfig__01(sessions):
    conf = UserConfig(
        id=102,
        name="U0102",
        sessions=sessions,
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))

    assert isinstance(conf, DictConfig)
