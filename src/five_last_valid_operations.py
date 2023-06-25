def get_last_five_valid_operations(transactions_list):

    #формируем список транзакции только из исполненных

    executed_list = []

    for transaction in transactions_list:
        try:
            statement = transaction['state']
            if statement == 'EXECUTED':
                executed_list.append(transaction)

        except KeyError:
            pass

    #сортируем список по ключу date и берем первые 5 записей
    sorted_trans_executed_list = sorted(executed_list, key=lambda x: x['date'], reverse=1)
    last_five_trans = sorted_trans_executed_list[:5]

    return last_five_trans
