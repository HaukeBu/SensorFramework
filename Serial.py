import serial
import io
import time

port = serial.Serial("/dev/cu.wchusbserial620", 9600, timeout=None)
sio = io.TextIOWrapper(io.BufferedRWPair(port, port))
# port.open()

request = "start\n"

while True:

    sio.write(request)

    temperature = sio.readline(1)
    pressure = sio.readline(16)



    print(temperature)
    print(pressure)

    time.sleep(1)