import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(15, RPi.GPIO.IN)
RPi.GPIO.setup(14, RPi.GPIO.OUT)

while True:
    RPi.GPIO.output(14, RPi.GPIO.input(15))

