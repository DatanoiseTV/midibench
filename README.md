# MIDI Benchmarking Tool

This is a cross-platform console application that uses `rtmidi` to list MIDI Control Change (CC) messages it receives and shows how many messages per second are received for each CC number and each connected MIDI device. It helps benchmark MIDI devices in real-time.

## Features

- Lists all connected MIDI input devices.
- Monitors and counts MIDI CC messages for each device and each CC number.
- Displays the number of messages per second in a console table view.

## Requirements

- Python 3.6 or higher
- `python-rtmidi` library
- `prettytable` library

## Installation

1. Clone the repository or download the script.

2. Install the required dependencies using `pip`:

```
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```
python midibench.py
```

The script will:

1. List all available MIDI input ports.
2. Monitor and count incoming MIDI CC messages for each device and each CC number.
3. Display a live updating table in the console, showing the number of CC messages per second.

## Example Output

```
Available MIDI input ports:
0: MIDI Device 1
1: MIDI Device 2

+----------------+-----------+-----------------------+
|     Device     | CC Number | Messages per Second   |
+----------------+-----------+-----------------------+
| MIDI Device 1  |    10     |          5            |
| MIDI Device 1  |    74     |          3            |
| MIDI Device 2  |    21     |          7            |
+----------------+-----------+-----------------------+
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- `rtmidi` library for MIDI input handling.
- `prettytable` library for displaying the console table.

## Notes

- Make sure your MIDI devices are properly connected and recognized by the system before running the script.
- The script clears the console every second to update the table view.

Feel free to modify and enhance this script according to your needs.