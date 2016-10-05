import MessageGenerator as msg_gen
import serial
import io


def distance_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json = msg_gen.pack_to_json(1, "distance", id_nr, value)
    return json


def acceleration_sensor(id_nr):
    print("ID:", id_nr)
    # get Values
    value = [1,2]
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


def serial_sensors():

    port = serial.Serial("/dev/cu.wchusbserial620", 9600, timeout=None)
    sio = io.TextIOWrapper(io.BufferedRWPair(port, port))

    json_list = []
    request = "start\n"

    sio.write(request)

    temperature = sio.readline(1)
    pressure = sio.readline(16)

    json_list.append(msg_gen.pack_to_json(1, "temperature", 1, temperature))
    json_list.append(msg_gen.pack_to_json(1, "pressure", 1, pressure))

    return json_list
