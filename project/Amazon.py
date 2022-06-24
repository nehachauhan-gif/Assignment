import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s= Service('chromedriver.exe')
opt = Options()
opt.add_argument("--window-size=1920,1080")  #Initialize a webdriver with resolution (1920x1080)
opt.add_argument("--disable-notifications")  #Close any pop-ups if appearing

driver=webdriver.Chrome(service=s,options=opt)
driver.get("https://www.amazon.in")          #Open amazon website

searchbox=driver.find_element(by=By.XPATH,value='//*[@id="twotabsearchtextbox"]') #seraching item in search box
searchbox.send_keys("Mobile")
searchbox.send_keys(Keys.ENTER)   #hit enter key

spans=driver.find_elements(by=By.XPATH,value='//span[@class="a-size-medium a-color-base a-text-normal"]')

dit={}
for i in range(len(spans)):
    if i==0:
        print(spans[i].text)  #extract the title text of the first item showing
        b=spans[i].text.split("(")
        dit['moblie']={}
        dit['moblie']['name']=b[0]
        dit['moblie']['specifications']=b[1]
print("items=",dit)           #Output the result in dictionary




















