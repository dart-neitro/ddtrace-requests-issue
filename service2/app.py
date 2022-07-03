import time
import os

from ddtrace import patch_all
import httpx
from flask import Flask, jsonify

patch_all()
app = Flask(__name__)

DELAY = int(os.environ.get('REQUEST_DELAY', 0))


@app.route("/endpoint2")
def endpoint2():
    print('sleep')
    time.sleep(DELAY)

    with httpx.Client() as client:
        r = client.get("https://google.com", timeout=60)
        print(r)
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
