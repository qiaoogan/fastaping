import requests


def get(url, headers=None, params=None):
    return requests.get(url, headers=headers, params=params)


def post(url, headers=None, payload=None):
    return requests.post(url, headers=headers, json=payload)


def put(url, headers=None, payload=None):
    return requests.put(url, headers=headers, json=payload)


def delete(url, headers=None):
    return requests.delete(url, headers=headers)


# if __name__ == "__main__":
#     print("testing requestUtils:")
#
#     url = "http://hw.dogger.instance/dashbackend/health"
#     response = get(url)
#     print(response.json())
#     print(response.json()['status'])
#     print(response.json()['version'])