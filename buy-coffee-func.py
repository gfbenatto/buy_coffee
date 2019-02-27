import urllib.request
import time

def get_price():
    site = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = site.read() .decode('utf-8')
    w = text.find('>$')
    begin = w + 2
    end = w + 6
    return float(text[begin:end])

option = input('Do you want to buy now? (S/N) ')
if option == 'S':
    price = get_price()
    print (f'Buy! Price: {price}')
else:
    price = 99.99
    while price >= 3.74:
        price = get_price()
        print(price)
        if price >= 3.74:
            time.sleep(2)
    print(f'Buy! Price:  {price}')