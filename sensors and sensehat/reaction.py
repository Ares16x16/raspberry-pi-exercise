import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


left_player = input('Please enter the left player name:')
right_player = input('Please enter the right player name:')
led = 4
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0)
time.sleep(random.uniform(1,5))
GPIO.output(led, 1)

left_button = 14
right_button = 15

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        if ( GPIO.input(left_button) ) == False:
            print(left_player + ' wins!')
            break
        if ( GPIO.input(right_button) ) == False:
            print(right_player + ' wins!')
            break
except KeyboardInterrupt:
        print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
