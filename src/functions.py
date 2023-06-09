import json
from datetime import datetime

with open("/home/aliaksandr_sigai/course_work_3/operations.json", "r") as file:
    data = json.load(file)

operation_counts = int(input("Введите количество операций: "))

def get_sorted_dates(data):
    """Сортируем по дате и возвращаем только необходимое количество элементов"""
    formatted_dates = []
    result = []
    for operation in data:
        if "date" in operation:# and operation.get("state") == "EXECUTED":
            formatted_dates.append(operation)
        #elif "date" in operation and operation.get("state") == "CANCELED":
    sorted_dates = sorted(formatted_dates, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    for item in sorted_dates:
        result.append(item)
    return result

def get_status():
    """Получение статуса операции"""
    status = get_sorted_dates(data)
    result_status = []
    for x in status:
        if x["state"] == "EXECUTED":
            result_status.append("выполнена")
        else :
            result_status.append("отменена")
    return result_status[:operation_counts]


def get_id():
    """id платежа"""
    status = get_sorted_dates(data)
    result_status = []
    for x in status:
        if "id" in x:
            result_status.append(x["id"])
    return result_status[:operation_counts]

def get_date():
    """Из необходимого количества элементов возвращаем только значение по ключу 'date'"""
    date_time = get_sorted_dates(data)
    date_list = []
    for x in date_time:
        if "date" in x:
            date_list.append(x["date"])

    return date_list[:operation_counts]

def formatted_date():
    """Форматируем даты в нужном порядке"""
    date = get_date()
    formatted_dates = []
    for date_str in date:
        formatted = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_dates.append(formatted.strftime("%d-%m-%Y"))

    return formatted_dates

def from_card_number():
    """Получение номера отправителя"""
    info = get_sorted_dates(data)
    result = []
    for x in info:
        result_list = {}
        if "from" in x:
            value = x["from"]
            letters = ''.join(x for x in value if x.isalpha())
            numbers = ''.join(x for x in value if x.isdigit())
            numbers_masked = numbers[:4] + " " + numbers[4:6] + "**" + " " + "****" + " " + numbers[-4:]
            result_list[letters] = numbers_masked
            result.append(result_list)
        else:
            result_list["Нет данных об отправителе"] = "---"
            result.append(result_list)
    return result[:operation_counts]

def to_card_number():
    """Выводим номер получателя"""
    info = get_sorted_dates(data)
    result = []
    for x in info:
        result_list = {}
        if "to" in x:
            value = x["to"]
            letters = ''.join(x for x in value if x.isalpha())
            numbers = ''.join(x for x in value if x.isdigit())
            numbers_masked = " " + "**" + numbers[-4:]
            result_list[letters] = numbers_masked
            result.append(result_list)
        else:
            result_list["Нет данных о получателе"] = "---"
            result.append(result_list)
    return result[:operation_counts]

def description():
    """Возвращение назначение платежа"""
    info = get_sorted_dates(data)
    result = []
    for x in info:
        if "description" in x:
            result.append(x["description"])
        else:
            result.append("Назначение не найдено")
    return result[:operation_counts]

def amount():
    """Возвращение суммы платежа"""
    info = get_sorted_dates(data)
    result = []
    for x in info:
        if "operationAmount" in x:
            result.append(x["operationAmount"]["amount"])
        else:
            result.append("Сумма не найдена")
    return result[:operation_counts]

def currency():
    """Возвращение валюты платежа"""
    info = get_sorted_dates(data)
    result = []
    for x in info:
        if "operationAmount" in x:
            result.append(x["operationAmount"]["currency"]["name"])
        else:
            result.append("Валюта не найдена")
    return result[:operation_counts]
print(currency())
def main():
    """Основной код программы"""
    i = 0
    while i < operation_counts:
        formatted_date_str = str(formatted_date()[i]).replace("-", ".")
        dict = from_card_number()[i]
        dict_to = to_card_number()[i]
        for key,value in dict.items():
            card_type = key
            card_number = value
            if "Visa" in key or "Счёт" in key:
                card_type = card_type[0:4] + " " + card_type[4:]
            elif "Maestro" in key:
                card_type = card_type[0:7] + " " + card_type[7:]
            elif "MИР" in key:
                card_type = card_type[0:3]
            elif "MasterCard" in key:
                card_type = card_type[0:10] + " " + card_type[10:]

        for key,value in dict_to.items():
            card_type_to = key
            card_number_to = value
            if "Visa" in key or "Счёт" in key:
                card_type_to = card_type_to[0:4] + " " + card_type_to[4:]
            elif "Maestro" in key:
                card_type_to = card_type_to[0:7] + " " + card_type_to[7:]
            elif "MИР" in key:
                card_type_to = card_type_to[0:3]
            elif "MasterCard" in key:
                card_type_to = card_type_to[0:10] + " " + card_type_to[10:]

        print()
        print(f"{get_id()[i]}\n"
              f"{formatted_date_str} {description()[i]} -> {get_status()[i]}"
                f"\n{card_type} {card_number} -> {card_type_to}{card_number_to}"
                f"\n{amount()[i]} {currency()[i]}")
        i += 1
    return f"\nСпасибо за работу,хорошего дня!"












