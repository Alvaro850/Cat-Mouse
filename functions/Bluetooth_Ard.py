import serial
import time

ser = serial.Serial('COM3', 9600, timeout = 0)
time.sleep(2)
ser.write(b"1\n")  
time.sleep(1)
ser.flush()
data = ser.readlines()
print(data)
print(data)
ser.close