import serial.tools.list_ports

def detect_icom_radio():


    icom_ports = [port for port, desc, hwid in serial.tools.list_ports.comports() if "ICOM" in desc.upper()]
    return icom_ports
