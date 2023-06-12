import pytest

from course_work_3.src.functions import get_sorted_dates, data, get_date, formatted_date, from_card_number, \
    to_card_number, description, amount, currency, main


@pytest.fixture
def fixture():
    operation_counts = 5
    date = [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]
    return date
def test_get_sorted_dates(fixture):

    assert get_sorted_dates(data) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]

def test_get_date(fixture):
    assert get_date() == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051', '2019-11-05T12:04:13.781725']

def test_formatted_date(fixture):
    assert formatted_date() == ['08-12-2019', '07-12-2019', '19-11-2019', '13-11-2019', '05-11-2019']

def test_from_card_number(fixture):
    assert from_card_number() == [{'Нет данных об отправителе': '---'}, {'VisaClassic': '2842 87** **** 9012'}, {'Maestro': '7810 84** **** 5568'}, {'Счет': '3861 14** **** 9794'}, {'Нет данных об отправителе': '---'}]

def test_to_card_number(fixture):
    assert to_card_number() == [{'Счет': ' **5907'}, {'Счет': ' **3655'}, {'Счет': ' **2869'}, {'Счет': ' **8125'}, {'Счет': ' **8381'}]

def test_description(fixture):
    assert description() == ['Открытие вклада', 'Перевод организации', 'Перевод организации', 'Перевод со счета на счет', 'Открытие вклада']

def test_amount(fixture):
    assert amount() == ['41096.24', '48150.39', '30153.72', '62814.53', '21344.35']

def test_currency(fixture):
    assert currency() == ['USD', 'USD', 'руб.', 'руб.', 'руб.']

def test_main():
    assert main() == "\nСпасибо за работу,хорошего дня!"
