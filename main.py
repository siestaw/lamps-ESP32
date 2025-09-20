from modules.network import wifi
from modules.api import client
from modules.led import controller
import time, ujson

with open("config.json", "r") as read_config:
    config = ujson.load(read_config)

wifi.connect_wifi(config["wifi"]["SSID"], config["wifi"]["password"])

url = config["api"]["url"]
controller_id = config["api"]["id"]
token = config["api"]["token"]
poll_interval = config["api"]["poll_interval"]

controller.init_leds(config["led"])

r, g, b = client.get_color(url, controller_id, token)
controller.set_color(r, g, b)
current_color = (r, g, b)
print(current_color)

while True:
    r, g, b = client.get_color(url, controller_id, token)
    new_color = (r, g, b)

    if new_color != current_color:
        print("new color:", new_color)
        current_color = r, g, b
        controller.set_color(r, g, b)

    time.sleep(poll_interval)