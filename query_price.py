from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import math
import pandas as pd
import numpy as np
from site_dictionary import *

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=r'C:\Users\Michael\OneDrive\Projects\chromedriver_win32\chromedriver.exe', options=options)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def currency_to_float(num):
    return float(num.replace('$', '').replace('CAD', '').replace(' ', '').replace('shipping', '').replace('C','').replace('+',''))

#BinderPOS
binderpos = [cardbrawlers, skyfox, frankscloset, enterthebattlefield, laboitemystere, darkfoxtcg, kanzengames, thecgrealm, reddragon,gamezilla,exorgames]
def binderpos_results(website, search):
    website = website["site"]
    search = str.lower(search)
    driver.get("https://"+ website + "/search?page=1&q=%2A"+ search + "%2A")
    if website == cardbrawlers["site"]:
        # wait for page to load in required elements
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--16864109330751__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        # unique website path
        sitepath = '//*[@id="shopify-section-template--16864109330751__content"]/div/div[2]/div['
        # website type
        type = 1
    elif website == skyfox["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--16865359888691__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        sitepath = '//*[@id="shopify-section-template--16865359888691__content"]/div/div[2]/div['
        type = 1
    elif website == frankscloset["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--16686015447275__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        sitepath = '//*[@id="shopify-section-template--16686015447275__content"]/div/div[2]/div['
        type = 1
    elif website == enterthebattlefield["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15962743832747__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        sitepath = '//*[@id="shopify-section-template--15962743832747__content"]/div/div[2]/div['
        type = 1
    elif website == laboitemystere["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15983260303519__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        sitepath = '//*[@id="shopify-section-template--15983260303519__content"]/div/div[2]/div['
        type = 1
    elif website == darkfoxtcg["site"]:
        if check_exists_by_xpath('//*[@id="shopify-section-template--15892603240601__content"]/div[1]/p'):
            return np.nan
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15892603240601__content"]/section/div[2]/div[1]/div[2]/p[1]').text) > 0)
        sitepath = '//*[@id="shopify-section-template--15892603240601__content"]/section/div[2]/div['
        type = 2
    elif website == kanzengames["site"]:
        if check_exists_by_xpath('//*[@id="pageBackground"]/div/main/div/p'):
            return np.nan
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="pageBackground"]/div/main/section[2]/div[2]/div[1]/div[2]/p[1]').text) > 0)
        sitepath = '//*[@id="pageBackground"]/div/main/section[2]/div[2]/div['
        type = 2
    elif website == thecgrealm["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="PageContainer"]/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/p[1]').text) > 0)
        sitepath = '//*[@id="PageContainer"]/div[3]/div/div[2]/div[2]/div/div['
        type = 3
    elif website == reddragon["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15906698559685__content"]/div/div[2]/div[1]/div/div/div[2]/a/div/div').text) > 0)
        sitepath = '//*[@id="shopify-section-template--15906698559685__content"]/div/div[2]/div['
        type = 1
    elif website == gamezilla["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="PageContainer"]/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/p[1]').text) > 0)
        sitepath = '//*[@id="PageContainer"]/div[3]/div/div[2]/div[2]/div/div['
        type = 3
    elif website == exorgames["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--15966556848301__content"]/section/div[2]/div[1]/div[2]/p[1]').text) > 0)
        sitepath = '//*[@id="shopify-section-template--15966556848301__content"]/section/div[2]/div['
        type = 2
    elif website == commonboxgames["site"]:
        if check_exists_by_xpath('//*[@id="shopify-section-template--16843855036720__content"]/div[1]/p'):
            return np.nan
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-template--16843855036720__content"]/section/div[2]/div[1]/div[2]/p[1]').text) > 0)
        sitepath = '//*[@id="shopify-section-template--16843855036720__content"]/section/div[2]/div['
        type = 2
    if type == 1:
        i = 1
        cardname_sec = ']/div/div/div[2]/a/div/div'
        price_sec = ']/div/div/div[2]/div[1]/div/span[2]'
        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        stock = driver.find_elements(By.ID, 'tag-container')
        s = 0
        prices = []
        if search in cardname and stock[s].text == '':
            while search in cardname and stock[s].text == '':
                price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                prices.append(price)
                i = i + 2
                s = s + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                else:
                    break
            price = min(prices)
        else:
            price = np.nan
    elif type == 2:
        i = 1
        setname_sec = ']/div[2]/p[1]'
        cardname_sec = ']/div[2]/p[2]/a'
        price_sec = ']/div[2]/p[3]'
        stock_sec = ']/div[3]'

        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + setname_sec).text + str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text))
        prices = []
        stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
        if search in cardname and not stock:
            while search in cardname and not stock:
                price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                prices.append(price)
                i = i + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + setname_sec).text + driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                    stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
                else:
                    break

            price = min(prices)
        else:
            price = np.nan
    elif type == 3:
        i = 1
        cardname_sec = ']/div[1]/p[1]'
        price_sec = ']/div[1]/p[2]'
        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text
        prices = []
        if search in cardname and not 'Sold Out' in price:
            while search in cardname and not 'Sold Out' in price:
                if 'Varies' in price:
                    prices.append(9999999999)
                else:
                    price = currency_to_float(price)
                    prices.append(price)
                i = i + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                    price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text
                else:
                    break
            price = min(prices)
        else:
            price = np.nan
    return price


#Crystal Commerce
crystalcommerce = [atlascollectables, jeux3dragons, firstplayer, fusiongamingonline, dollys, topdeckhero, cardseternal, comichunter, gamekeeper,cartamagica, godsarena]
def crystalcommerce_results(website, search):
    website = website["site"]
    search = str.lower(search)
    driver.get("https://" + website + "/products/search?q="+ search + "&c=1")
    if website == atlascollectables["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[4]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[4]/section/div/div[4]/ul/li['
        type = 1
    elif website == jeux3dragons["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == firstplayer["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == fusiongamingonline["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 3
    elif website == dollys["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == topdeckhero["site"]:
        if check_exists_by_xpath('//*[@id="page-container"]/div[3]/section/div/p'):
            return np.nan
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 2
    elif website == cardseternal["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == comichunter["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == gamekeeper["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[4]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[4]/section/div/div[4]/ul/li['
        type = 2
    elif website == cartamagica["site"]:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1
    elif website == godsarena["site"]:
        if check_exists_by_xpath('//*[@id="page-container"]/div[3]/section/div/p'):
            return np.nan
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
        sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
        type = 1

    if type == 1:
        i = 1
        cardname_sec = ']/div/div[1]/div[2]/a[1]/h4'
        price_sec = ']/div/div[2]/div[1]/span[2]/form/div[1]/span'
        stock_sec = ']/div/div[2]/div[1]/span[1]/span[2]'
        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        if cardname == "dungeon master's screen wilderness kit" or cardname == "Dungeon Master's Screen Wilderness Kit":
            i = 2
            cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
        prices = []
        if search in cardname:
            while search in cardname:
                if "Out of stock" in stock:
                    prices.append(np.nan)
                else:
                    price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                    prices.append(price)
                i = i + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                    stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
                else:
                    break
            prices = [item for item in prices if not(math.isnan(item)) == True]
            if len(prices) < 1:
                price = np.nan
            else:
                price = min(prices)
        else:
            price = np.nan
    elif type == 2:
        i = 1
        cardname_sec = ']/div/div[1]/div[2]/a[1]/h4'
        price_sec = ']/div/div[2]/div[1]/span[2]/form/div[1]/span'
        stock_sec = ']/div/div[2]/div[1]/span[1]/span/em'
        oos_sec = ']/div/div[2]/div[1]/span[1]/span'

        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        #stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
        prices = []
        if search in cardname:
            while search in cardname:
                if not check_exists_by_xpath(sitepath + str(i) + stock_sec):
                    prices.append(np.nan)
                elif "Out of stock" in driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text:
                    prices.append(np.nan)
                else:
                    price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                    prices.append(price)
                i = i + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                else:
                    break
            prices = [item for item in prices if not(math.isnan(item)) == True]
            if len(prices) < 1:
                price = np.nan
            else:
                price = min(prices)
        else:
            price = np.nan
    elif type == 3:
        i = 1
        cardname_sec = ']/div/div[1]/div[2]/a[1]/h4'
        price_sec = ']/div/div[1]/div[2]/div[1]/div/span[2]/form/div[1]/span'
        stock_sec = ']/div/div[1]/div[2]/div[1]/div/span[1]/span[2]'
        #oos_sec = ']/div/div[1]/div[2]/div[1]/div[1]/span[1]/span[2]'
        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        #stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
        prices = []
        if search in cardname:
            while search in cardname:
                if "Out of stock" in driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text:
                    prices.append(np.nan)
                else:
                    price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                    prices.append(price)
                i = i + 1
                if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                else:
                    break
            prices = [item for item in prices if not(math.isnan(item)) == True]
            if len(prices) < 1:
                price = np.nan
            else:
                price = min(prices)
        else:
            price = np.nan
    return price


# Other Websites
def ebay_results(search):
    search = str.lower(search)
    driver.get("https://www.ebay.ca/sch/i.html?_from=R40&_nkw="+ search + "&_sacat=0&LH_TitleDesc=0&_sop=15&_blrs=recall_filtering&rt=nc&LH_PrefLoc=3")
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[1]/div/div[2]/div[1]/div[1]/h1/span[2]').text) > 0)
    sitepath = '//*[@id="srp-river-results"]/ul/li['
    i = 1
    cardname_sec = ']/div/div[2]/a/div/span'
    price_sec1 = ']/div/div[2]/div[2]/div[1]/span'
    price_sec2 = ']/div/div[2]/div/div[1]/span'
    shipping_sec1 = ']/div/div[2]/div[2]/div[3]/span'
    shipping_sec2 = ']/div/div[2]/div/div[3]/span'
    while not check_exists_by_xpath(sitepath + str(i) + cardname_sec):
        i = i + 1

    cardname = str.lower(driver.find_element(By.XPATH,(sitepath + str(i) + cardname_sec)).text)
    while search not in cardname:
        i = i + 1
        cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    try:
        price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec1).text
        shipping_sec = shipping_sec1
    except:
        price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec2).text
        shipping_sec = shipping_sec2
    if driver.find_element(By.XPATH,sitepath + str(i) + shipping_sec).text != "Free shipping" and driver.find_element(By.XPATH,sitepath + str(i) + shipping_sec).text != "or Best Offer":
        price = currency_to_float(price) + currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + shipping_sec).text)
    else:
        price = currency_to_float(price)
    return price

def facetoface_results(search):
    driver.get("https://www.facetofacegames.com/search/?keyword=" + search + "&sort=priceasc&pg=1&tab=Yu-Gi-Oh!&child_inventory_level=1")
    search = str.lower(search)
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[1]/div/div/h1').text) > 0)
    if "0 search" in driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[1]/div/div/h1').text:
        return np.nan
    else:
        try:
            suggest = driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[1]/ul/h3').text
            if "Did you mean?" in suggest:
                return np.nan
        except:
            if not check_exists_by_xpath('//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/a/h4'):
                return np.nan
            #wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/a/h4').text) > 0)
            cardname = str.lower(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/a/h4').text)
            #wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/span').text) > 0)
            prices = []
            #time.sleep(5)
            for i in range(1,5):
                if check_exists_by_xpath('//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/p/span['+ str(i) +']'):
                    stock = driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/p/span['+ str(i) +']').text
                else:
                    break
                if "In" in stock:
                    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[' + str(i) + ']/span').text) > 0)
                    prices.append(driver.find_element(By.XPATH,'//*[@id="hawksearch__search-page"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[' + str(i) + ']/span').text)
            price = min(prices)
            return currency_to_float(price)

def duelkingdom_results(search):
    search = str.lower(search)
    driver.get("https://duelkingdom.ca/search?filter.v.availability=1&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=show&q="+ search + "&type=product%2Ccollection%2Cpage&sort_by=price-ascending")
    if check_exists_by_xpath('//*[@id="collection-products"]/h5'):
        return np.nan
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="collection-products"]/div/div[1]/div/div[2]/div[1]/h4/a').text) > 0)
    sitepath = '//*[@id="collection-products"]/div/div['
    i = 1
    cardname_sec = ']/div/div[2]/div[1]/h4/a'
    price_sec = ']/div/div[2]/div[2]/div/h6/span'
    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    price = -1
    while search not in cardname:
        i = i + 1
        if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
            cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        else:
            return np.nan
    price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text
    if price == -1:
        price = np.nan
    else:
        price = currency_to_float(price)
    return price

def ygohustle_results(search):
    driver.get("https://ygohustle.com/search?type=product&q="+ search)
    if "NOT YIELD" in driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/div/h1').text:
        return np.nan
    search = str.lower(search)
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/div/div/div[1]/a/p').text) > 0)
    sitepath = '//*[@id="shopify-section-search-template"]/div/div/div/div/div['
    i = 1
    cardname_sec = ']/a/p'
    price_sec = ']/a/div[2]/span/small'
    stock_sec = ']/a/div[1]/div/div[1]/span'
    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    prices = []
    stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
    if search in cardname and not stock:
        while search in cardname and not stock:
            price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
            prices.append(price)
            i = i + 1
            if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
            else:
                break
        price = min(prices)
    else:
        price = np.nan
    return price

def trinityhobby_results(search):
    driver.get("https://trinityhobby.com/search?q="+ search + "&uff_68z6r3_stockStatus=1&usf_sort=price")
    search = str.lower(search)
    if check_exists_by_xpath('//*[@id="usf_container"]/div[2]/div[2]/div/button'):
        return np.nan
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="usf_container"]/div[2]/div[2]/div/a/div[2]/div[1]').text) > 0)
    sitepath = '//*[@id="usf_container"]/div[2]/div[2]/div['
    i = 1
    cardname_sec = ']/a/div[2]/div[1]'
    price_sec = ']/a/div[2]/div[2]/span'
    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    price = -1
    while search not in cardname:
        i = i + 1
        if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
            cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
        else:
            return np.nan
    price = driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text
    if price == -1:
        price = np.nan
    else:
        price = currency_to_float(price)
    return price

def essentialcards_results(search):
    driver.get("https://www.essentialcards.ca/search?type=product&q=" + search)
    search = str.lower(search)
    if "NOT YIELD" in driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/h1').text:
        return np.nan
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/div/div[1]/a/p').text) > 0)
    cardname = driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/div/div[1]/a/p').text
    price = driver.find_element(By.XPATH,'//*[@id="shopify-section-search-template"]/div/div/div/div[1]/a/div[2]/span/small/span').text
    sitepath = '//*[@id="shopify-section-search-template"]/div/div/div/div['
    i = 1
    cardname_sec = ']/a/p'
    price_sec = ']/a/div[2]/span/small/span'
    stock_sec = ']/a/div[1]/div/div[1]/span'
    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    prices = []
    stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
    if search in cardname and not stock:
        while search in cardname and not stock:
            price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
            prices.append(price)
            i = i + 1
            if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                stock = check_exists_by_xpath(sitepath + str(i) + stock_sec)
            else:
                break
        price = min(prices)
    else:
        price = np.nan
    return price

def lapieuvrebarbue_results(search):
    driver.get("https://www.lapieuvrebarbue.com/search?q=" + search + "&filter.v.availability=1&filter.p.product_type=Yu-Gi-Oh%21+Singles")
    search = str.lower(search)
    try:
        wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="prod-"]/div[2]/a/h3').text) > 0)
    except:
        return np.nan
    cardname_lst = driver.find_elements(By.XPATH,'//*[@id="prod-"]/div[2]/a/h3')
    price_lst = driver.find_elements(By.XPATH,'//*[@id="prod-"]/div[2]/div[1]/dl[1]/dd/span')
    prices = []
    i = 0
    length = len(cardname_lst)
    while search in str.lower(cardname_lst[i].text):
        prices.append(currency_to_float(price_lst[i].text))
        i = i + 1
        length = length - 1
        if length == 0:
            break
    if len(prices) < 1:
        return np.nan
    else:
        return min(prices)

def lexpedition_results(search):
    driver.get("https://www.expeditionjeux.com/products/search?q="+ search + "&c=1")
    search = str.lower(search)
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li[1]/div/div[1]/div[2]/a[1]/h4').text) > 0)
    sitepath = '//*[@id="page-container"]/div[3]/section/div/div[4]/ul/li['
    i = 1
    cardname_sec = ']/div/div[1]/div[2]/a[1]/h4'
    price_sec = ']/div/div[2]/div[1]/span[2]/form/div[1]/span'
    stock_sec = ']/div/div[2]/div[1]/span[1]/span[2]'
    cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
    stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
    prices = []
    if search in cardname:
        while search in cardname:
            if "Out of stock" in stock:
                prices.append(np.nan)
            else:
                price = currency_to_float(driver.find_element(By.XPATH,sitepath + str(i) + price_sec).text)
                prices.append(price)
            i = i + 1
            if check_exists_by_xpath(sitepath + str(i) + cardname_sec):
                cardname = str.lower(driver.find_element(By.XPATH,sitepath + str(i) + cardname_sec).text)
                stock = driver.find_element(By.XPATH,sitepath + str(i) + stock_sec).text
            else:
                break
        prices = [item for item in prices if not(math.isnan(item)) == True]
        if len(prices) < 1:
            price = np.nan
        else:
            price = min(prices)
    else:
        price = np.nan
    return(price)



# Market price
def tcgplayer(search):
    driver.get("https://www.google.com/search?q=tcgplayer+market+price+" + search)
    driver.find_element(By.CLASS_NAME, 'yuRUbf').click()
    wait(driver, 10).until(lambda driver: len(driver.find_element(By.XPATH,'//*[@id="app"]/div/div/section[2]/section/div/div[2]/section[3]/div/section[1]/ul/li[1]/span[2]').text) > 0)
    price = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/section[2]/section/div/div[2]/section[3]/div/section[1]/ul/li[1]/span[2]').text
    driver.get("https://www.google.com/search?q=1+usd+to+cad&oq=1+USD+to+CAD&aqs=chrome.0.0i433i512j0i512l6j69i60.2978j1j1&sourceid=chrome&ie=UTF-8")
    rate = driver.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    return round(currency_to_float(price) * float(rate), 2)

#test all functions above
def loop_sites(search):
    for site in binderpos:
        try:
            print(site["name"] + ": ")
            print(binderpos_results(site,search))
        except:
            print(site["name"] + " doesn't work")
    for site in crystalcommerce:
        try:
            print(site["name"] + ": ")
            print(crystalcommerce_results(site,search))
        except:
            print(site["name"] + " doesn't work")
    try:
        print(ebay["name"] + ": ")
        print(ebay_results(search))
    except:
        print("ebay doesn't work")
    try:
        print(facetoface["name"] + ": ")
        print(facetoface_results(search))
    except:
        print("facetoface doesn't work")
    try:
        print(duelkingdom["name"] + ": ")
        print(duelkingdom_results(search))
    except:
        print("duelkingdom doesn't work")
    try:
        print(ygohustle["name"] + ": ")
        print(ygohustle_results(search))
    except:
        print("ygohustle doesn't work")
    try:
        print(trinityhobby["name"] + ": ")
        print(trinityhobby_results(search))
    except:
        print("trinityhobby doesn't work")
    try:
        print(essentialcards["name"] + ": ")
        print(essentialcards_results(search))
    except:
        print("essentialcards doesn't work")
    try:
        print(lapieuvrebarbue["name"] + ": ")
        print(lapieuvrebarbue_results(search))
    except:
        print("lapieuvrebarbue doesn't work")
    print("Market Price: ")
    print(tcgplayer(search))
    driver.quit()


def test_site(csv):
    search = pd.read_csv(csv, names = ['search', 'quantity',''])
    list = search["search"].tolist()
    for card in list:
        print(binderpos_results(exorgames, card))
