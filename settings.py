from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time as tm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import os, glob
from set import Method
from page_object import Page
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class settings1(): # by Anton Chingaev
    def __init__(self):
        self.met = Method()
        self.page = Page()

    def auth(self, driver, login, password): # Авторизация на страницу
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.excretion(driver.find_element(By.NAME, self.page.login), driver, login, False)
        self.met.excretion(driver.find_element(By.NAME, self.page.passowrd), driver, password, False)
        self.met.click_element(driver, wait, xpath_name=self.page.button_come_in)

    def open_project(self, driver): # Открыть проект
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project)
        self.met.mouse_over(driver, wait, xpath_name=self.page.project_bis)
        self.met.mouse_over(driver, wait, xpath_name=self.page.project_training)
        self.met.click_element(driver, wait, xpath_name=self.page.project_test)

    def num_1(self, driver): # Открытие карточки создания контракта
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.сontract_management)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)
        self.met.visibly(driver, xpath_name='//iframe[@class="modal-iframe"]', vis=True)
        self.met.text_search(driver, xpath_name=self.page.metca_create_contract, teg='h3', text='Создать контракт')
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        tm.sleep(2)

    def num_2(self, driver): # Открытие карточки создания типового документа
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.documents_management)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)
        self.met.text_search(driver, xpath_name=self.page.metca_create_documents, teg='h3', text='Создать типовые документы')
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        tm.sleep(2)

    def num_3(self, driver): # Открытие карточки создания документа
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.project_management_doc)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)
        self.met.text_search(driver, xpath_name=self.page.metca_project_management_doc, teg='h3', text='Создать документ')
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        tm.sleep(2)

    def num_4(self, driver): # Открытие настроек категории
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.project_management_doc_new)
        self.met.click_element(driver, wait, xpath_name=self.page.button_add)
        self.met.text_search(driver, xpath_name=self.page.partition_window, teg='h3', text='Добавить')
        tm.sleep(2)

    def num_5(self, driver): # Создание документа
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)
        now_time = f'{datetime.strftime(datetime.now(),  "%d-%m-%y %H:%M:%S")}'

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)
        self.met.frame_switch(driver, True)
        self.met.excretion(driver.find_element(By.XPATH, self.page.field_name), driver, now_time, False)
        self.met.frame_switch(driver, False)
        self.met.click_element(driver, wait, xpath_name=self.page.btn_create_in_frame)

        self.met.text_search(driver, xpath_name=self.page.field_name_reestr, teg='a', text=now_time)

        self.met.click_element(driver, wait, xpath_name=f"{self.page.structural_list}//tr[@data-id='{self.met.find_id_element(driver, now_time)}']{self.page.rt_field_actions}")

        self.met.click_element(driver, wait, xpath_name=self.page.delete_field)
        self.met.action_on_alerts(driver, action=True)

        tm.sleep(1)
        try:
            self.met.text_search(driver, xpath_name=self.page.field_name_reestr, teg='a', text=now_time)
            raise 'Элемент не удален'
        except NoSuchElementException:
            pass