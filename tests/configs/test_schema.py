import pytest
from omegaconf import DictConfig, OmegaConf

from openpack_toolkit import ActClass, ActSet
from openpack_toolkit.configs._schema import (
    AnnotConfig,
    DataLocation,
    DatasetConfig,
    DataSplitConfig,
    DataStreamConfig,
    Label,
    Metadata,
    OpenPackConfig,
    ReleaseConfig,
    SessionConfig,
    UserConfig,
)
from openpack_toolkit.configs.datasets.annotations import OPENPACK_OPERATIONS


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


@pytest.fixture()
def split_conf():
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
    return conf


@pytest.fixture()
def annot_conf():
    conf = AnnotConfig(
        kind="dataset/annotation",
        name="test",
        metadata=Metadata(
            labels={
                "version": "v0.0.0",
            }
        ),
        path=DataLocation(dir="test", fname="test-file.csv"),
        classes=[Label(99, "Test1")],
    )
    return conf


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


def test_DataSplitConfig__01(split_conf):
    conf = OmegaConf.structured(split_conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)

    assert conf.train[0][0] == "U0102"
    assert conf.train[0][1] == "S0100"

# =======================
#  OpenPack Root Config
# =======================


def test_OpenPackConfig__01(split_conf, annot_conf):
    dataset_conf = DatasetConfig(
        name="test",
        streams=None,
        stream=None,
        split=split_conf,
        annotation=annot_conf,
        classes=OPENPACK_OPERATIONS,
    )

    conf = OpenPackConfig(
        path={"dir": "test"},
        dataset=dataset_conf,
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)

# =========
#  Release
# =========


def test_ReleaseConfig__01():
    conf = ReleaseConfig(
        metadata=Metadata(
            labels={
                "version": "v0.0.0",
                "url": "https://xxxx",
            },
        ),
        users={
            "U0101": ReleaseConfig._User(
                sessions=["S0100", "S0200", "S0300", "S0400", "S0500"],
                exclude=["ht"],
            )
        },
        streams={
            "zenodo": ["openpack-operations"],
        }
    )

    conf = OmegaConf.structured(conf)
    print(OmegaConf.to_yaml(conf))
    assert isinstance(conf, DictConfig)
