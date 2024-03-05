#!/bin/bash

docker container run \
  --rm \
  --mount type=bind,source="$(pwd)",target=/home/mount \
  -e TEST_ENV="container" \
  -e TEST_HOST="http://192.168.2.104:8901" \
  qiaoogan/papitestenv:0.0.2 \
  bash /home/mount/tests-entry.sh