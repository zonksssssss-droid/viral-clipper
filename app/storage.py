from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from app.config import DATA_DIR
from app.models import Job


JOB_ROOT = DATA_DIR / "jobs"
JOB_ROOT.mkdir(parents=True, exist_ok=True)


def job_path(job_id: str) -> Path:
    return JOB_ROOT / f"{job_id}.json"


def save_job(job: Job) -> None:
    job_path(job.id).write_text(json.dumps(job.to_dict(), indent=2), encoding="utf-8")


def load_job(job_id: str) -> Optional[Job]:
    path = job_path(job_id)
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    from app.models import Clip

    clips = [Clip(**clip) for clip in data.get("clips", [])]
    matches = [Clip(**clip) for clip in data.get("matches", [])]
    job = Job(
        id=data["id"],
        source_path=data.get("source_path"),
        source_url=data.get("source_url"),
        max_clips=data.get("max_clips", 3),
        timezone=data.get("timezone", "UTC"),
        created_at=data.get("created_at", ""),
        status=data.get("status", "queued"),
        clips=clips,
        matches=matches,
    )
    return job


def ensure_source_dir(job_id: str) -> Path:
    job_dir = JOB_ROOT / job_id
    job_dir.mkdir(parents=True, exist_ok=True)
    return job_dir


def write_placeholder_clip(path: Path) -> None:
    path.write_bytes(b"\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00\x00\x00\x00\x00demo-clip")
