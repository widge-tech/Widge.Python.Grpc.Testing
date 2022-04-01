FROM python:3.10.2
ADD . /app
VOLUME /app/environments
WORKDIR /app
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ pipenv && pipenv install --system
EXPOSE 3000
CMD [ "python", "./src/main.py" ]
