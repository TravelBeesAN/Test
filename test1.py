import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

a = 1
b = 3
@pytest.fixture
def common_setup():
  driver = webdriver.Chrome()
  driver.implicitly_wait(5)
  driver.get("https://time.mk/st/vesti")
  driver.maximize_window()
  yield driver
  driver.quit()


def test_1(common_setup):
    driver = common_setup

    try:
     sport = driver.find_element(By.XPATH, "//*[@id='super_1']/center")
     sport.click()
     time.sleep(2)

     fudbal = driver.find_element(By.XPATH, "//*[@id='c1']/center")
     fudbal.click()
     time.sleep(2)

     test1 = driver.find_element(By.XPATH, "//*[@id='c1']/span").text

     expected_test1 = "Фудбалm"
     assert test1 == expected_test1, f"Error! Expected name {expected_test1} is not same with the test1"
     print("Test1 passed! Very successful test")
     time.sleep(2)

    except Exception as e:
     print(f"Error encountered here: {e}")
     page2 = driver.find_element(By.XPATH, "//*[@id='news_pane']/div[2]/a[2]/span/center")
     page2.click()
     time.sleep(2)

     blog = driver.find_element(By.XPATH, "//*[@id='footer']/center/div/a[5]/span")
     blog.click()

     test2 = driver.find_element(By.XPATH, "//*[@id='c0']/span").text

     expected_test2 = "Студиска mпрограма по информатика базирана на MOOC курсеви"
     assert test2 == expected_test2, f"Error! Not expected page!!!"
     print("Test2 passed! Very successful test")
     time.sleep(2)

    finally:
     home = driver.find_element(By.XPATH, "//*[@id='logo']")
     home.click()
     time.sleep(2)

     success = driver.find_element(By.XPATH, "//*[@id='page_title']/center/p").text
     expected_test3 = "Топ теми на денот"

     assert success == expected_test3, f"Error!!!"
     print("Test3 passed! Very successful test")

     time.sleep(2)

def test_2():
    #driver = common_setup
    big = a+b
    small =a+a
    assert big<small, f"Not True! {big} is bigger then {small}"
    print("True")











