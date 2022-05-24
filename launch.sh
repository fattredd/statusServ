#!/usr/bin/env bash

docker run \
    --rm \
    -p 5000:5000 \
    -v `pwd`/src/config:/app/config \
    -v `pwd`/src/data:/app/data \
    status-serv:latest
