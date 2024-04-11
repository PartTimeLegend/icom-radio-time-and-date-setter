from radio_controller import RadioController

class RadioFactory:
    @staticmethod
    def create_radio(port, baudrate=9600):
        return RadioController(port, baudrate)
