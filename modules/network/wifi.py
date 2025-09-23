import network, time
from modules.utils.helpers import logger


class WifiError(Exception):
    pass

def connect_wifi(ssid, password):
    logger("Trying to connect to wifi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    time.sleep(0.2)
    wlan.active(True)
    time.sleep(0.2)

    for attempt in range(5):
        try:
            wlan.connect(ssid, password)
        except OSError as e:
            logger("WLAN connect error")

        start = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 5000:
                logger(f"Attempt {attempt+1} failed, retrying...")
                break
            time.sleep(0.1)
        else:
            return wlan.ifconfig()

        time.sleep(1)

    raise WifiError("Couldn't connect to WiFi after retries")
