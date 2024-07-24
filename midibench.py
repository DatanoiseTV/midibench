import rtmidi
import time
from collections import defaultdict
from prettytable import PrettyTable

# Dictionaries to store message counts per device and CC number
message_counts = defaultdict(lambda: defaultdict(int))
cc_seen = defaultdict(set)  # Track seen CC numbers per device
start_time = time.time()

def midi_input_callback(message, data):
    message, deltatime = message
    device_name = data['name']
    if message[0] & 0xF0 == 0xB0:  # Control Change message (0xB0)
        cc_number = message[1]
        message_counts[device_name][cc_number] += 1
        cc_seen[device_name].add(cc_number)

def monitor_midi_devices():
    global start_time  # Declare start_time as global
    midi_in = rtmidi.MidiIn()
    available_ports = midi_in.get_ports()

    if not available_ports:
        print("No MIDI input ports available.")
        return

    print("Available MIDI input ports:")
    for i, port_name in enumerate(available_ports):
        print(f"{i}: {port_name}")
    
    for i, port in enumerate(available_ports):
        midi_in.open_port(i)
        midi_in.set_callback(midi_input_callback, {'name': port})

    try:
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 1.0:
                table = PrettyTable()
                table.field_names = ["Device", "CC Number", "Messages per Second"]
                for device, cc_counts in message_counts.items():
                    for cc in cc_seen[device]:
                        count = cc_counts[cc]
                        table.add_row([device, cc, count])
                print("\033c", end="")  # Clear the console
                print(table)
                # Reset counts but keep CCs
                for device in message_counts:
                    for cc in message_counts[device]:
                        message_counts[device][cc] = 0
                start_time = current_time
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting...")
        for i in range(len(available_ports)):
            midi_in.close_port()

if __name__ == "__main__":
    monitor_midi_devices()
