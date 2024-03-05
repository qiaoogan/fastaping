FROM python:3.12-alpine
WORKDIR /home/mount
COPY ./requirements.txt .
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  -r requirements.txt

CMD ["tail", "-f", "/dev/null"]