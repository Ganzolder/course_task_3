from src.operation_convert import Transaction
import src.get_transactions as get_trans
from src.five_last_valid_operations import get_last_five_valid_operations as get_5


def main():
    # основная функция вызова и обработки запросов

    url = 'https://api.npoint.io/369c3f185c6c1d7b30c3'

    response = get_trans.get_transactions(url)  # делаем запрос к внешнему json
    transactions_list = get_trans.response_convert(response)  # преобразуем в список словарей
    data_list = get_5(transactions_list)  # сортируем список и получем последние 5 операций в виде списка словарей

    for transaction in data_list:
        # создаем объекты

        record = Transaction(date=transaction['date'], description=transaction['description'],
                             from_=transaction.get('from'), to_=transaction['to'],
                             operation_amount=transaction['operationAmount'], id_=transaction['id'],
                             currency=transaction['operationAmount']['currency'])

        # выводим результат

        print(f'{record.date_converter(record.date)} {record.description}\n'
              f'{record.from_converter(record.from_)} -> {record.to_converter(record.to_)}\n'
              f'{record.calculate_operation_amount(record.operation_amount, record.currency)}\n')


if __name__ == '__main__':
    main()
