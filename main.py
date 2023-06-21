import json

json_file = open("src\operations.json", "r", "utf_8")

transactions = json.load(json_file)

print(transactions)
