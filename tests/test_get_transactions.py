import pytest

from src import get_transactions

def test_get_transactions():
    assert get_transactions.get_transactions() != None

