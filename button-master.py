import RPi.GPIO as GPIO
import uinput
import time

# GPIO -> Key mapping
BUTTONS = {
    5: uinput.KEY_W,   # Up
    6: uinput.KEY_A,   # A
    12: uinput.KEY_S,  # S
    13: uinput.KEY_D,  # D
    19: uinput.KEY_Z,  # Z
    16: uinput.KEY_X,  # X
    26: uinput.KEY_C,  # C
    20: uinput.KEY_V   # V
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTONS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup virtual keyboard device
device = uinput.Device(list(BUTTONS.values()))

print("GPIO button → keyboard mapper running... Press Ctrl+C to quit.")

try:
    while True:
        for pin, key in BUTTONS.items():
            if GPIO.input(pin) == GPIO.LOW:  # Button pressed
                device.emit_click(key)
                print(f"Sent {key}")
                time.sleep(0.2)  # debounce
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting...")
