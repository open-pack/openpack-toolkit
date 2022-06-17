from dataclasses import dataclass
from typing import Dict, List, Optional

from omegaconf import MISSING

from ..activity import ActSet

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
class DataStreamConfig:
    """
    Attributes:
        schema (str): -
        name (str): -
        description (str): -
        super_stream (str): Parent Class. Inherited from.
        path (DatasetStream.Path): -
        frame_rate (int): -
    """

    @dataclass
    class Paths:
        # path to the root directory of this stream.
        dir: Optional[str] = None
        fname: Optional[str] = None

    schema: str = MISSING
    name: str = MISSING
    description: Optional[str] = None
    super_stream: Optional[str] = None
    path: Paths = MISSING
    file_format: Optional[Dict] = None
    frame_rate: int = MISSING  # [Hz, fps]


@dataclass
class ImuConfig(DataStreamConfig):
    schema: str = "ImuConfig"
    devices: List[str] = MISSING
    acc: bool = True
    gyro: bool = True
    quat: bool = True


@dataclass
class KeypointConfig(DataStreamConfig):
    schema: str = "KeypointConfig"
    category: str = MISSING
    model: str = MISSING
    nodes: Dict[int, str] = MISSING


@dataclass
class AnnotConfig:
    name: str = MISSING
    version: str = MISSING
    path: Dict[str, str] = MISSING
    file_format: Optional[Dict[str, str]] = None
    classes: ActSet = MISSING


@dataclass
class DatasetConfig:
    name: str = MISSING
    streams: Dict[str, DataStreamConfig] = MISSING
    split: DataSplitConfig = MISSING
    annot: AnnotConfig = MISSING
