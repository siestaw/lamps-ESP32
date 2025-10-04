import network, time
from modules.utils.helpers import logger

class WifiError(Exception):
    pass

def connect_wifi(ssid, password):
    logger("Trying to connect to WiFi...")

    wlan = network.WLAN(network.STA_IF)
    if not wlan.active():
        wlan.active(True)
    time.sleep(1)

    try:
        wlan.config(reconnects=5)
    except Exception:
        pass

    if wlan.isconnected():
        logger(f"Already connected: {wlan.ifconfig()}")
        return wlan.ifconfig()

    logger(f"Connecting to SSID: {ssid}")
    wlan.connect(ssid, password)

    for attempt in range(10):
        start = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 5000:
                logger(f"Attempt {attempt+1} failed, status={wlan.status()} -> retrying...")
                wlan.disconnect()
                time.sleep(1)
                wlan.connect(ssid, password)
                break
            time.sleep(0.1)
        else:
            logger(f"Connected after {attempt+1} attempt(s): {wlan.ifconfig()}")
            return wlan.ifconfig()

    raise WifiError("Couldn't connect to WiFi after multiple retries")