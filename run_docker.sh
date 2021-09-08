#!/usr/bin/env bash

docker build --tag=app .

docker run -p 5000:5000 app