import network
import time

class WifiError(Exception):
    pass

def connect_wifi(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)  # Station Interface
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

    print("Connected! IP:", wlan.ifconfig()[0])
    return wlan.ifconfig()