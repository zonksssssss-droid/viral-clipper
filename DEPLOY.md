# Deploying Viral Clipper

The app needs FFmpeg, disk space for videos, and a few minutes of CPU per video, so it is best hosted on a
server or container host rather than a static host. Two good paths:

## Option A: small VPS with Docker (most control)
1. Create a Linux VPS with at least 2 vCPUs, 4 GB RAM, and 40+ GB disk.
2. Point your domain's A record at the server.
3. Install Docker and clone this repository onto the host.
4. Create `.env` from `.env.example` and set `ANTHROPIC_API_KEY`, `APP_PASSWORD`, and `DOMAIN`.
5. Start the stack:
   ```bash
   docker compose up -d --build
   ```
6. Open `https://your-domain`.

## Option B: Render
1. Push this repository to GitHub.
2. In Render, create a new Blueprint from the repo.
3. Add `ANTHROPIC_API_KEY` and `APP_PASSWORD` when prompted.
4. Note that persistent disk is needed for video storage and large uploads may be limited by your plan.

## Before sharing the link
- Set `APP_PASSWORD`.
- Add a monthly spend cap on your Anthropic account.
- Keep `MAX_VIDEO_MINUTES` and `MAX_JOBS_PER_HOUR` at sensible values.
- Download clips you want to keep before retention expires.

## Scaling later
This starter app keeps state in JSON files and runs jobs in an in-process async task queue. For higher scale, move state to Postgres, jobs to a queue such as RQ/Celery, and files to object storage.
