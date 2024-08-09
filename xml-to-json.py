import json
import xmltodict

with open("files/anyquery-feed.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

    json_data = json.dumps(data_dict, indent=4)

    with open("files/data.json", "w") as json_file:
        json_file.write(json_data)