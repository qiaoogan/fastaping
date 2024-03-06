FROM python:3.12-alpine
WORKDIR /home/testenv

COPY ./requirements.txt .
RUN apk add bash curl openjdk11
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  -r requirements.txt

COPY ./allure.zip .
RUN unzip allure.zip -d allure
ENV PATH="${PATH}:/home/testenv/allure/bin"

CMD ["tail", "-f", "/dev/null"]