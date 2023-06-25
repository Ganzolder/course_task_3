import datetime
import re


class Transaction:

    # создаем класс для работы с данными json  и преобразования их в требуемый формат

    def __init__(self, id_, date, operation_amount, currency, description, to_, from_='Неизвестно'):
        self.id_ = id_
        self.date = date
        self.operation_amount = operation_amount
        self.currency = currency
        self.description = description
        self.from_ = from_
        self.to_ = to_

    def date_converter(self, date):

        # конвертируем дату в требуемую

        short_date = date[:date.find('T')]
        date_operation = datetime.datetime.strptime(short_date, "%Y-%m-%d").strftime("%d.%m.%Y")
        return date_operation

    def calculate_operation_amount(self, operation_amount, currency):

        # конвертируем сумму

        sum_operation = operation_amount['amount']
        cur_operation = currency['name']
        operation_sum = f'{sum_operation} {cur_operation}'
        return operation_sum

    def from_converter(self, from_):

        # конвертируем отправителя
        account_crypted_digits = 0
        grouped_digits = 0

        if from_ is not None:
            devided_card = from_.split()
            try:
                int(devided_card[1])
                first_digits = devided_card[1][:6]
                last_digits = devided_card[1][-4:]
            except ValueError:
                first_digits = devided_card[2][:6]
                last_digits = devided_card[2][-4:]

            if devided_card[0].lower() == 'счет':
                account_crypted_digits = f'**{devided_card[1][-4:]}'
            else:
                crypted_number = f'{first_digits}******{last_digits}'
                grouped_digits = re.findall('....', crypted_number)

            try:
                int(devided_card[1])
                if devided_card[0].lower() == 'счет':
                    crypted_card = f'{devided_card[0]} {account_crypted_digits}'
                else:
                    crypted_card = f'{devided_card[0]} {" ".join(grouped_digits)}'
            except ValueError:
                crypted_card = f'{devided_card[0]} {devided_card[1]} {" ".join(grouped_digits)}'
            return crypted_card

        else:
            return 'Неизвестный отправитель'

    def to_converter(self, to_):

        # конвертируем получателя

        devided_account = to_.split()
        account_digits = devided_account[1]
        account_last_digits = account_digits[-4:]
        crypted_account = f'{devided_account[0]} **{account_last_digits}'

        return crypted_account
