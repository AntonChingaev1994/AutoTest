from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import settings1
from selenium.webdriver.chrome.service import Service


class Statistika_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service('C:\chromedriver\chromedriver.exe'))
        self.driver.maximize_window()
        self.auth_1 = settings1()
        self.url = 'https://t.devcontrol.ru/'
        self.login = 'chingaev'
        self.password = 'aschingaev1994'

    def test_01(self):
        self.driver.get('{}'.format(self.url))
        self.auth_1.auth(self.driver, self.login, self.password) # Авторизация на страницу
        self.auth_1.open_project(self.driver) # Открытие проекта
        self.auth_1.num_1(self.driver) # Открытие карточки создания контракта

    def test_02(self):
        self.driver.get('{}'.format(self.url))
        self.auth_1.auth(self.driver, self.login, self.password) # Авторизация на страницу
        self.auth_1.open_project(self.driver) # Открытие проекта
        self.auth_1.num_2(self.driver) # Открытие карточки создания типового документа

    def test_03(self):
        self.driver.get('{}'.format(self.url))
        self.auth_1.auth(self.driver, self.login, self.password)  # Авторизация на страницу
        self.auth_1.open_project(self.driver) # Открытие проекта
        self.auth_1.num_3(self.driver) # Открытие карточки управления проектом

    def test_04(self):
        self.driver.get('{}'.format(self.url))
        self.auth_1.auth(self.driver, self.login, self.password)  # Авторизация на страницу
        self.auth_1.open_project(self.driver) # Открытие проекта
        self.auth_1.num_4(self.driver) # Открытие карточки управления проектом(new)

    def test_05(self):
        self.driver.get('{}'.format(self.url))
        self.auth_1.auth(self.driver, self.login, self.password)  # Авторизация на страницу
        self.auth_1.open_project(self.driver) # Открытие проекта
        self.auth_1.num_5(self.driver) # Создание и удаление документа

    def teatDown(self):
        self.driver.quit()


if __name__=='__main__':
    unittest.main()
