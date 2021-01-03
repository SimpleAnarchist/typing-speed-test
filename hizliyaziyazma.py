from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, element

browser = webdriver.Chrome()
browser.get("https://www.m5bilisim.com/tr/on-parmak/hiz-testi/")
sleep(3)

listem = []

div = browser.find_element_by_id("satir")
soup = BeautifulSoup(div.get_attribute("innerHTML"), "html.parser")

for i in soup.find_all("span"):
    listem.append(i.text)


for liste in listem:
    print("*****************")
    print(liste)
    hizliyaz = browser.find_element_by_xpath("//*[@id='yaziyaz']").send_keys(liste, Keys.SPACE)
    sleep(0.20)

kalan = browser.find_element_by_css_selector("span[id^='zaman']")

sleep(int(kalan.text.replace(":","").lstrip("0")) + 5)

browser.close()