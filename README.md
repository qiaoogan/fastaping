# fastaping

### Run API
```commandline
~/.pyenv/versions/3.12.0/bin/python -m uvicorn main:app  --port 8901 --reload
```

### Run API with docker compose
```commandline
# launch
docker-compose -f docker-compose.yaml up -d

# stop
docker-compose -f docker-compose.yaml down -v
```
