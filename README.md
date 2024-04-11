Sure, here's a `README.md` file for the provided code:

```markdown
# Icom Radio Time and Date Setter

This Python script sets the time and date on Icom radios connected to the computer.

## Prerequisites

- Python 3.x
- pySerial library

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/parttimelegend/icom-radio-time-and-date-setter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd icom-radio-time-and-date-setter
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python main.py
   ```

   The script will detect any connected Icom radios and set the time and date on each one.

## File Structure

- `main.py`: The main script that detects Icom radios and sets the time and date.
- `radio_controller.py`: Defines the `RadioController` class responsible for communicating with the radio over the serial port.
- `time_date_setter.py`: Defines the `TimeDateSetter` class responsible for setting the time and date on the radio.
- `radio_factory.py`: Defines the `RadioFactory` class responsible for creating instances of the `RadioController`.
- `time_date_setter_factory.py`: Defines the `TimeDateSetterFactory` class responsible for creating instances of the `TimeDateSetter`.
- `detect_icom_radio.py`: Defines the `detect_icom_radio` function to detect connected Icom radios using the `pyserial` library.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to adjust the content based on your project's specifics and requirements.