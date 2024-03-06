#!/bin/bash

echo "tests ran in container"
pytest -v --alluredir=./allure-results --clean-alluredir
rm -rf allure-report && pwd && ls -al
echo $PATH
allure generate allure-results -c -o allure-report
pwd && ls -al