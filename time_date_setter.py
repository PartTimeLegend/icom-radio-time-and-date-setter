import datetime


class TimeDateSetter:
    @staticmethod

    
    def set_time_and_date(radio_controller):
        now = datetime.datetime.now()
        time_str = now.strftime("%H%M%S")
        date_str = now.strftime("%d%m%y")
        radio_controller.send_command(f"TM{time_str}")  # Set the time
        radio_controller.send_command(f"DA{date_str}")  # Set the date
