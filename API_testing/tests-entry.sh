#!/bin/bash

echo "tests ran in container"
pwd && ls -al
pytest -v -s