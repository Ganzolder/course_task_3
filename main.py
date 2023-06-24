from src.operation_convert import Transaction
import src.get_transactions as get_trans

url = 'https://api.npoint.io/369c3f185c6c1d7b30c3'

response = get_trans.get_transactions(url)
transactions_list = get_trans.response_convert(response)

executed_list = []

for transaction in transactions_list:
    try:
        statement = transaction['state']
        if statement == 'EXECUTED':
            executed_list.append(transaction)
    except KeyError:
        pass


print(len(executed_list))
'''
test_list = []
first = transactions_list[0]['date'][:10]
second = transactions_list[5]['date'][:10]
third = transactions_list[10]['date'][:10]
test_list.append(first)
test_list.append(second)
test_list.append(third)

sorted_test_list = sorted(test_list)
print(first, second, third, sorted_test_list)'''