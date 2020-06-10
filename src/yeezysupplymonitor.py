import json
import requests
import googlehomecontroller
import time

def check_product_availbility(sku):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'} # required for headless chrome to work on yeezy supply
    url = (f'https://www.yeezysupply.com/api/products/{sku}/availability')
    response = requests.get(url, headers=headers)
    if response.headers['content-type'].find('application/json') == -1: # check to make sure response is JSON
        return False
    product = json.loads(response.content)
    if product['availability_status'] != 'PREVIEW': # If product is JSON, check product status
        return True
    else: 
        return False

def monitor_site(sku, monitor_delay):
    while check_product_availbility(sku) == False:
        time.sleep(monitor_delay)
    wakeup_alarm()

def wakeup_alarm():
    googlehomecontroller.play_music('spotify:track:49fT6owWuknekShh9utsjv')

def main():
    print(check_product_availbility('FY5158'))

if __name__ == "__main__":
    main()