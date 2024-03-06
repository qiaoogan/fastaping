#!/bin/bash

docker container run \
  --rm \
  --mount type=bind,source="$(pwd)",target=/home/mount \
  -e TEST_ENV="container" \
  -e TEST_HOST="http://host.docker.internal:31101" \
  qiaoogan/papitestenv:0.0.3 \
  bash /home/mount/tests-entry.sh