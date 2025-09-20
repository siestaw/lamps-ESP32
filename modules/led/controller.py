from machine import Pin, PWM

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
    _red.duty(r)
    _green.duty(g)
    _blue.duty(b)