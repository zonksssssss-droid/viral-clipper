import os
from pathlib import Path

DATA_DIR = Path(os.getenv("DATA_DIR", "./data")).resolve()
APP_PASSWORD = os.getenv("APP_PASSWORD")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DOMAIN = os.getenv("DOMAIN", "localhost")
MAX_VIDEO_MINUTES = int(os.getenv("MAX_VIDEO_MINUTES", "8"))
MAX_JOBS_PER_HOUR = int(os.getenv("MAX_JOBS_PER_HOUR", "20"))
RETENTION_HOURS = int(os.getenv("RETENTION_HOURS", "48"))
FRAME_INTERVAL = float(os.getenv("FRAME_INTERVAL", "2"))
REFINE = int(os.getenv("REFINE", "1"))

DATA_DIR.mkdir(parents=True, exist_ok=True)
