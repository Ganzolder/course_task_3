from src import get_transactions

url = 'https://api.npoint.io/369c3f185c6c1d7b30c3'


def test_get_transactions():
    # тест запроса

    response = get_transactions.get_transactions(url)
    assert response.status_code == 200


def test_response_conert():
    # тест преобразования json

    response = get_transactions.get_transactions(url)
    assert type(response.json()) == list
