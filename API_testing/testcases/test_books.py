# import requests
# import pytest
# import os
#
# # /stock/book, POST ---> 创建单个book的数据；
#
#
# host = os.environ.get("TEST_HOST") if os.environ.get("TEST_ENV") == "container" else "http://localhost:8901"
#
# @pytest.mark.skip
# def test_createBook():
#     book = {
#         "name": "Book dogger",
#         "author": "Postman",
#         "publishedAt": "2024-03-01",
#         "price": 100,
#         "stock": 200
#     }
#     response = requests.post(f"{host}/stock/book/",json=book)
#
#     assert response.status_code == 201
#     assert response.json() == book
#
#
# @pytest.fixture()
# def getBook(book_name):
#     response = requests.get(f"{host}/stock/book/{book_name}")
#     assert response.status_code == 200
#     return response.json()
#
#
# @pytest.mark.parametrize("book_name",["Book A", "Book B", "Book"])
# def test_getBook(getBook,book_name):
#     assert getBook['name'] == book_name
#
#
# # /stock/book, GET ---> 查询books的数据；
# def test_getAllBooks():
#     response = requests.get(f"{host}/stock/book/")
#     assert response.status_code == 200
#     assert response.json()[0]['name'] == "Book A"
