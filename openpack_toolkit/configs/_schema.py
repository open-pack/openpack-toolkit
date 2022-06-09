from dataclasses import dataclass
from typing import Dict, List, Optional

from omegaconf import MISSING

# ======
#  User
# ======


@dataclass
class SessionConfig:
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
    train: Optional[List[List]] = None
    val: Optional[List[List]] = None
    test: Optional[List[List]] = None
    submission: Optional[List[List]] = None


@dataclass
class DataStreamConfig:
    @dataclass
    class Paths:
        # path to the root directory of this stream.
        rootdir: Optional[str] = None
        template: Optional[str] = None

    schema: str = MISSING
    name: str = MISSING
    description: Optional[str] = None
    path: Paths = MISSING
    frame_rate: int = MISSING  # [Hz, fps]


@dataclass
class ImuConfig(DataStreamConfig):
    schema: str = "ImuConfig"
    nodes: List[str] = MISSING
    acc: bool = True
    gyro: bool = True
    quat: bool = True


@dataclass
class KeypointConfig(DataStreamConfig):
    schema: str = "KeypointConfig"
    category: str = MISSING
    model: str = MISSING
    nodes: Dict[int, str] = MISSING
