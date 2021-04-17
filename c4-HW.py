from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

my_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
my_driver.get("http://walla.co.il")

#ffdriver = webdriver.Firefox(executable_path="C:/geckodriver.exe")
#ffdriver.get("ynet.co.il")
my_driver.close()