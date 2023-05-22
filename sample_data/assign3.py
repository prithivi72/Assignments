import json
with open("sample_data.json") as file:

    data = json.load(file)
    new_list = []
    parameters = data["parametersList"]
    for each_parameter in parameters:
        new_dict = {
            "parameterName": each_parameter["parameterName"],
            "min_value": each_parameter["min"],
            "max_value": each_parameter["max"],
            "avg_value": each_parameter["avg"]
        }
        new_list.append(new_dict)

json_list = json.dumps(new_list)
print(json_list)
with open("../final.json", "w") as file1:
    file1.write(json_list)