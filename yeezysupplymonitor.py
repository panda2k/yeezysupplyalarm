import os
import logging
from datetime import datetime
import json
import requests
import time

log_path = os.path.join(os.getcwd(), "logs/")
if os.path.isdir(log_path) == False:
    os.mkdir(log_path)
logging.basicConfig(
    level=logging.DEBUG, 
    filename=log_path + datetime.now().strftime("%Y:%m:%d:%H:%M:%S").replace(':', '-') + ".txt",
    filemode='w',
    format='%(asctime)s, %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

import googlehomecontroller


class YeezySupplyMonitor:
    def check_product_availbility(self, sku):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'} # required for headless chrome to work on yeezy supply
        url = (f'https://www.yeezysupply.com/api/products/{sku}/availability')
        response = requests.get(url, headers=headers)
        if response.headers['content-type'].find('application/json') == -1: # check to make sure response is JSON
            logging.debug('Product not found')
            return False
        product = json.loads(response.content)
        logging.debug(product)
        if product['availability_status'] != 'PREVIEW': # If product is JSON, check product status
            logging.debug('Product available')
            return True
        else: 
            logging.debug('Product not available')
            return False

    def monitor_site(self, sku, monitor_delay):
        while self.check_product_availbility(sku) == False:
            time.sleep(monitor_delay)
        logging.debug('Triggering alarm')
        wakeup_alarm()

    def wakeup_alarm(self):
        googlehomecontroller.play_music('spotify:track:49fT6owWuknekShh9utsjv')

def main():
    monitor = YeezySupplyMonitor()
    #monitor.monitor_site('x', 5)

if __name__ == "__main__":
    main()