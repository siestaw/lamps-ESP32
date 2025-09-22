from machine import Pin, PWM
import time

_red = None
_green = None
_blue = None

def init_leds(pins, freq=1000):
    global _red, _green, _blue
    _red = PWM(Pin(pins["red"]))
    _green = PWM(Pin(pins["green"]))
    _blue = PWM(Pin(pins["blue"]))

    for pin in (_red, _green, _blue):
        pin.freq(freq)

def set_color(r, g, b):
    def scale(x):
        return int(x * 1023 / 255)

    _red.duty(scale(r))
    _green.duty(scale(g))
    _blue.duty(scale (b))

def error_handler(r, g, b, interval, msg):
    print("ERROR: " + msg)
    while True:
        set_color(r, g, b)
        time.sleep(interval)
        set_color(0, 0, 0)
        time.sleep(interval)