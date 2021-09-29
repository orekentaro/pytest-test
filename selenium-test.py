import time
from selenium import webdriver
import chromedriver_binary
import json
from selenium.webdriver.support.select import Select

json_open = open('config.json', 'r', encoding='UTF8')
json_load = json.load(json_open)
json_open.close()
driver = webdriver.Chrome()

driver.get("https://kouza-st.offgrid.ninja/")
button = driver.find_element_by_xpath('//*[@id="header"]/nav/div[2]/div/ul/li[5]/a')
button.click()
option_pass = driver.find_element_by_xpath('//*[@id="kouza1"]/option[2]')
dropdown = driver.find_element_by_xpath('//*[@id="kouza1"]')
select = Select(dropdown)
select.select_by_index(1)
# radio = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[20]/div/div/label')
# radio.click()
check = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[20]/div/div/label')
driver.execute_script("arguments[0].click();", check)
driver.find_element_by_xpath('//*[@id="postbutton"]').click()
ken_drop_down = driver.find_element_by_xpath('//*[@id="ken"]')
ken = Select(ken_drop_down)
ken.select_by_index(18)
time.sleep(0.5)
siku_drop_down = driver.find_element_by_xpath('//*[@id="shiku"]')
siku = Select(siku_drop_down)
siku.select_by_index(10)
time.sleep(0.5)
chou_drop_down = driver.find_element_by_xpath('//*[@id="chou"]')
chou = Select(chou_drop_down)
chou.select_by_index(5)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="find-postcode"]').click()