import json


def pack_to_json(version, sensor_type, id_nr, value):
    json_msg = json.dumps({"version": version, "sensortype": sensor_type, "values": [{"id": id_nr, "value": value}]})
    return json_msg
