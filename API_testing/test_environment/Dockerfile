FROM python:3.12-alpine
WORKDIR /home/mount

COPY ./requirements.txt .
RUN apk add bash curl openjdk11
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  -r requirements.txt

COPY ./allure.zip .
RUN unzip allure.zip -d allure
ENV PATH="${PATH}:/home/mount/allure/bin"

CMD ["tail", "-f", "/dev/null"]