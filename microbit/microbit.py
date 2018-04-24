# Add your Python code here. E.g.
from microbit import *
import radio
import random

random.seed(1234567890123456)
tools = [Image.SKULL, Image.PITCHFORK, Image.PACMAN]
choice = 0
others = 0

radio.on()
radio.config(channel=13)

while True:
    if button_a.was_pressed():
        others = 0
        choice = random.randrange(len(tools))

    display.show(tools[choice])
    radio.send('e %s' % str(choice))
    sleep(500)

    incoming = radio.receive()
    if incoming:
        x = incoming.split()[1]
        if int(x) == choice:
            others += 1
    display.show(str(others))
    sleep(500)
