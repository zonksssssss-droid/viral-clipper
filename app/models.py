from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Clip:
    file: str
    title: str
    caption: str
    hashtags: List[str]
    score: float
    start: float
    end: float
    posting_time: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "title": self.title,
            "caption": self.caption,
            "hashtags": self.hashtags,
            "score": self.score,
            "start": self.start,
            "end": self.end,
            "posting_time": self.posting_time,
        }


@dataclass
class Job:
    id: str
    source_path: Optional[str]
    source_url: Optional[str]
    max_clips: int
    timezone: str
    created_at: str
    status: str = "queued"
    clips: List[Clip] = field(default_factory=list)
    matches: List[Clip] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "source_path": self.source_path,
            "source_url": self.source_url,
            "max_clips": self.max_clips,
            "timezone": self.timezone,
            "created_at": self.created_at,
            "status": self.status,
            "clips": [clip.to_dict() for clip in self.clips],
            "matches": [clip.to_dict() for clip in self.matches],
        }
