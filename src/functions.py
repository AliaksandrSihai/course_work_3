import json
from datetime import datetime

with open("/home/aliaksandr_sigai/course_work_3/operations.json", "r") as file:
    data = json.load(file)


def get_sorted_dates(data):
    formatted_dates = []
    result = []
    for operation in data:
        if "date" in operation and operation.get("state") == "EXECUTED":
            formatted_dates.append(operation)
    sorted_dates = sorted(formatted_dates, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    for item in sorted_dates[:5]:
        result.append(list(item.items()))

    return result







