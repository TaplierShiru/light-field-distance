# For piked version only CUDA from 10.1 to 11.4 supported
# But its work fine with 11.7
ARG CUDA_VERSION=12.1.0
ARG UBUNTU_VERSION=20.04

# GPU version
FROM nvidia/cuda:${CUDA_VERSION}-devel-ubuntu${UBUNTU_VERSION} 

# CPU version
# FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

ARG PYTHON_VER_MAJ=3.10
ARG PYTHON_VER=3.10.2

ARG BLENDER_VERSION_MAJ=3.5
ARG BLENDER_VERSION=3.5.1

ENV PYTHON_SITE_PACKAGES /usr/local/lib/python$PYTHON_VER_MAJ/site-packages/
ENV WITH_INSTALL_PORTABLE OFF
ENV NVIDIA_DRIVER_CAPABILITIES graphics,compute,video,utility

RUN apt-get update
RUN apt-get -y install \
    build-essential \
    cmake \
    curl \
    git \
    libffi-dev \
    libssl-dev \
    libx11-dev \
    libxxf86vm-dev \
    libxcursor-dev \
    libxi-dev \
    libxrandr-dev \
    libxinerama-dev \
    libglew-dev \
    libsm6 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    libosmesa6-dev \
    libbz2-dev \
    subversion \
    zlib1g-dev \
    libsqlite3-dev \
    sudo \
    ncdu \
    freeglut3 \
    freeglut3-dev \
    xvfb

# install python
WORKDIR /home/tmp/python
ADD https://www.python.org/ftp/python/$PYTHON_VER/Python-$PYTHON_VER.tgz Python.tgz
RUN tar xzf Python.tgz
WORKDIR /home/tmp/python/Python-$PYTHON_VER
RUN ./configure --enable-optimizations
RUN make -j$(nproc) install


WORKDIR /home
COPY . .

ENV DISPLAY :99 

RUN cd lfd/3DAlignment/ \
  && make \
  && make release

RUN cd lfd/LightField/ \
  && make \
  && make release 

# Install additional packages
RUN pip3 install numpy Pillow matplotlib jupyterlab trimesh
WORKDIR /home
RUN python3 setup.py install

# test if it works
# RUN Xvfb :99 -screen 0 1900x1080x24+32 & export DISPLAY=:99 && python3 test.py
