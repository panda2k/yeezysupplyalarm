import json
import requests
import googlehomecontroller
import time

def check_product(sku):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'} # required for headless chrome to work on yeezy supply
    url = (f'https://www.yeezysupply.com/api/products/{sku}/')
    response = requests.get(url, headers=headers)
    product = json.loads(response.content)
    print(response.headers['content-type'])
    if 'message' in product.keys():
        return product['message']
    else:
        return product['attribute_list']['badge_text']

def check_product_availbility(sku):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'} # required for headless chrome to work on yeezy supply
    url = (f'https://www.yeezysupply.com/api/products/{sku}/availability')
    response = requests.get(url, headers=headers)
    print(response.headers['content-type'])
    if response.headers['content-type'].find('application/json') != -1:
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
    print(check_product_availbility('H67799'))
    #check_product('H67799')

if __name__ == "__main__":
    main()