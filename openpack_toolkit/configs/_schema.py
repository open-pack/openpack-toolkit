from dataclasses import dataclass
from typing import Dict

from omegaconf import MISSING


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
