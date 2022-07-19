import requests
import logging
import time

def check_internet():
    url = "https://www.youtube.com/"
    timeout = 5
    logging.info('Checking internet connection')
    try:
        requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout):
        logging.exception('Exception occurred, no internet access. Waiting 15 seconds for connection to reestablish')
        time.sleep(20)
        try:
            requests.get(url, timeout=timeout)
        except (requests.ConnectionError, requests.Timeout):
            logging.exception('Failed to connect to the internet, process finished')
            quit()
