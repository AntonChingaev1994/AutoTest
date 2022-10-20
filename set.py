from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os, glob


def write_a_log1(index, string):
    with open("Выгрузка_документов_log.txt", "a") as f:
        if index == True:
            f.write('- {} ----- Успешно\n'.format(string))
        else:
            f.write('{}\n'.format(string))

def click1(elem, driver):  # Выделение текста на кликующем элементе
    original_style = elem.get_attribute('style')
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          "background: yellow; border: 2px solid red;")
    time.sleep(0.3)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          original_style)
    elem.click()

def excretion1(elem, driver): # Выделение текста (только для строк даты)
    original_style = elem.get_attribute('style')
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          "background: yellow; border: 2px solid red;")
    time.sleep(0.3)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                      original_style)


def excretion(elem, driver, names, key): # Выделение строки и вставка данных
    original_style = elem.get_attribute('style')
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                      "background: yellow; border: 2px solid red;")
    time.sleep(0.3)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                      original_style)
    elem.send_keys('{}'.format(names))
    if key == True:
        driver.find_element_by_xpath('//div[@class="controls-Suggest__suggestionsContainer controls-Suggest__suggestionsContainer_theme-default controls-Suggest__suggestionsContainer-inInput"]') # Поиск элемента перед нажатием Enter
        time.sleep(3)
        elem.send_keys(Keys.ENTER)
        time.sleep(3)


def proverka(driver, wait, xpath_name):  # Ждать когда появиться элемент
    try:
        driver.implicitly_wait(40)
        driver.find_element_by_xpath('{}'.format(xpath_name))
        time.sleep(1)
        click1(wait.until(EC.element_to_be_clickable((By.XPATH, '{}'.format(xpath_name)))), driver)
    except NoSuchElementException:
        write_a_log1(False, 'Не найден элемент ----- Тест провален')
        driver.close()

class Method():
    def time_out(self, driver, name_doc, name): # Ждать пока исчезнет элемент
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)
        click1(wait.until(EC.element_to_be_clickable((By.XPATH, '{}'.format(name)))), driver)
        while True:
            try:
                prover = driver.find_element_by_xpath('{}'.format(name_doc)) # Ожидает пока пропадет элемент(карточка документа)
                if prover != None:
                    continue
            except NoSuchElementException:
                break

    def excretion(self, elem, driver, names, key): # Выделение строки и вставка данных
        original_style = elem.get_attribute('style')
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          "background: yellow; border: 2px solid red;")
        time.sleep(0.3)
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", elem,
                          original_style)
        elem.send_keys('{}'.format(names))
        if key == True:
            driver.find_element_by_xpath('//div[@class="controls-Suggest__suggestionsContainer controls-Suggest__suggestionsContainer_theme-default controls-Suggest__suggestionsContainer-inInput"]') # Поиск элемента перед нажатием Enter
            time.sleep(3)
            elem.send_keys(Keys.ENTER)
            time.sleep(3)

    def click_element(self, driver, wait, xpath_name):  # Ждать когда появиться элемент
        try:
            driver.implicitly_wait(40)
            driver.find_element(By.XPATH, f'{xpath_name}')
            time.sleep(1)
            click1(wait.until(EC.element_to_be_clickable((By.XPATH, '{}'.format(xpath_name)))), driver)
        except NoSuchElementException:
            write_a_log1(False, 'Не найден элемент ----- Тест провален')
            driver.close()

    def proverka_new(self, driver, wait, xpath_name): # ???
        try:
            driver.find_element_by_xpath('{}'.format(xpath_name))
            click1(wait.until(EC.element_to_be_clickable((By.XPATH, '{}'.format(xpath_name)))), driver)
        except NoSuchElementException:
            write_a_log1(False, string='PDF реестр документа не скачался ----- Тест провален')
            driver.close()

    def data(self, driver, dict_name): # Работа с датами
        excretion1(driver.find_element_by_xpath('{}'.format(dict_name[2])), driver)
        for x in range(3):
            if x <= 1:
                driver.find_element_by_xpath('{}'.format(dict_name[1])).send_keys(dict_name[0])
            else:
                driver.find_element_by_xpath('{}'.format(dict_name[1])).send_keys('20')

    def write_a_log(self, index, string):
        with open("Выгрузка_документов_log.txt", "a") as f:
            if index == True:
                f.write('---- {}\n'.format(string))
            else:
                f.write('{}\n'.format(string))

    def check_filter(self, driver, wait):
        new_driver = driver
        proverka(driver, wait, xpath_name='//div[@name="detailPanelTarget"]')
        try:
            new_driver.implicitly_wait(2)
            new_driver.find_element_by_xpath('//*[text()="По умолчанию"]')
            proverka(driver, wait, xpath_name='//*[text()="По умолчанию"]')
            proverka(driver, wait, xpath_name='//*[text()="Отобрать"]')
        except NoSuchElementException:
            proverka(driver, wait,xpath_name='//div[@class="controls-Button__close__icon_toolButton-theme_default"]')
            time.sleep(1)

    def mouse_over(self, driver, wait, xpath_name):
        try:
            driver.implicitly_wait(40)
            driver.find_element(By.XPATH, f'{xpath_name}')
            time.sleep(1)
            element_to_hover_over = driver.find_element(By.XPATH, f"{xpath_name}")
            ActionChains(driver).move_to_element(element_to_hover_over).perform()
        except NoSuchElementException:
            driver.close()

    def find_element(self, driver, xpath_name):
        try:
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, f'{xpath_name}')
        except NoSuchElementException:
            driver.close()

    def frame_switch(self, driver, switch=True):
        if switch:
            driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="modal-iframe"]'))
        else:
            driver.switch_to.default_content()

    def text_search(self, driver, xpath_name, teg, text):

        driver.implicitly_wait(20)

        driver.find_element(By.XPATH, f"{xpath_name}//{teg}[text()='{text}']")


    def action_on_alerts(self, driver, action):
        if action:
            driver.switch_to.alert.accept()
        else:
            driver.switch_to.alert.dismiss()


    def visibly(self, driver, xpath_name, vis=True):

        driver.find_element(By.XPATH, f'{xpath_name}').is_displayed()
        if vis:
            driver.find_element(By.XPATH, f'{xpath_name}')
        else:
            try:
                driver.find_element(By.XPATH, f'{xpath_name}').is_displayed()
                print('Элемент виден')
            except:
                print('Элемент не виден')
                driver.close()

    def find_id_element(self, driver, now_time):
        return driver.find_element(
            By.XPATH, f"//td[@class='rt_c rt_field_title']//a[text()='{now_time}']//..//..").get_attribute('data-id')

    # def find_id_element_2(self, driver, xpath, el, attribute):
    #
    #     for value in range(el):
    #         xpath += '//..'
    #
    #     return driver.find_element(By.XPATH, f"{xpath}").get_attribute(attribute)
