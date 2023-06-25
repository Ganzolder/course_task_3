from src.operation_convert import Transaction


def test_operation_amount():
    # тест суммы получателя

    test_obj = Transaction(123, '19.06.2023', {"amount": "31957.58"}, {"name": "руб.", "code": "RUB"},
                           'просто так', '***123', '*5434')
    result = test_obj.calculate_operation_amount({"amount": "31957.58"}, {"name": "руб.", "code": "RUB"})
    assert result == '31957.58 руб.'


def test_date():
    # тест даты

    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', '***123', '*5434')
    result = test_obj.date_converter('2019-08-26T10:50:58.294041')
    assert result == '26.08.2019'


def test_from_():
    # тест отправителя

    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', 'Maestro 1596837868705199',
                           '*5434')
    result = test_obj.from_converter('Maestro 1596837868705199')
    assert result == 'Maestro 1596 83** **** 5199'


def test_to_():
    # тест получателя

    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', 'Maestro 1596837868705199',
                           'Счет 64686473678894779589')
    result = test_obj.to_converter('Счет 64686473678894779589')
    assert result == 'Счет **9589'
