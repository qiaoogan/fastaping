# from ..clients.TestClient import *
# import pytest
#
# book = {
#     "name": "pytest",
#     "author": "pytest",
#     "publishedAt": "2024-03-01",
#     "price": 100.0,
#     "stock": 200
# }
#
#
# updated_book = {
#     "name": "pytest_updated",
#     "author": "pytest_updated",
#     "publishedAt": "2024-05-01",
#     "price": 55.0,
#     "stock": 117
# }
#
#
# def test_create_book():
#     res = create_book(book)
#     assert res.status_code == 201
#     assert res.json() == book
#
#     book_to_verify = get_book(book["name"])
#     assert book_to_verify.json() == book
#
#
# def test_get_all_books():
#     res = get_all_books()
#     assert res.status_code == 200
#
#
# def test_change_book():
#     res = modify_book(book["name"], updated_book)
#     assert res.status_code == 200
#     assert res.json() == updated_book
#
#
# def test_delete_book():
#     res = delete_book(book['name'])
#     assert res.status_code == 200
