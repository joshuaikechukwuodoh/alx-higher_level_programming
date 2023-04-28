#!/bin/bash
# Get the body size of a request
curl -Is "$1" | awk '/Content-Length/ {print $2}'

