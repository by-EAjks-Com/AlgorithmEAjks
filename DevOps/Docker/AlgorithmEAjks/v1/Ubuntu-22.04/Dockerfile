#   Copyright (C) 2020-2023 Andrea and Eric DELAGE <Contact@by-EAjks.Com>
#   See the file "LICENSE" for the full license governing this code.

FROM ubuntu:22.04

LABEL maintainer "by-EAjks.Com <Contact@by-EAjks.Com>"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris

RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends \
        build-essential \
        cmake \
        python3 \
        python3-pip \
        python3-venv \
        swig && \
    apt-get autoremove --yes --purge && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN python3 -m venv .venv && \
    . ./.venv/bin/activate && \
    pip  install --upgrade "pip>=23.0.1,<24" && \
    pip  install --upgrade "tox>=4.4.6" && \
    pip  install --upgrade "check-manifest>=0.49" && \
    pip  install --upgrade "flake8>=6.0.0,<7" && \
    pip  install --upgrade "pytest>=7.2.1,<8" && \
    pip  install --upgrade "build>=0.10.0" && \
    pip  install --upgrade "twine>=4.0.2,<5" && \
    pip  install --upgrade "setuptools>=67.4.0,<68" && \
    pip  install --upgrade "coverage>=7.2.0,<8" && \
    pip  install --upgrade "wheel>=0.38.4" && \
    pip  install --upgrade "pipx>=1.1.0,<2" && \
    pipx install "jupyterlab"

ENV PATH=/root/.local/bin${PATH:+:${PATH}}
