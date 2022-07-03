import os
import time

import requests
import httpx

DELAY = int(os.environ.get('REQUEST_DELAY', 0))
SERVICE_NAME = os.environ.get("SERVICE_NAME", "noname-service")


TARGET_ENDPOINT_URL1 = os.environ.get('target_endpoint1')
if not TARGET_ENDPOINT_URL1:
    raise Exception('target_endpoint1 has not been found')
if not TARGET_ENDPOINT_URL1:
    raise Exception('target_endpoint1 has not been found')


TARGET_ENDPOINT_URL2 = os.environ.get('target_endpoint2')
if not TARGET_ENDPOINT_URL2:
    raise Exception('target_endpoint2 has not been found')
if not TARGET_ENDPOINT_URL2:
    raise Exception('target_endpoint2 has not been found')


# init data
DELAY = int(os.environ.get('REQUEST_DELAY', 0))


def send_request_via_requests():
    print('sleep')
    time.sleep(DELAY)
    r = requests.get(TARGET_ENDPOINT_URL1)
    print(r)


def send_request_via_httpx():
    print('sleep')
    time.sleep(DELAY)

    with httpx.Client() as client:
        r = client.get(TARGET_ENDPOINT_URL2, timeout=60)
    print(r)

def main():
    print('start')
    send_request_via_requests()
    send_request_via_httpx()
    print('end')

if __name__ == "__main__":
    main()