from radio_factory import RadioFactory
from time_date_setter_factory import TimeDateSetterFactory
from detect_icom_radio import detect_icom_radio

def main():
    # Detect Icom radio attached
    icom_ports = detect_icom_radio()
    if not icom_ports:
        print("No Icom radio detected.")
        return

    # Set the time and date on each detected Icom radio
    for port in icom_ports:
        # Create radio controller
        radio = RadioFactory.create_radio(port)

        # Create time/date setter
        time_date_setter = TimeDateSetterFactory.create_time_date_setter()

        # Set the time and date
        time_date_setter.set_time_and_date(radio)

        # Close serial connection
        radio.close()

if __name__ == "__main__":
    main()
