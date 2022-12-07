import requests, json
import time
import sys
import math

#Fancy colors
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
class start(object):
    #USD Bitcoin price
    def BitcoinPrice(self):
        URL = 'https://www.bitstamp.net/api/ticker/'
        try:
            api_request = requests.get(URL)
            price = float(json.loads(api_request.text)['last'])
            #logical and mathmatical concept 1
            if price < 5000.00:
                print("\33[94mNow is a good time to invest in Bitcoin\033[0m")
            return price

        except requests.ConnectionError:
            print("\033[91mPlease check internet connection!!\033[0m")
            sys.exit()      
    #Euro Bitcoin price
    def EuroBitcoinPrice(self):
        URLEuro = 'https://www.bitstamp.net/api/v2/ticker/btceur/'
        try:   
            api_requestEuro = requests.get(URLEuro)
            priceEuro = float(json.loads(api_requestEuro.text)['last'])
            #logical and mathmatical concept 2
            if priceEuro < 2657:
                print("\33[94mNow is a good time to invest in Bitcoin\033[0m")
            return priceEuro

        except requests.ConnectionError:
            print("\033[91mPlease check internet connection!!\033[0m")
            sys.exit()    

    print ("""
    Currencies to compare Bitcoin price to:
    *U.S. Dollar (USD)
    *Euros (Euro)
    *More info
    """)
    #Run main part of program
    def __init__(self):
        #Checks if user typed in USD, Euro
        #Abstration with lists
        usd_keywords = ["USD", "usd", "Usd", "us dollar", "US dollar", "U.S. dollar", "U.S. Dollar", "US DOLLAR", "U.S. DOLLAR"]
        euro_keywords = ["Euro", "euro", "EURO", "Euros", "euros", "EUROS"]


        self.currencyCompare = input(">")
        if self.currencyCompare in usd_keywords:
            while True:
                time.sleep(5)	
                print("\033[1;32mThe current price of 1 \033[0m" "\33[93mBitcoin \033[0m" "\033[1;32mis: \033[0m" "$" + str(self.BitcoinPrice()) + "\033[1;32m USD\033[0m")

        elif self.currencyCompare in euro_keywords:
            while True:
                time.sleep(5)
                print("\033[1;32mThe current price of 1 \033[0m" "\33[93mBitcoin \033[0m" "\033[1;32mis: \033[0m" "€" + str(self.EuroBitcoinPrice()) + "\033[1;32m Euros\033[0m")
                
        else:
          print("Not an option, please choose an option from above menu. Options are: USD and Euro")
          start()
a = start()
