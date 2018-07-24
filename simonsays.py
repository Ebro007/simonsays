import time
import random
import RPi.GPIO as GPIO
import LEDRGB as LED

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
buzz = GPIO.PWM(buzz_pin, 1000)


frequencies= [250, 500, 750, 1500]


def loop():
	while True:
		n = random.randint(0,3)
		LED.setColor(colors[n])
		buzz.ChangeFrequency(frequencies[n])
		buzz.start(50)
		time.sleep(0.5)
		buzz.stop
		time.sleep(0.5)
		LED.noColor()
		time.sleep(0.5)

if __name__=='__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Bye!'
		LED.destroy()

