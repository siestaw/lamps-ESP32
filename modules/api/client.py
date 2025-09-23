import urequests
from modules.utils import helpers
import json

class ApiError(Exception):
    pass

class DataError(Exception):
    pass

def get_color(url, id, token):
    api = url.rstrip("/")+ "/api/v1/colors/" + str(id)
    headers = {"Authorization": token}

    try:
        resp = urequests.get(api, headers=headers)
        data = resp.json()
        resp.close()

    except Exception as e:
        raise ApiError("Couldn't connect to Laterna API")
    
    if data["success"] == False:
        raise DataError(data["error"])
    
    hex_color = data["data"]["color"]
    r, g, b = helpers.hex_to_rgb(hex_color)
    return r, g, b