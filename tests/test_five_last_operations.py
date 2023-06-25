from src.five_last_valid_operations import get_last_five_valid_operations as last_five


def test_last_five():
    test_trans_list = [{'id': 441945886, 'to': 'Счет 64686473678894779589', 'date': '2019-08-26T10:50:58.294041',
                        'from': 'Maestro 1596837868705199', 'state': 'EXECUTED', 'description': 'Перевод организации',
                        'operationAmount': {'amount': '31957.58', 'currency': {'code': 'RUB', 'name': 'руб.'}}},
                       {'id': 41428829, 'to': 'Счет 35383033474447895560', 'date': '2019-07-03T18:35:29.512364',
                        'from': 'MasterCard 7158300734726758', 'state': 'EXECUTED',
                        'description': 'Перевод организации',
                        'operationAmount': {'amount': '8221.37', 'currency': {'code': 'USD', 'name': 'USD'}}}]
    result = last_five(test_trans_list)
    assert len(result) == 2
    assert type(result) == list
    assert type(result[0]) == dict
