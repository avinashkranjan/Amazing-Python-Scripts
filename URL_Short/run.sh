#!/bin/bash

docker stop urlshortener_server;
docker build -t url_shortener . \
&& docker run -dit --rm -p 8000:8000 --name urlshortener_server url_shortener
