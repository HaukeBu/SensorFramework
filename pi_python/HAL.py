import MessageGenerator as msg_gen
import serial
import io


def distance_sensor(id_nr):
    json_list = []
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json_list.append( msg_gen.pack_to_json(1, "distance", id_nr, value))
    return json_list


def acceleration_sensor(id_nr):
    json_list = []
    print("ID:", id_nr)
    # get Values
    value = [1,2]
    # Validation

    # get json
    json_list.append(msg_gen.pack_to_json(1, "acceleration", id_nr, value))
    return json_list


def sound_sensor(id_nr):
    json_list = []
    print("ID:", id_nr)
    # get Values
    value = [1]
    # Validation

    # get json
    json_list.append(msg_gen.pack_to_json(1, "sound", id_nr, value))
    return json_list


def serial_sensors():

    #port = serial.Serial("/dev/cu.wchusbserial620", 9600, timeout=None)
    port = serial.Serial("com3", 9600, timeout=None)

    sio = io.TextIOWrapper(io.BufferedRWPair(port, port))

    print("port is open: ", port.is_open)
    json_list = []

    sio.write("hello\n")
    sio.flush()
    hello = sio.readline()
    print(hello)
    #temperature = 0
    #pressure = 0

    json_list.append(msg_gen.pack_to_json(1, "temperature", 1, 1))
    json_list.append(msg_gen.pack_to_json(1, "pressure", 1, 1))

    return None
