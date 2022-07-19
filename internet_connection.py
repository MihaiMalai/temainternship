import requests
import logging

def check_internet():
    url = "https://www.youtube.com/"
    timeout = 5
    logging.info('Checking internet connection')
    try:
        requests.get(url, timeout=timeout)
    except (requests.ConnectionError, requests.Timeout):
        connected = input('No internet access, please try to reconnect. If connected press "y", if failed to '
                          'connect press "n" to quit: ')
        if str.lower(connected) != 'y':
            print('Failed to connect to the internet, process finished')
            quit()
        while str.lower(connected) == 'y':
            try:
                requests.get(url, timeout=timeout)
                break
            except (requests.ConnectionError, requests.Timeout):
                connected = input('No internet access, please try to reconnect. If connected press "y", if failed to '
                                  'connect press "n" to quit: ')
                if connected != 'y':
                    print('Failed to connect to the internet, process finished')
                    quit()
