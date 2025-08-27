FROM python:3.13-slim-bullseye AS dev
COPY . /workspaces/gufo_loader
WORKDIR /workspaces/gufo_loader
RUN \
    set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends\
    git\
    curl\
    && curl -L -o /tmp/liftbridge.tgz https://github.com/liftbridge-io/liftbridge/releases/download/v1.9.0/liftbridge_1.9.0_linux_amd64.tar.gz\
    && (cd /tmp && tar zxf /tmp/liftbridge.tgz liftbridge && mv liftbridge /usr/local/bin)\
    && rm /tmp/liftbridge.tgz\
    && pip install --upgrade pip\
    && pip install --upgrade build\
    && pip install -e .[dev,test,lint,docs,ipython]