import urllib.request
import time

option = input('Do you want to buy now? (S/N) ')

if option == 'S':
    site = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = site.read() .decode('utf-8')
    w = text.find('>$')
    begin = w + 2
    end = w + 6
    price = float(text[begin:end])
    print(f'Buy! Price {price}')
else:
    price = 7
    while price >= 4.74:
        site = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
        text = site.read() .decode('utf-8')
        w = text.find('>$')
        begin = w + 2
        end = w + 6
        price = float(text[begin:end])
        if price >= 5.74:
            time.sleep(3)
    print(f'Buy! Price {price}')



