import requests

def get_transactions():
    response = requests.get('https://api.npoint.io/369c3f185c6c1d7b30c3')
    transactions = response.json()
    return transactions

