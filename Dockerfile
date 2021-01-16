FROM python:3.8

RUN set -eux \
    && apt-get update -qqy \
    && apt-get install -qqy --no-install-recommends pipenv \
    && apt-get clean \
    && apt-get autoclean
