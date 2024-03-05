docker container run \
  --rm \
  --mount type=bind,source="$(pwd)",target=/home/mount \
  -e TEST_ENV="container" \
  -e TEST_HOST="http://123.60.93.173/fastapi" \
  qiaoogan/papitestenv:0.0.1 \
  ash /home/mount/tests-entry.sh