import serial

port = serial.Serial("/dev/cu.wchusbserial620", 9600, timeout=None)
# port.open()

while True:

    data = port.readline()
    print(data)