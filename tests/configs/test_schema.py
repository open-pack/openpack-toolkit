import pytest
from omegaconf import DictConfig, OmegaConf

from openpack_toolkit.configs._schema import (
    DataSplitConfig,
    DataStreamConfig,
    ImuConfig,
    KeypointConfig,
    SessionConfig,
    UserConfig,
)


@pytest.fixture()
def sessions():
    sessions = {
        "S0100": SessionConfig(
            duration="50m13s",
            end="2021-10-22T12:10:07+09:00",
            start="2021-10-22T11:19:54+09:00",
        ),
        "S0200": SessionConfig(
            duration="39m8s",
            end="2021-10-22T13:10:22+09:00",
            start="2021-10-22T12:31:14+09:00",
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


def test_DataSplitConfig__01():
    conf = DataSplitConfig(
        train=[
            ["U0102", "S0100"],
            ["U0102", "S0200"],
            ["U0102", "S0300"],
        ],
        val=[
            ["U0102", "S0400"],
        ],
        test=[
            ["U0102", "S0500"],
        ],
        submission=[
            ["U0102", "S0500"],
        ]
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)

    assert conf.train[0][0] == "U0102"
    assert conf.train[0][1] == "S0100"


def test_ImuConfig__01():
    conf = ImuConfig(
        name="atr-acc",
        description="hoge hoge hoge",
        super_stream="atr-qags",
        path=DataStreamConfig.Paths(
            dir="/foo/subdir",
            fname="huga.csv",
        ),
        frame_rate=30,
        devices=["atr01", "atr02", "atr03", "atr04"],
        acc=True,
        gyro=False,
        quat=False,
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)


def test_KeypointConfig__01():
    conf = KeypointConfig(
        name="atr-acc",
        description="hoge hoge hoge",
        super_stream=None,
        path=DataStreamConfig.Paths(
            dir="/foo/subdir",
            fname="huga.csv",
        ),
        frame_rate=30,
        category="2d-kpt",
        model="foo-hrnet",
        nodes={0: "node0", 1: "node1"},
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)
