from selenium import webdriver
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime

chrome_driver_path = "/home/msi/Ma formation/100 Days of Code - The Complete Python Pro Bootcamp for 2021/C) Intermediate +/Course/Web Scraping & Automation/7) Selenium Webdriver Browser and Game Playing Bot/Chrome Driver 115/chromedriver-linux64/chromedriver"
brave_browser_path = '/usr/bin/brave-browser'


def get_upgrades(driver: webdriver.Chrome):

    store = driver.find_element(By.ID, "store")

    cursor = store.find_element(By.ID, "buyCursor")

    cursor_price_element = cursor.find_element(By.TAG_NAME, "b")
    # print(int(cursor_price_element.text.strip('Cursor - ').replace(',','')))
    cursor_price = int(cursor_price_element.text.strip(
        'Cursor - ').replace(',', ''))

    grandma = store.find_element(By.ID, "buyGrandma")
    grandma_price_element = grandma.find_element(By.TAG_NAME, "b")
    # print(int(grandma_price_element.text.strip('Grandma - ').replace(',', '')))
    grandma_price = int(grandma_price_element.text.strip(
        'Grandma - ').replace(',', ''))

    factory = store.find_element(By.ID, "buyFactory")
    factory_price_element = factory.find_element(By.TAG_NAME, "b")
    # print(int(factory_price_element.text.strip('Factory - ').replace(',', '')))
    factory_price = int(factory_price_element.text.strip(
        'Factory - ').replace(',', ''))

    mine = store.find_element(By.ID, "buyMine")
    mine_price_element = mine.find_element(By.TAG_NAME, "b")
    # print(int(mine_price_element.text.strip('Mine - ,').replace(',', '')))
    mine_price = int(mine_price_element.text.strip(
        'Mine - ,').replace(',', ''))

    shipment = store.find_element(By.ID, "buyShipment")
    shipment_price_element = shipment.find_element(By.TAG_NAME, "b")
    # print(int(shipment_price_element.text.strip('Shipment - ').replace(',', '')))
    shipment_price = int(shipment_price_element.text.strip(
        'Shipment - ').replace(',', ''))

    alchemy_lab = store.find_element(By.ID, "buyAlchemy lab")
    alchemy_lab_price_element = alchemy_lab.find_element(By.TAG_NAME, "b")
    # print(int(alchemy_lab_price_element.text.strip('Alchemy lab - ').replace(',', '')))
    alchemy_lab_price = int(alchemy_lab_price_element.text.strip(
        'Alchemy lab - ').replace(',', ''))

    portal = store.find_element(By.ID, "buyPortal")
    portal_price_element = portal.find_element(By.TAG_NAME, "b")
    # print(int(portal_price_element.text.strip('Portal - ').replace(',', '')))
    portal_price = int(portal_price_element.text.strip(
        'Portal - ').replace(',', ''))

    time_machine = store.find_element(By.ID, "buyTime machine")
    time_machine_price_element = time_machine.find_element(By.TAG_NAME, "b")
    # print(int(time_machine_price_element.text.strip(
    # 'Time machine - ').replace(',', '')))
    time_machine_price = int(time_machine_price_element.text.strip(
        'Time machine - ').replace(',', ''))

    upgrades = [cursor, grandma, factory, mine,
                shipment, alchemy_lab, portal, time_machine]

    prices = [cursor_price, grandma_price, factory_price, mine_price,
              shipment_price, alchemy_lab_price, portal_price, time_machine_price]
    print(prices)
    return upgrades, prices


def get_money(driver: webdriver.Chrome):
    money = driver.find_element(By.ID, "money")
    my_money = int(money.text.replace(',', ''))
    return my_money


##################################################################################################
chrome_service = Service(executable_path=chrome_driver_path)
chrome_options = Options()
chrome_options.binary_location = brave_browser_path
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

start_game = True
start_time = datetime.datetime.now()
last_upgrade_time = start_time

while start_game:
    cookie.click()
    current_time = datetime.datetime.now()
    print(current_time-last_upgrade_time)
    if current_time-last_upgrade_time > datetime.timedelta(seconds=5):
        last_upgrade_time = datetime.datetime.now()
        my_money = get_money(driver)
        [upgrades, prices] = get_upgrades(driver)
        for price in prices:
            if my_money > price:
                best_affordable_upgrade = price

        upgrades[prices.index(best_affordable_upgrade)].click()

    if current_time - start_time > datetime.timedelta(minutes=5):
        start_game = False
        cps_element = driver.find_element(By.ID, 'cps')
        cps = cps_element.text.strip('cookies/second : ')
        print(f"cookies/second:{cps}")

        # <div id="cps">cookies/second : 0</div>
