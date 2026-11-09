# Viral Clipper backend

Paste a video (upload or link) -> AI finds the moments most likely to perform as short clips,
writes titles/captions/hashtags, suggests posting times, and cuts the clips. It also supports
"find me the part where..." natural-language search.

## Setup

1. Install FFmpeg.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Copy the environment example and fill in secrets:
   ```bash
   cp .env.example .env
   ```
4. Run locally:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Open http://localhost:8000

## API examples

```bash
curl -F file=@video.mp4 -F max_clips=5 -F timezone=America/New_York http://localhost:8000/jobs
curl http://localhost:8000/jobs/<job_id>
curl -X POST http://localhost:8000/jobs/<job_id>/find -H 'Content-Type: application/json' -d '{"query":"every time someone laughs","max_results":5}'
curl -o clip.mp4 http://localhost:8000/jobs/<job_id>/clips/viral_ab12cd34.mp4
```

## Production deployment

See `DEPLOY.md` for Docker, Render, and Caddy setup.

## Notes

- This starter app includes a working backend and browser UI with a simulated clip-generation pipeline.
- Real video analysis and AI clipping can be wired in to a hosted model provider or local FFmpeg workflow.
- State is stored on disk under `DATA_DIR` and is intentionally simple for a demo/prototype deployment.
