import serial
import time

# change 'COM3' to your Arduino port
# On Linux/Mac it might be '/dev/ttyUSB0' or '/dev/ttyACM0'
arduino = serial.Serial('COM4', 9600, timeout=1)
time.sleep(2)  # wait for Arduino to reset

while True:
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        try:
            temp, humidity = line.split(",")
            print(f"Temperature: {temp} °C | Humidity: {humidity} %")
        except:
            print("Bad data:", line)
