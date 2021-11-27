from time import sleep
import requests
from bs4 import BeautifulSoup
import os

os.system('cls')
item = input("Item Name : ")
item = item.lower()
item = item.replace('(','[')
item = item.replace(')',']')
blackmarket = input("This item is Blackmarket ? (Yes = 1 | No = 0) : ")

if blackmarket == "1":
    item = item + ' [black market]'
elif blackmarket != "0":
    print("Invalid Blackmarket Input !")
    sleep(3)
    exit()

paint = input("Paint (If its colorless leave it empty) : ")
paint = paint.lower()
if len(paint) != 0:
    item = paint.strip() +' '+ item

os.system('cls')

url_h = 'https://www.rl-trades.com//ajax/&h0="{}"&s[]=rl&'.format(item)
url_w = 'https://www.rl-trades.com//ajax/&w0="{}"&s[]=rl&'.format(item)

r_h = requests.get(url_h)
source_h = BeautifulSoup(r_h.content,"lxml")
r_w = requests.get(url_w)
source_w = BeautifulSoup(r_w.content,"lxml")

while True:

    control = False
    print("\tSEARCHING ITEM : ",item,"\n\n")
    print("\t  SELL ORDER\n")

    for td in source_h.find_all('td'):
        if td.text != "":
            if td.text == item and control == False:
                control = True
            
            elif control != False:
                if td.text.find('credits') != -1:
                    try:
                        print(item," : ",int(td.text.split('xcredits')[0]))
                    except:
                        print(item," :  [OFFER] ",td.text)
                    control = False
    
    

    control = False
    print("\n\n\t   BUY ORDER\n")

    for td in source_w.find_all('td'):
        if td.text != "":
            if td.text.find('credits') != -1 and control == False:
                try:
                    cr = int(td.text.split('xcredits')[0])
                except:
                    cr = '[OFFER] ' + td.text
                control = True

            elif control != False:

                if td.text == item:
                    print(item," : ",cr)

                control = False

    r_h = requests.get(url_h)
    source_h = BeautifulSoup(r_h.content,"lxml")
    r_w = requests.get(url_w)
    source_w = BeautifulSoup(r_w.content,"lxml")
    sleep(5) 
    os.system('cls')