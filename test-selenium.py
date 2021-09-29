from selenium import webdriver
import chromedriver_binary
import json
import pytest


class TestSagamiSelenium:
  @pytest.fixture
  def test_login(self):
    driver = webdriver.Chrome()

    driver.get("https://kouza-st.offgrid.ninja/creete_admin/")

    email_pass = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/div/div[1]/input')
    password_pass = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/div/div[2]/input')

    email_pass.send_keys('nagato@offgrid.co.jp')
    password_pass.send_keys('1234')

    button = driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/button')
    button.click()
    return driver

  def test1(self, test_login):
    json_open = open('config.json', 'r', encoding='UTF8')
    json_load = json.load(json_open)
    print(json_load['text'])
    json_open.close()

    title_pass = test_login.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/h3')

    assert json_load['text'] == title_pass.text

  def test2(self, test_login):
    json_open = open('config.json', 'r', encoding='UTF8')
    json_load = json.load(json_open)
    print(json_load['contact_title'])
    json_open.close()
    contact = test_login.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[4]/a')
    contact.click()
    contact_list = test_login.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[4]/ul/li/a')
    contact_list.click()
    contact_title = test_login.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/h3').text

    assert contact_title == json_load['contact_title']
