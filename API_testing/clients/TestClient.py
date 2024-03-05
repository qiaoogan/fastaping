import os
from utils.request_utils import post, put, get, delete

HOST = os.environ.get("TEST_HOST") if os.environ.get("TEST_ENV") == "container" else "http://localhost:8901"


class Config:
    host = HOST
    health = "/health"
    book_base = "/stock/book"


book_url = Config.host + Config.book_base


def get_health():
    url = Config.host + Config.health
    return get(url)


def create_book(book):
    return post(book_url, payload=book)


def get_all_books():
    return get(book_url)


def get_book(book_name):
    url = book_url + "/" + book_name
    return get(url)


def modify_book(book_name, book):
    url = book_url + "/" + book_name
    return put(url, payload=book)


def delete_book(book_name):
    url = book_url + "/" + book_name
    return delete(url)
