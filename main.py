from modules.network import wifi
from modules.api import client
from modules.led import controller
import time, ujson

print("Starting up!")
time.sleep(2) # wait for Wifi-Interface to start

with open("config.json", "r") as read_config:
    config = ujson.load(read_config)
    
url = str(config["api"]["url"])
controller_id = int(config["api"]["id"])
token = str(config["api"]["token"])
poll_interval = int(config["api"]["poll_interval"])

controller.init_leds(config["led"])

try: 
    wifi.connect_wifi(config["wifi"]["SSID"], config["wifi"]["password"])
except wifi.WifiError as e:
    controller.error_handler(255, 0, 0, 1, str(e))

try: 
    r, g, b = client.get_color(url, controller_id, token)
    controller.set_color(r, g, b)
    current_color = (r, g, b)
except client.ApiError as e:
    controller.error_handler(255, 255, 0, 1, str(e))
except client.DataError as e:
    controller.error_handler(0, 0, 255, 1, str(e))

while True:
    try:
        r, g, b = client.get_color(url, controller_id, token)
        controller.set_color(r, g, b)
    except client.ApiError as e:
        controller.error_handler(255, 0, 255, 1, str(e))
    except client.DataError as e:
        controller.error_handler(0, 0, 255, 1, str(e))

    time.sleep(poll_interval)