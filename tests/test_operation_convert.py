import pytest
from src.operation_convert import Transaction


def test_operation_amount():
    test_obj = Transaction(123, '19.06.2023', 456, 'руб.', 'просто так', '***123', '*5434')
    result = test_obj.calculate_operation_amount(456, 'руб.')
    assert result == '456 руб.'

def test_date():
    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', '***123', '*5434')
    result = test_obj.date_converter('2019-08-26T10:50:58.294041')
    assert result == '26.08.2019'

def test_from_():
    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', 'Maestro 1596837868705199', '*5434')
    result = test_obj.from_converter('Maestro 1596837868705199')
    assert result == 'Maestro 1596 83** **** 5199'

def test_to_():
    test_obj = Transaction(123, '2019-08-26T10:50:58.294041', 456, 'руб.', 'просто так', 'Maestro 1596837868705199', 'Счет 64686473678894779589')
    result = test_obj.to_converter('Счет 64686473678894779589')
    assert result == 'Счет **9589'