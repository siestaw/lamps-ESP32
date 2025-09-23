import time
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def logger(msg):
    ms = time.ticks_ms()
    print("[{} ms] {}".format(ms, msg))