import datetime
import re


class Transaction:
    def __init__(self, id_, date, operation_amount, currency, description, from_, to_):
        self.id_ = id_
        self.date = date
        self.operation_amount = operation_amount
        self.currency = currency
        self.description = description
        self.from_ = from_
        self.to_ = to_

    def date_converter(self, date):
        short_date = date[:date.find('T')]
        date_operation = datetime.datetime.strptime(short_date, "%Y-%m-%d").strftime("%d.%m.%Y")
        return date_operation

    def calculate_operation_amount(self, operation_amount, currency):
        operation_sum = f'{operation_amount} {currency}'
        return operation_sum

    def from_converter(self, from_):
        i = 6

        devided_card = from_.split()

        first_digits = devided_card[1][:6]
        last_digits = devided_card[1][-4:]

        crypted_number = f'{first_digits}******{last_digits}'
        grouped_digits = re.findall('....', crypted_number)

        crypted_card = f'{devided_card[0]} {" ".join(grouped_digits)}'

        return crypted_card

    def to_converter(self, to_):

        devided_account = to_.split()
        account_digits = devided_account[1]
        account_last_digits = account_digits[-4:]
        crypted_account = f'{devided_account[0]} **{account_last_digits}'

        return crypted_account
