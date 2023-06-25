import requests


def get_transactions(url):
    # делаем запрос в удаленный json

    response = requests.get(url)
    return response


def response_convert(response):
    # конвертируем запрос в спсиок словарей python

    transactions = response.json()
    return transactions
