import base64
from pathlib import Path

import requests

import flash

with (Path("./assets") / "ant.jpg").open("rb") as f:
    print(f)
    imgstr = base64.b64encode(f.read()).decode("UTF-8")

body = {"session": "UUID", "payload": {"inputs": {"data": imgstr}}}
resp = requests.post("http://127.0.0.1:8000/predict", json=body)
print(resp.json())