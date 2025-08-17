import RPi.GPIO as GPIO
from pynput.keyboard import Controller, Key
import time

# Setup
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 5
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

keyboard = Controller()

print("Press the button on GPIO5 to send 'W'")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed
            keyboard.press('w')
            keyboard.release('w')
            print("Sent W")
            time.sleep(0.2)  # debounce delay
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting...")
