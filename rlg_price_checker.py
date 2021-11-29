import requests
from bs4 import BeautifulSoup
import os

while True:
    os.system('cls')
    item = input("Item Name : ")
    item = item.lower()
    item = item.replace('(','[')
    item = item.replace(')',']')

    paint = input("Paint (If its colorless leave it empty) : ")
    paint = paint.lower()
    if len(paint) != 0:
        item = paint.strip() +' '+ item



    url_h = 'https://www.rl-trades.com//ajax/&h0="{}"&s[]=rl&'.format(item)
    url_w = 'https://www.rl-trades.com//ajax/&w0="{}"&s[]=rl&'.format(item)

    r_h = requests.get(url_h)
    source_h = BeautifulSoup(r_h.content,"lxml")
    r_w = requests.get(url_w)
    source_w = BeautifulSoup(r_w.content,"lxml")

    finded = []
    wrong = False
    for j in range(0,2):
        os.system('cls')
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
                            finded.append(td.text.split('xcredits')[0])
                        except:
                            print(item," :  [OFFER] ",td.text.strip())
                            finded.append(td.text.strip())
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
                        finded.append(cr)
                    control = False
        
        for i  in finded:
            if i != "":
                wrong = True

        if wrong == False:
            item = item + ' [black market]'

    input("\nPress enter to search another item...")