docker run --rm \
  --user 1000:1000 \
  --read-only \
  -v "$(pwd)":/app \
  python:3.11-slim \
  bash -c "pip install -r requirements.txt && pytest" 