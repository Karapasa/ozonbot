import time, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

'''Бот для ПФ на товары озона'''


def gal_right():
    # 5 раз прокручивает фото в галереи
    for i in range(0, 4):
        webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
        time.sleep(3)

for url in open('urls.txt', 'r'):
    # Объект Хрома с путем к движку
    driver = webdriver.Chrome(os.path.abspath('chromedriver'))

    # Получаем нужную страницу из листа
    driver.get(url)
    WebDriverWait(driver, 7)

    # Находит первую фотку и кликает по ней
    gallery = driver.find_element_by_class_name('a1i9').click()
    time.sleep(4)

    gal_right()
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Находит блок с описание и переходит к нему
    scroll = driver.find_element_by_class_name('b0b3').location_once_scrolled_into_view
    time.sleep(5)
    # Возвращается в начало страницы
    webdriver.ActionChains(driver).send_keys(Keys.HOME).perform()
    time.sleep(3)

    # Находит ссылку бренда переходит к ней и кликает
    dics = driver.find_element_by_link_text('Все товары Minimore')
    dics.location_once_scrolled_into_view
    time.sleep(3)
    dics.click()

    WebDriverWait(driver, 6)

    # Эмулирует скролл вниз стрелкой
    for i in range(1, 100):
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
    time.sleep(4)

    driver.quit()
