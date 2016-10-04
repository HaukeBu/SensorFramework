import MessageGenerator as msg_gen


def distance_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "distance", id_nr, value)
    return json


def pressure_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1, 2]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "pressure", id_nr, value)
    return json


def temperature_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "temperature", id_nr, value)
    return json


def acceleration_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "acceleration", id_nr, value)
    return json


def sound_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "sound", id_nr, value)
    return json
