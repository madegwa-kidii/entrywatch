import requests
import time


def sender():
    try: 

        url = "https://......"

        payload = {
            "username": "madegwa",
            "timestamp": time.localtime(),
        }

        res = requests.post(url,payload)
    except requests.exceptions.HTTPError as myerror:
        print("HTTP: ",myerror)