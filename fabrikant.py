from selenium import webdriver
import unittest, time, re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os

link = "https://admin20.fabrikant.ru/login"
link2 = "https://test.fabrikant.ru/private-office/"

try:
    WebDriver = webdriver.Chrome(executable_path=r'C:\Windows\SysWOW64\chromedriver.exe')
    WebDriver.set_window_size(1920, 1080)
    WebDriver.get(link2)
    login = WebDriver.find_element(by=By.XPATH, value='//input[@name="login[username]"]')
    login.click()
    login.send_keys('fabrikant')
    password = WebDriver.find_element(by=By.XPATH, value='//input[@name="login[password]"]')
    password.click()
    password.send_keys('Qqqq111!')
    submit0 = WebDriver.find_element(by=By.XPATH, value='//button[@type="submit"]')
    submit0.click()
    time.sleep(5)
    WebDriver.get(link)
    time.sleep(2)
    login = WebDriver.find_element(by=By.XPATH, value="//input[@name='login']")
    login.click()
    login.send_keys('m.lazareva')
    time.sleep(2)
    password = WebDriver.find_element(by=By.XPATH, value="//input[@name='password']")
    password.click()
    password.send_keys('9RCNLiweuD')
    submit1 = WebDriver.find_element(by=By.XPATH, value='//button[@type="submit"]')
    submit1.click()
    time.sleep(3)

    create_procedure = WebDriver.find_element(by=By.XPATH, value='//*[@id="nav"]/li[15]/a')
    create_procedure.click()
    template_proc = WebDriver.find_element(by=By.XPATH, value='//*[@id="nav"]/li[15]/ul/li/a')
    template_proc.click()
    input_num = WebDriver.find_element(by=By.XPATH,
                                       value='//input[@type="search"]')
    input_num.click()
    input_num.send_keys('600001\n')
    create_procedure = WebDriver.find_element(by=By.XPATH, value='.//*[text()="Создать процедуру"]')
    create_procedure.click()

    debug = WebDriver.find_element(by=By.XPATH, value='//*[@id="top-menu-2"]/ul[1]/li[8]/a')
    debug.click()
    time.sleep(2)
    izv = WebDriver.find_element(by=By.XPATH, value='//a[@name="fill_dates"]')
    izv.click()
    select_name = Select(
        WebDriver.find_element(by=By.XPATH, value='//select[@name="procedure_participant_info_visibility"]'))
    # WebDriver.execute_script("return arguments[0].scrollIntoView(true);", select1)
    select_name.select_by_value('self')
    select_cost = Select(WebDriver.find_element(by=By.XPATH,
                                                value='//select[@name="procedure_participant_price_visibility"]'))
    select_cost.select_by_value('self')
    select_withnds = Select(WebDriver.find_element(by=By.XPATH,
                                                   value='//select[@name="lot_method_compare_price_offers"]'))
    select_withnds.select_by_value('compare_with_nds')
    select_nds = Select(WebDriver.find_element(by=By.XPATH, value='//select[@name="lot_price[nds]"]'))
    select_nds.select_by_value('20')
    date_checkbox = WebDriver.find_element(by=By.XPATH,
                                           value='//input[@name="proposal_date_start[is_get_date_public]"]')
    date_checkbox.click()

    # add_lot = WebDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a')
    # add_lot.click()
    # izv = WebDriver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/span/a')
    # izv.click()
    # select_withnds_lot = Select(WebDriver.find_element(by=By.XPATH,
    #                                                    value='/html/body/div[1]/div/div[2]/div[2]/div[1]/form/div/div[1]/div[1]/div/div/select'))
    # select_withnds_lot.select_by_value('compare_with_nds')

    add_goods = WebDriver.find_element(by=By.NAME, value='saveAndAddPositions')
    add_goods.click()
    add_position = WebDriver.find_element(by=By.XPATH,
                                          value='(//a[@class="btn btn-raised btn-organizer"])[1]')
    add_position.click()
    izv = WebDriver.find_element(by=By.XPATH, value='//a[@name="fill_dates"]')
    izv.click()
    select_nds = Select(WebDriver.find_element(by=By.XPATH,
                                               value='//select[@name="position_price_per_unit[nds]"]'))
    select_nds.select_by_value('20')
    select_nds2 = Select(WebDriver.find_element(by=By.XPATH,
                                                value='//select[@name="position_price[nds]"]'))
    select_nds2.select_by_value('20')
    save_button = WebDriver.find_element(by=By.NAME, value='save')
    save_button.click()

    put_sum_to_lot_price = WebDriver.find_element(by=By.NAME, value='put_sum_to_lot_price')
    put_sum_to_lot_price.click()
    return_lot = WebDriver.find_element(by=By.XPATH,
                                        value='(//a[@class="btn btn-raised btn-organizer"])[3]')
    return_lot.click()
    upload_doc = WebDriver.find_element(by=By.XPATH,
                                        value='(//a[@class="btn btn-raised btn-organizer"])[2]')
    WebDriver.execute_script("window.scrollTo(document.body.scrollHeight, 0);", upload_doc)
    upload_doc.click()
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "../forautotest/file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)

    # self.find(self.UPLOAD_PROTOCOL_FIELD).send_keys(TEST_TXT_FILE)
    button_file = WebDriver.find_element(by=By.XPATH,
                                         value='(//div[@id="myTabContent"]//div[@class="js-uploader-block"]//input)[1]')
    button_file.send_keys(file_path)
    upload_button = WebDriver.find_element(by=By.XPATH, value='.//*[text()="Загрузить"][1]')
    # WebDriver.execute_script("window.scrollTo(document.body.scrollHeight, 0);", upload_button)
    upload_button.click()
    publication = WebDriver.find_element(by=By.XPATH, value='(//a[@class="btn btn-raised btn-organizer"])[3]')
    publication.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    WebDriver.quit()
