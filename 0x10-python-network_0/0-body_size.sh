#!/bin/bash
import requests

def get_body_size(url):
    response = requests.head(url)
    content_length = response.headers.get('Content-Length')
    return int(content_length) if content_length else None

