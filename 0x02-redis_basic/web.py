#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In this tasks, we will implement a get_page function (prototype: def get_page
(url: str) -> str:). The core of the function is very simple. 
It uses the requests module to obtain the HTML content of a particular URL and 
returns it.
"""
from functools import wraps
import redis
import requests

redis_client = redis.Redis()


def count_requests(method):
    """ Decorator for counting """
    @wraps(method)
    def wrapper(url):
        key_count = f"count:{url}"
        key_cached = f"cached:{url}"

        cached_value = redis_client.get(key_cached)
        if cached_value:
            return cached_value.decode('utf-8')

        html_content = method(url)

        redis_client.incr(key_count)
        redis_client.setex(key_cached, 10, html_content)

        return html_content

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    response = requests.get(url, timeout=10)
    return response.text


if __name__ == '__main__':
    URL = 'http://slowwly.robertomurray.co.uk'
    print(get_page(URL))
