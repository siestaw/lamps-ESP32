from machine import Pin, PWM
from modules.utils.helpers import logger
import time

_red = None
_green = None
_blue = None

def init_leds(pins, freq=1000):
    logger("Initializing LED's...")
    global _red, _green, _blue
    try:
        _red = PWM(Pin(pins["red"]))
        _green = PWM(Pin(pins["green"]))
        _blue = PWM(Pin(pins["blue"]))

        for pin in (_red, _green, _blue):
            pin.freq(freq)
        
    except ValueError as e:
        logger("ERROR: " + str(e))
        led = Pin(pins["internal"], Pin.OUT)
        while True:
            led.value(1)
            time.sleep(1)
            led.value(0)
            time.sleep(1)

def set_color(r, g, b, error=False):
    if error == False:
        logger(str(f"Changing color to {r}, {g}, {b}"))
    def scale(x):
        return int(x * 1023 / 255)
    _red.duty(scale(r))
    _green.duty(scale(g))
    _blue.duty(scale (b))

def error_handler(r, g, b, interval, msg):
    logger(str("ERROR: " + msg))
    while True:
        set_color(r, g, b, error=True)
        time.sleep(interval)
        set_color(0, 0, 0, error=True)
        time.sleep(interval)