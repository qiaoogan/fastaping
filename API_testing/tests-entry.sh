#!/bin/bash

echo "tests ran in container"
pwd && ls -al
pytest -v --alluredir=./temp --clean-alluredir
allure generate ./temp -o ./report --clean