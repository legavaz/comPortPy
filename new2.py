

import serial
import serial.threaded
import sys

ser = serial.Serial()
ser.port = "com6" #argv[1] if len(argv) > 1 else "/dev/ttyACM0"
ser.timeout = 1

# try to connect
try:
    ser.open()
except serial.SerialException as e:
    print("Error, could not connect to the boards.",e)
    serial = None
    exit(1)


# def Open():
#     global serial
#     if len(argv) > 1 and argv[1] in ("-h", "--help"):
#         print(
#             "Usage: %s [serial device]\n\tDefault device is /dev/ttyACM0\n" % (argv[0]))
#         exit(0)

#     serial = Serial()
#     serial.port = argv[1] if len(argv) > 1 else "/dev/ttyACM0"
#     serial.timeout = CONNECTION_TIMEOUT

#     # try to connect
#     try:
#         serial.open()
#     except SerialException, e:
#         print("Error, could not connect to the boards.")
#         stderr.write("%s\n" % (e))
#         serial = None
#         exit(1)
