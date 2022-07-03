import time
import os

from ddtrace import patch_all
import requests
from flask import Flask, jsonify

patch_all()
app = Flask(__name__)

DELAY = int(os.environ.get('REQUEST_DELAY', 0))


@app.route("/endpoint1")
def endpoint1():
    print('sleep')
    time.sleep(DELAY)
    r = requests.get("https://google.com")
    return "ok"


@app.route("/healthcheck")
def healthcheck():
    return jsonify({
        "service": os.environ.get("DD_SERVICE"),
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
    )
