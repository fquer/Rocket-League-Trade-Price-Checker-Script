from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
from collections import Counter
import atexit
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('cls')

def exit_handler():
    subprocess.call('taskkill /f /im firefox.exe')
    subprocess.call('taskkill /f /im geckodriver.exe')
    
atexit.register(exit_handler)

multiple_offers_in_trade = False   #Keep false for better price analysis
delay_click = 0.1
print("Loading Driver...")
firefox_options = FirefoxOptions()
firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options, executable_path='geckodriver.exe')
driver.set_window_size(2320, 1080)
driver.get("https://rocket-league.com/trading")
driver.find_element_by_id("acceptPrivacyPolicy").click()

founded = False

while True:

    sell_array = []
    buy_array = []
    sell_times = []
    buy_times = []
    os.system('cls')
    item = input("Item Name : ")
    item = item.capitalize()

    paint = input("Paint (If its colorless leave it empty) : ")
    paint = paint.capitalize()
    if paint == '':
        paint = 'None'
    print("\nLoading...")
    first = True

    for say in range(0,2):
        
        driver.execute_script("window.scrollTo(0, 500)") 

        # Item Arama Baslangici
        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[1]/div").click() # Arana tab'ini acma
        sleep(delay_click)

        item_input = driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[1]/div/div/div/input") # input field bul
        item_input.send_keys(item) # item'i yaz
        sleep(delay_click)

        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[1]/div/div/ul/li[2]").click() # cikan ilk sonuca bas
        sleep(delay_click)
        # Item Arama Sonu



        # Renk Secme Baslangici
        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[3]/div").click() # Arana tab'ini acma
        sleep(delay_click)

        item_paint_input = driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[3]/div/div/div/input") # input field bul
        item_paint_input.send_keys(paint) # item'i yaz
        sleep(delay_click)

        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[3]/div/div/ul/li").click() # cikan ilk sonuca bas
        sleep(delay_click)
        # Renk Secme Sonu


        # Wants Have Secme Baslangici
        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[8]/div").click() # Secme tab'ini acma
        sleep(delay_click)

        if first:
            driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[8]/div/div/ul/li[2]").click() # Wants Bas
        else:
            driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[8]/div/div/ul/li[3]").click() # Have Bas

        sleep(delay_click)
        # Wants Have Secme Sonu

        # Platform Secme Baslangici
        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[7]/div").click() # Platform Secme tab'ini acma
        sleep(delay_click)
        driver.find_element_by_xpath("/html/body/main/div/div/div[1]/div[2]/div/div/form/div[7]/div/div/ul/li[2]").click() # Pc secme
        # Platform Secme Sonu

        driver.find_element_by_css_selector("input.rlg-btn-primary.rlg-itemfilter__apply").click() # apply filter bas

        source = BeautifulSoup(driver.page_source,"lxml")
        
        for has, wants, time in zip(source.find_all('div', {'class': 'rlg-trade__itemshas'}),source.find_all('div', {'class': 'rlg-trade__itemswants'}),source.find_all('span', {'class': 'rlg-trade__time'})):
            
            for has_item_block, wants_item_block in zip(has.find_all('div', {'class': 'rlg-item'}),wants.find_all('div', {'class': 'rlg-item'})):

                for has_founded_item, wants_founded_item in zip(has_item_block.find_all('h2', {'class': 'rlg-item__name'}),wants_item_block.find_all('h2', {'class': 'rlg-item__name'})):

                    has_founded_paint = has_item_block.find('div', {'class': 'rlg-item__paint'})
                    has_founded_quantity = has_item_block.find('div', {'class': 'rlg-item__quantity'})

                    if has_founded_item.text.strip() == "Credits":
                        if has_founded_quantity != None:
                            has_searched = has_founded_quantity.text.strip()+' '+has_founded_item.text.strip()  
                    
                    elif has_founded_paint != None:
                        if has_founded_quantity != None:
                            has_searched = has_founded_quantity.text.strip()+' '+has_founded_paint.text.strip()+' '+has_founded_item.text.strip()
                        else:
                            has_searched = has_founded_paint.text.strip()+' '+has_founded_item.text.strip()
                    else:
                        if has_founded_quantity != None:
                            has_searched = has_founded_quantity.text.strip()+' '+has_founded_item.text.strip()
                        else:
                            has_searched = has_founded_item.text.strip()


                    wants_founded_paint = wants_item_block.find('div', {'class': 'rlg-item__paint'})
                    wants_founded_quantity = wants_item_block.find('div', {'class': 'rlg-item__quantity'})

                    if wants_founded_item.text.strip() == "Credits":
                        if wants_founded_quantity != None:
                            wants_searched = wants_founded_quantity.text.strip()+' '+wants_founded_item.text.strip()
                    
                    elif wants_founded_paint != None:
                        if wants_founded_quantity != None:
                            wants_searched = wants_founded_quantity.text.strip()+' '+wants_founded_paint.text.strip()+' '+wants_founded_item.text.strip()
                        else:
                            wants_searched = wants_founded_paint.text.strip()+' '+wants_founded_item.text.strip()
                    else:
                        if wants_founded_quantity != None:
                            wants_searched = wants_founded_quantity.text.strip()+' '+wants_founded_item.text.strip()
                        else:
                            wants_searched = wants_founded_item.text.strip()

                    if first:
                        
                        if paint != 'None':
                            if has_searched.lower() == paint.lower() + ' ' + item.lower():
                                sell_array.append(has_searched+"  :  "+wants_searched)
                                founded = True
                                sell_times.append(time.text)
                                break
                        else:
                            if has_searched.lower() == item.lower():
                                sell_array.append(has_searched+"  :  "+wants_searched)
                                founded = True
                                sell_times.append(time.text)
                                break
                        
                    else:
                        
                        if paint != 'None':
                            if wants_searched.lower() == paint.lower() + ' ' + item.lower():
                                buy_array.append(wants_searched+"  :  "+has_searched)
                                founded = True
                                buy_times.append(time.text)
                                break
                        else:
                            if wants_searched.lower() == item.lower():
                                buy_array.append(wants_searched+"  :  "+has_searched)
                                founded = True
                                buy_times.append(time.text)
                                break

                if founded == True and multiple_offers_in_trade == False:
                    founded = False
                    break

                

                        

        first = False

    os.system('cls')

    print("SELL ORDER")
    for i, j in zip(sell_array, sell_times):
        print(i + " || " + j.split('\n')[1])


    sell_count = []
    print("\nCOUNTS")

    for i in sell_array:
        if i.find("Credits") != -1:
            if i.find("Credits offer") == -1:
                sell_count.append(i)

    for key, value in dict(sorted(Counter(sell_count).items(), key=lambda item: item[1])).items():
        print(str(key + ' =   x' + str(value)))


    print("\n\nBUY ORDER")
    for i, j in zip(buy_array, buy_times):
        print(i + " || " + j.split('\n')[1])


    buy_count = []
    print("\nCOUNTS")

    for i in buy_array:
        if i.find("Credits") != -1:
            if i.find("Credits offer") == -1:
                buy_count.append(i)

    for key, value in dict(sorted(Counter(buy_count).items(), key=lambda item: item[1])).items():
        print(str(key + ' =   x' + str(value)))

    print("")
    input("Press Enter to Continue...")