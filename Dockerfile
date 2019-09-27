FROM python:3.6 as developer
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install tor -y && apt-get install python-stem

WORKDIR /usr/src/app
ADD . /usr/src/app/

RUN sh torconfig.sh
RUN pip3 install -r requirements.txt
