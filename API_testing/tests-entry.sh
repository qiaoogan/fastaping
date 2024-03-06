#!/bin/bash

echo "tests ran in container"
pytest -v --alluredir=./allure-results --clean-alluredir
rm -rf allure-report && pwd && al -al
allure generate allure-results -c -o allure-report
pwd && al -al