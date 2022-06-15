import pytest
from omegaconf import OmegaConf

from openpack_toolkit.configs import datasets


@pytest.mark.parametrize("conf", (
    datasets.streams.ATR_ACC_STREAM,
    datasets.streams.ATR_QAGS_STREAM,
    datasets.streams.KINECT_2D_KPT_STREAM,
))
def test_users__DataStreamConfigs__01(conf):
    print(OmegaConf.to_yaml(conf))
