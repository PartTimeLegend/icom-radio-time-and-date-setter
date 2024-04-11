import serial
import time


class RadioController:


    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate=self.baudrate, timeout=1)

    def send_command(self, command):
        self.ser.write(command.encode() + b'\n')
        time.sleep(0.1)  # Wait for the radio to process the command

    def close(self):
        self.ser.close()
