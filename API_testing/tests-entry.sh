#!/bin/bash

echo "tests ran in container"
pwd && ls -al
pytest -v --alluredir=./allure-results --clean-alluredir