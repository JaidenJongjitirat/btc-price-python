import requests, json
import time
import sys

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ts = raw_input("\033[1;32mTicker speed (\033[0m""\33[93min seconds\033[0m""\033[1;32m)> \033[0m")
def BitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        api_request = requests.get(URL)
        price = float(json.loads(api_request.text)['last'])
        return price

    except requests.ConnectionError:
        print "\033[91mError querying Bitcoin price!!\033[0m"
        sys.exit()   

while True:
    time.sleep(int(ts))	
    print "\033[1;32mThe current price of \033[0m" "\33[93mBitcoin \033[0m" "\033[1;32mis: \033[0m" "$" + str(BitcoinPrice()) + "\033[1;32m USD\033[0m"   

BitcoinPrice()
