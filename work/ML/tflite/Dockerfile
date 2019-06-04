FROM ubuntu:16.04

## 设置源为阿里
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt-get clean && \ 
    apt-get update 
## 安装依赖库
RUN apt-get install  -y g++-arm-linux-gnueabihf && \
    apt-get install -y gcc-arm-linux-gnueabihf

WORKDIR /home/root

COPY  ./tensorflow ./tensorflow

RUN  ./tensorflow/contrib/lite/download_dependencies.sh 