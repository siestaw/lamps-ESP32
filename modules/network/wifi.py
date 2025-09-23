import network
import time
from modules.utils.helpers import logger

class WifiError(Exception):
    pass

def connect_wifi(ssid, password, timeout=10):
    logger("Connecting to Wifi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        try:
            wlan.connect(str(ssid), str(password))
        except OSError as e:
            raise WifiError(f"Wifi connect failed: {e}") from e

        start = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                raise WifiError("Couldn't connect to WiFi")
            time.sleep(0.1)