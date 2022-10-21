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
from set import Method, ModalContentIframe, ModalWindow, DropdownMmenuRight
from page_object import Page
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class settings1(): # by Anton Chingaev
    def __init__(self):
        self.met = Method()
        self.page = Page()
        self.frame = ModalContentIframe()
        self.modal_window = ModalWindow()
        self.right_menu = DropdownMmenuRight()

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

        element = self.met.text_search(driver, xpath_name=self.page.metca_create_contract, teg='h3', text='Создать контракт')

        self.met.check_visible(driver, element, True)
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        self.met.check_visible(driver, element, False)
        tm.sleep(2)

    def num_2(self, driver): # Открытие карточки создания типового документа
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.documents_management)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)

        element = self.met.text_search(driver, xpath_name=self.page.metca_create_documents, teg='h3', text='Создать типовые документы')

        self.met.check_visible(driver, element, True)
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        self.met.check_visible(driver, element, False)
        tm.sleep(2)

    def num_3(self, driver): # Открытие карточки управления проектом
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.project_management_doc)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)

        element = self.met.text_search(driver, xpath_name=self.page.metca_project_management_doc, teg='h3', text='Создать документ')

        self.met.check_visible(driver, element, True)
        self.met.click_element(driver, wait, xpath_name=self.page.btn_close)
        self.met.check_visible(driver, element, False)
        tm.sleep(2)

    def num_4(self, driver): # Открытие карточки управления проектом(new)
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 10)
        string = 'Развитие ЦУС в рамках сроков с 13.05.2019 по 30.06.2019, в сроках не учтен период проведения испытаний, пилотирования, тестирования'

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.project_management_doc_new)

        self.met.check_visible(driver, f'//div[@class="tree_list_table"]//a[text()="{string}"]', False)
        self.met.click_element(driver, wait, xpath_name=self.page.btn_fill_in_template)

        self.met.click_element(driver, wait, xpath_name='//div[text()="Объект"]//..')
        self.modal_window.select_element(driver, wait, id=11, title='тест')

        self.met.click_element(driver, wait, xpath_name='//div[text()="Версия УП"]//..')
        self.modal_window.select_element(driver, wait, id=3, title='Начальная версия')

        self.met.click_element(driver, wait, xpath_name=self.page.btn_success)
        self.met.action_on_alerts(driver, action=True)
        tm.sleep(1)
        self.met.action_on_alerts(driver, action=True)
        self.met.check_visible(driver, f'//div[@class="tree_list_table"]//a[text()="{string}"]', True)

        id = self.met.get_atribut(driver, xpth=f'//div[@class="tree_list_table"]//a[text()="{string}"]', iter=2, atribut='data-id')
        self.met.click_element(driver, wait, xpath_name=f'//div[@data-id="{id}"]//a[@title="Действия"]')

        self.met.click_element(driver, wait, xpath_name='//ul[@class="dropdown-menu pull-right not_active show"]//a[@title="Удалить"]')
        self.met.action_on_alerts(driver, action=True)
        self.met.check_visible(driver, f'//div[@class="tree_list_table"]//a[text()="{string}"]', False)
        tm.sleep(2)

    def num_5(self, driver): # Создание и удаление документа
        driver.implicitly_wait(20)
        wait = WebDriverWait(driver, 20)
        now_time = f'{datetime.strftime(datetime.now(),  "%d-%m-%y %H:%M:%S")}'

        self.met.click_element(driver, wait, xpath_name=self.page.project_management)
        self.met.click_element(driver, wait, xpath_name=self.page.create_button)

        self.frame.paste_text(driver, self.page.field_name, now_time)
        self.frame.click_field(driver, wait, 'Тип')
        self.modal_window.select_element(driver, wait, 135, 'Правоустанавливающие документы')

        self.met.click_element(driver, wait, xpath_name=self.page.btn_create_in_frame)

        element = self.met.text_search(driver, xpath_name=self.page.field_name_reestr, teg='a', text=now_time)

        self.met.check_visible(driver, element, True)

        id = self.met.get_atribut(driver, xpth=f'//td[@class="rt_c rt_field_title"]//a[text()="{now_time}"]', iter=2, atribut='data-id')
        self.met.click_element(driver, wait, xpath_name=f"{self.page.structural_list}//tr[@data-id='{id}']{self.page.rt_field_actions}")

        self.right_menu.delete(driver, wait)
        self.met.action_on_alerts(driver, action=True)

        self.met.check_visible(driver, element, False)