from bs4 import BeautifulSoup
import os
from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
from collections import Counter
import atexit
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('cls')

def exit_handler():
    #subprocess.call('taskkill /f /im msedgedriver.exe')
    #subprocess.call('taskkill /f /im msedge.exe')
    pass
    
atexit.register(exit_handler)

OFFERS_LOCATION = 'C:\\Trade\\' # Ends with double backslash

def readData():
    # OFFER READING
    h_items = open(OFFERS_LOCATION + 'has_items.txt')
    w_items = open(OFFERS_LOCATION + 'wants_items.txt')
    h_colours = open(OFFERS_LOCATION + 'has_colours.txt')
    w_colours = open(OFFERS_LOCATION + 'wants_colours.txt')
    h_certification = open(OFFERS_LOCATION + 'has_certifications.txt')
    w_certification = open(OFFERS_LOCATION + 'wants_certifications.txt')

    h_items_2 = open(OFFERS_LOCATION + 'has_items_2.txt')
    w_items_2 = open(OFFERS_LOCATION + 'wants_items_2.txt')
    h_colours_2 = open(OFFERS_LOCATION + 'has_colours_2.txt')
    w_colours_2 = open(OFFERS_LOCATION + 'wants_colours_2.txt')
    h_certification_2 = open(OFFERS_LOCATION + 'has_certifications_2.txt')
    w_certification_2 = open(OFFERS_LOCATION + 'wants_certifications_2.txt')

    h_items_3 = open(OFFERS_LOCATION + 'has_items_3.txt')
    w_items_3 = open(OFFERS_LOCATION + 'wants_items_3.txt')
    h_colours_3 = open(OFFERS_LOCATION + 'has_colours_3.txt')
    w_colours_3 = open(OFFERS_LOCATION + 'wants_colours_3.txt')
    h_certification_3 = open(OFFERS_LOCATION + 'has_certifications_3.txt')
    w_certification_3 = open(OFFERS_LOCATION + 'wants_certifications_3.txt')

    has_items = h_items.read()
    wants_items = w_items.read()
    has_colours = h_colours.read()
    wants_colours = w_colours.read()
    has_certification = h_certification.read()
    wants_certification = w_certification.read()

    has_items_2 = h_items_2.read()
    wants_items_2 = w_items_2.read()
    has_colours_2 = h_colours_2.read()
    wants_colours_2 = w_colours_2.read()
    has_certification_2 = h_certification_2.read()
    wants_certification_2 = w_certification_2.read()

    has_items_3 = h_items_3.read()
    wants_items_3 = w_items_3.read()
    has_colours_3 = h_colours_3.read()
    wants_colours_3 = w_colours_3.read()
    has_certification_3 = h_certification_3.read()
    wants_certification_3 = w_certification_3.read()

    has_items=has_items.split('-')
    wants_items=wants_items.split('-')
    has_colours=has_colours.split('-')
    wants_colours=wants_colours.split('-')
    has_certification=has_certification.split('-')
    wants_certification=wants_certification.split('-')

    has_items_2=has_items_2.split('-')
    wants_items_2=wants_items_2.split('-')
    has_colours_2=has_colours_2.split('-')
    wants_colours_2=wants_colours_2.split('-')
    has_certification_2=has_certification_2.split('-')
    wants_certification_2=wants_certification_2.split('-')

    has_items_3=has_items_3.split('-')
    wants_items_3=wants_items_3.split('-')
    has_colours_3=has_colours_3.split('-')
    wants_colours_3=wants_colours_3.split('-')
    has_certification_3=has_certification_3.split('-')
    wants_certification_3=wants_certification_3.split('-')

    for i in range(0,len(has_items)):
        try:
            has_items[i] = int(has_items[i])
        except:
            pass

    for i in range(0,len(wants_items)):
        try:
            wants_items[i] = int(wants_items[i])
        except:
            pass

    for i in range(0,len(has_items_2)):
        try:
            has_items_2[i] = int(has_items_2[i])
        except:
            pass

    for i in range(0,len(wants_items_2)):
        try:
            wants_items_2[i] = int(wants_items_2[i])
        except:
            pass

    for i in range(0,len(has_items_3)):
        try:
            has_items_3[i] = int(has_items_3[i])
        except:
            pass

    for i in range(0,len(wants_items_3)):
        try:
            wants_items_3[i] = int(wants_items_3[i])
        except:
            pass

    h_items.close()
    w_items.close()
    h_colours.close()
    w_colours.close()
    h_certification.close()
    w_certification.close()

    h_items_2.close()
    w_items_2.close()
    h_colours_2.close()
    w_colours_2.close()
    h_certification_2.close()
    w_certification_2.close()

    h_items_3.close()
    w_items_3.close()
    h_colours_3.close()
    w_colours_3.close()
    h_certification_3.close()
    w_certification_3.close()

    return has_items, wants_items, has_colours, wants_colours, has_certification, wants_certification, has_items_2, wants_items_2, has_colours_2, wants_colours_2, has_certification_2, wants_certification_2, has_items_3, wants_items_3, has_colours_3, wants_colours_3, has_certification_3, wants_certification_3

multiple_offers_in_trade = False   #Keep false for better price analysis
delay_click = 0.1
load_time = 4
print("Loading Driver...")
options = EdgeOptions()
options.use_chromium = True
options.add_argument('--headless')
driver = Edge("msedgedriver.exe",options=options)
driver.set_window_size(2320, 1080)
driver.get("https://rocket-league.com/trading")
driver.find_element_by_id("acceptPrivacyPolicy").click()

founded = False
os.system('cls')

file = open('price_list.txt', 'w')
has_items, wants_items, has_colours, wants_colours, has_certification, wants_certification, has_items_2, wants_items_2, has_colours_2, wants_colours_2, has_certification_2, wants_certification_2, has_items_3, wants_items_3, has_colours_3, wants_colours_3, has_certification_3, wants_certification_3 = readData()

while True:

    sell_array = []
    buy_array = []
    sell_times = []
    buy_times = []
    
    if len(has_items) != 0:

        for item_has, item_wants, paint_has, paint_wants in zip(has_items,wants_items,has_colours,wants_colours):
            if type(item_has) == str and item_has.strip() != "":
                
                item = item_has
                has_items.remove(item_has)
                wants_items.remove(item_wants)

                if type(paint_has) == str and paint_has.strip() != "":
                    if paint_has[0] != "#":
                        paint = paint_has
                        has_colours.remove(paint_has)
                        wants_colours.remove(paint_wants)

                    else:
                        paint = "None"
                        del has_colours[0]
                        del wants_colours[0]
                else:
                    paint = "None"
                    del has_colours[0]
                    del wants_colours[0]

                break

            elif type(item_wants) == str and item_wants.strip() != "":
                
                item = item_wants
                has_items.remove(item_has)
                wants_items.remove(item_wants)
                if type(paint_wants) == str and paint_wants.strip() != "":
                    if paint_wants[0] != "#":
                        paint = paint_wants
                        has_colours.remove(paint_has)
                        wants_colours.remove(paint_wants)

                    else:
                        paint = "None"
                        del has_colours[0]
                        del wants_colours[0]
                else:
                    paint = "None"
                    del has_colours[0]
                    del wants_colours[0]

                break
    else:
        break
    

    first = True

    for say in range(0,2):
        
        driver.execute_script("window.scrollTo(0, 500)") 
        sleep(load_time)
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


    
    file.write("\n\nSELL ORDER\n\n")
    for i, j in zip(sell_array, sell_times):
        file.write(i + " || " + j.split('\n')[1] + "\n")


    sell_count = []
 
    file.write("\n\nCOUNTS\n\n")

    for i in sell_array:
        if i.find("Credits") != -1:
            if i.find("Credits offer") == -1:
                sell_count.append(i)

    for key, value in dict(sorted(Counter(sell_count).items(), key=lambda item: item[1])).items():
        file.write(str(key + ' =   x' + str(value)) + "\n")



    file.write("\n\nBUY ORDER\n\n")
    for i, j in zip(buy_array, buy_times):
        file.write(i + " || " + j.split('\n')[1] + "\n")


    buy_count = []
    
    file.write("\n\nCOUNTS\n\n")

    for i in buy_array:
        if i.find("Credits") != -1:
            if i.find("Credits offer") == -1:
                buy_count.append(i)

    for key, value in dict(sorted(Counter(buy_count).items(), key=lambda item: item[1])).items():
        file.write(str(key + ' =   x' + str(value)) + "\n")

    file.write("\n===========================================================\n\n")
    print(paint + " colour " + item + " added.")

print("\nDone !")
file.close()
