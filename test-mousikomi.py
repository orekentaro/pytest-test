from selenium import webdriver
import chromedriver_binary
import json
import pytest
from selenium.webdriver.support.select import Select
import time


class TestSelenium:
  @pytest.fixture
  def test_driver(self):
    driver = webdriver.Chrome()

    driver.get("https://kouza-st.offgrid.ninja/")
    button = driver.find_element_by_xpath('//*[@id="header"]/nav/div[2]/div/ul/li[5]/a')
    button.click()
    return driver

  def test_view_mousikomi(self, test_driver):
    with open('config.json', 'r', encoding='UTF8') as json_open:
      json_load = json.load(json_open)
      title_pass = test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[1]')

      assert json_load['mousikomi_title'] == title_pass.text

  def test_select(self, test_driver):
    with open('config.json', 'r', encoding='UTF8') as json_open:
      json_load = json.load(json_open)
      title_pass = test_driver.find_element_by_xpath('//*[@id="kouza1"]/option[2]')

      assert json_load['test_select'] == title_pass.text

  def test_selected(self, test_driver):
    with open('config.json', 'r', encoding='UTF8') as json_open:
      json_load = json.load(json_open)
      # プルダウンの選択
      dropdown = test_driver.find_element_by_xpath('//*[@id="kouza1"]')
      # インスタンス化
      select = Select(dropdown)
      # インデックス０が初期表示なので1を選択
      select.select_by_index(1)
      # 名前セット
      test_driver.find_element_by_xpath('//*[@id="name1"]').send_keys('永戸　健太郎')
      # カナセット
      test_driver.find_element_by_xpath('//*[@id="name2"]').send_keys('ナガト　ケンタロウ')
      # 年齢
      test_driver.find_element_by_xpath('//*[@id="age1"]').send_keys(30)
      # 性別ラジオボタンを選択
      test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[10]/div/div[3]/label').click()
      # 郵便番号
      test_driver.find_element_by_xpath('//*[@id="post1"]').send_keys(5121216)
      time.sleep(0.1)
      # 電話番号
      test_driver.find_element_by_xpath('//*[@id="phone1"]').send_keys("09054853215")
      # 緊急連絡先
      test_driver.find_element_by_xpath('//*[@id="emgphone1"]').send_keys('0120828828')
      # メール
      test_driver.find_element_by_xpath('//*[@id="mail"]').send_keys('unchi@gmail.com')
      # 会員ラジオボタンを選択
      check = test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[20]/div/div/label')
      test_driver.execute_script("arguments[0].click();", check)
      time.sleep(0.1)
      # フォーム送信
      test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[21]/div/input').click()
      # 確認
      check_text = test_driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div/p').text
    assert json_load['check'] == check_text

  def test_modal(self, test_driver):
    with open('config.json', 'r', encoding='UTF8') as json_open:
      json_load = json.load(json_open)
      # プルダウンの選択
      dropdown = test_driver.find_element_by_xpath('//*[@id="kouza1"]')
      # インスタンス化
      select = Select(dropdown)
      # インデックス０が初期表示なので1を選択
      select.select_by_index(1)
      # 名前セット
      test_driver.find_element_by_xpath('//*[@id="name1"]').send_keys('永戸　健太郎')
      # カナセット
      test_driver.find_element_by_xpath('//*[@id="name2"]').send_keys('ナガト　ケンタロウ')
      # 年齢
      test_driver.find_element_by_xpath('//*[@id="age1"]').send_keys(30)
      # 性別ラジオボタンを選択
      test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[10]/div/div[3]/label').click()
      # 住所検索ボタンクリック
      test_driver.find_element_by_xpath('//*[@id="postbutton"]').click()
      # 都道府県をセレクト
      ken_drop_down = test_driver.find_element_by_xpath('//*[@id="ken"]')
      ken = Select(ken_drop_down)
      ken.select_by_index(18)
      # Ajax問合せの為少し停止
      time.sleep(0.5)
      # 市区町村セレクト
      siku_drop_down = test_driver.find_element_by_xpath('//*[@id="shiku"]')
      siku = Select(siku_drop_down)
      siku.select_by_index(10)
      # Ajax問合せの為少し停止
      time.sleep(0.5)
      # 町名をセレクト
      chou_drop_down = test_driver.find_element_by_xpath('//*[@id="chou"]')
      chou = Select(chou_drop_down)
      chou.select_by_index(5)
      # Ajax問合せの為少し停止
      time.sleep(0.5)
      # 確定ボタン
      test_driver.find_element_by_xpath('//*[@id="find-postcode"]').click()
      # モーダルが閉じる前に動いてエラーになる為停止
      time.sleep(0.5)
      # 電話番号
      test_driver.find_element_by_xpath('//*[@id="phone1"]').send_keys("09054853215")
      # 緊急連絡先
      test_driver.find_element_by_xpath('//*[@id="emgphone1"]').send_keys('0120828828')
      # メール
      test_driver.find_element_by_xpath('//*[@id="mail"]').send_keys('unchi@gmail.com')
      # 会員ラジオボタンを選択
      check = test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[20]/div/div/label')
      test_driver.execute_script("arguments[0].click();", check)
      time.sleep(0.5)
      # フォーム送信
      test_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[3]/div/form/div[21]/div/input').click()
      # 申込ボタン
      test_driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[4]/div/form/div[22]/div/button[2]').click()
      # 確認
      check_text = test_driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]').text

    assert json_load['compl'] == check_text
