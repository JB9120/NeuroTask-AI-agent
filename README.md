
# NeuroTask SaaS

Enterprise AI Todo Agent SaaS

## Run locally

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Build Docker

```bash
docker build -t neurotask .
docker run -p 8000:8000 neurotask
```

Generated: 2026-02-25 17:26:17.992035
