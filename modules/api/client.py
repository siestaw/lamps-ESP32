import urequests
from modules.utils import helpers
import json

def get_color(url, id, token):
    api = url.rstrip("/")+ "/api/v1/colors/" + str(id)
    print(api)
    headers = {"Authorization": token}

    resp = urequests.get(api, headers=headers)
    data = resp.json()
    resp.close()

    hex_color = data["data"]["color"]
    r, g, b = helpers.hex_to_rgb(hex_color)
    return r, g, b
    
def post_controllers(url, token):
    api = url.rstrip("/") + "/api/v1/controllers"
    headers = {"Authorization": token}

    resp = urequests.post(api, headers=headers)
    data = resp.json()
    resp.close()

    return data["data"]["created"]
