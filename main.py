import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


forms_link='https://docs.google.com/forms/d/e/1FAIpQLScmVqcLE84iA3M3Rv_Daau9a5f5hZmcxyGEtrxCxZi55jLOVw/viewform?usp=sf_link'
apartments_url='https://www.apartments.com/san-francisco-ca/under-3400/?bb=lkt1ogn12Og5kkx-a'
headers={
"User-Agent": os.environ.get('USER_AGENT', ''),
"Accept-Language" : os.environ.get('ACCEPT_LANGUAGE', '')}

response=requests.get(apartments_url, headers=headers)
response.raise_for_status()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(apartments_url)
soup=BeautifulSoup(response.content, 'html.parser')

all_prices=[]
all_links=[]
all_addresses=[]

def info_from_one_page():
    prices_with_everything = soup.find_all(class_='property-pricing')
    prices = [price.text for price in prices_with_everything]
    addresses_with_everythink = soup.find_all(class_='js-url')
    addresses = [address.text for address in addresses_with_everythink]
    addresses = [address for address in addresses if address != '\n\n\n\n']
    links_with_everything = driver.find_elements(By.CLASS_NAME, 'property-link')
    links = [content.get_attribute('href') for content in links_with_everything]
    all_prices.extend(prices)
    all_addresses.extend(addresses)
    all_links.extend(links)


while True:
    info_from_one_page()
    try:
        next_button = driver.find_element(By.CLASS_NAME, 'next')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'next')))
        next_button.click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except NoSuchElementException:
        print("Nie znaleziono elementu 'Next'. Zakończono proces.")
        break
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        break

info_from_one_page()
driver.quit()


driver = webdriver.Chrome(options=chrome_options)
driver.get(forms_link)


for i in range(len(all_addresses)):
    time.sleep(1)
    adr_input = driver.find_element(By.CSS_SELECTOR,
                                    '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    adr_input.send_keys(all_addresses[i])

    price_input = driver.find_element(By.CSS_SELECTOR,
                                      '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    price_input.send_keys(all_prices[i])

    link_input = driver.find_element(By.CSS_SELECTOR,
                                     '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    link_input.send_keys(all_links[i])
    send = driver.find_element(By.CSS_SELECTOR,
                               '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div')
    send.click()
    driver.back()


