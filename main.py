#!/usr/bin/python

## Requires pika for queue connection

import queue as QueuePackage
import Communicators as communicators
import Threads as own_threads
import HAL


json_queue = QueuePackage.Queue()
json_queue.put("Start!");

# Get the communicator and Setup the connection
# communicator = communicators.CommunicatorDummy()
communicator = communicators.SocketCommunicator("141.22.80.72", 15000)
communicator.setup_connection()

# create threads
pressure_sensor_thread = own_threads.SensorEvaluator(1, "SensorEvaluator_pressure", 1, json_queue, HAL.pressure_sensor)
temperature_sensor_thread = own_threads.SensorEvaluator(2, "SensorEvaluator_temperature", 2, json_queue, HAL.temperature_sensor)
communicator_thread = own_threads.MQ_Communicator(10, "MQ_Communicator", 10, json_queue, communicator)

# start the communicator thread
pressure_sensor_thread.start()
temperature_sensor_thread.start()
communicator_thread.start()




# join all threads
pressure_sensor_thread.join()
temperature_sensor_thread.join()
communicator_thread.join()









