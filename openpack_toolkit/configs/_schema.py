from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from omegaconf import MISSING

from ..activity import ActSet

# ======
#  Core
# ======


@dataclass
class Metadata:
    labels: Optional[Dict[str, str]] = None


@dataclass
class DataLocation:
    dir: str = MISSING
    fname: str = MISSING

@dataclass
class BaseConfig:
    kind: str = MISSING
    name: str = MISSING
    metadata: Metadata = MISSING

# ======
#  User
# ======


@dataclass
class SessionConfig:
    """
    Attributes:
        start (str): Timestamp of session start time (IOS format)
        end (str): Timestamp of session end time (IOS format)
        duration (str): length of session, i.e., end - start
    """
    duration: str = MISSING
    end: str = MISSING
    start: str = MISSING


@dataclass
class UserConfig:
    id: int = MISSING
    name: str = MISSING
    sessions: Dict[str, SessionConfig] = MISSING  # DictConfig


# =========
#  Dataset
# =========


@dataclass
class DataSplitConfig:
    name: str = MISSING
    train: Optional[List[List]] = None
    val: Optional[List[List]] = None
    test: Optional[List[List]] = None
    submission: Optional[List[List]] = None


@dataclass
class DataStreamConfig(BaseConfig):
    path: DataLocation = MISSING
    frameRate: int = MISSING  # [Hz, fps]

    # for IMU/E4
    devices: Optional[List[str]] = None
    acc: Optional[bool] = None
    gyro: Optional[bool] = None
    quat: Optional[bool] = None

    # for keypoints
    nodes: Optional[Dict[int, str]] = MISSING


# @dataclass
# class ImuConfig(DataStreamConfig):
#     schema: str = "ImuConfig"
#     devices: List[str] = MISSING
#     acc: bool = True
#     gyro: bool = True
#     quat: bool = True


# @dataclass
# class E4Config(DataStreamConfig):
#     schema: str = "E4Config"
#     devices: List[str] = MISSING
#     sensor: str = MISSING


# @dataclass
# class KeypointConfig(DataStreamConfig):
#     schema: str = "KeypointConfig"
#     category: str = MISSING
#     model: str = MISSING
#     nodes: Dict[int, str] = MISSING


# @dataclass
# class SystemDataConfig(DataStreamConfig):
#     schema: str = "SystemDataConfig"

@dataclass
class Label():
    """dataclass that represent a single activity class.
    """
    id: Union[int, str] = MISSING
    name: str = MISSING
    version: str = MISSING
    is_ignore: bool = False
    category: Optional[str] = None
    event: Optional[str] = None


@dataclass
class AnnotConfig(BaseConfig):
    # conf_type: str = MISSING
    # name: str = MISSING
    # version: str = MISSING
    # path: Optional[Dict[str, str]] = MISSING
    # file_format: Optional[Dict[str, str]] = None

    path: DataLocation = MISSING
    classes: List[Label] = MISSING
    # activity_sets: Optional[Dict] = None


@dataclass
class DatasetConfig:
    name: str = MISSING
    streams: Optional[Dict[str, DataStreamConfig]] = None
    stream: Optional[DataStreamConfig] = None
    split: DataSplitConfig = MISSING
    annotation: AnnotConfig = MISSING
    classes: Optional[ActSet] = MISSING


# =========
#  Release
# =========
@dataclass
class ReleaseConfig(BaseConfig):
    @dataclass
    class _User:
        sessions: List[str] = MISSING
        exclude: Optional[List[str]] = MISSING
    
    users: Dict[str, _User] = MISSING
    streams: Dict[str, List[str]] = MISSING


# =======================
#  OpenPack Root Config
# =======================

@dataclass
class OpenPackConfig:
    path: Optional[Dict] = None
    dataset: DatasetConfig = MISSING
    release: Optional[ReleaseConfig] = None
