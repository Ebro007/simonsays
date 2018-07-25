import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
from getpass import getpass

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
buzz = GPIO.PWM(buzz_pin, 1000)

colors = ['R', 'G', 'B', 'Y']
frequencies= [10000, 2000, 1000, 250]

def validate_guess(color_sequence_string, guess):
	if guess == color_sequence_string:
		print"Correct, here is the next color sequence"
	else:
		print "Incorrect guess"
		print "The correct sequence is ", color_sequence_string
		print "Your guess was: ", guess
		LED.destroy()
		exit()

def loop():
	n = random.randint(0,3)
	color_sequence=[colors[n]]
	frequency_sequence=[frequencies[n]]
	while True:
		for i in range(0, len(color_sequence)):
			buzz.ChangeFrequency(frequency_sequence[i])
			buzz.start(50)
			LED.setColor(color_sequence[i])
			time.sleep(0.5)
			buzz.stop()
			LED.noColor()
			time.sleep(0.5)
		guess = getpass("Guess the color sequence:")
		color_sequence_string = ''.join(color_sequence)
		validate_guess(color_sequence_string, guess.upper())
		n = random.randint(0,3)
		color_sequence.append(colors[n])
		frequency_sequence.append(frequencies[n])




if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Bye!'
