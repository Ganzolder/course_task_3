import requests

def get_transactions(url):
    response = requests.get(url)
    return response

def response_convert(response):
    transactions = response.json()
    return(transactions)




