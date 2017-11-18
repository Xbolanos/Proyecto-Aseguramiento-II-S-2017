# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestSystem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait = WebDriverWait(self.driver, 5*60)

    def test_system(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Ingresar").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("admin@reconoceme.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123Queso")
        driver.find_element_by_css_selector("input.load-images-button").click()
        driver.find_element_by_link_text("ReconoceME").click()
        driver.find_element_by_id("trainingFiles").clear()
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/1.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/2.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/3.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/4.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/5.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/6.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/7.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/8.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/9.pgm")
        driver.find_element_by_id("trainingFiles").send_keys(
            "/home/ximena/Documents/Repos/Proyecto-Aseguramiento-II-S-2017/"
            "WebServer/src/test/Muestras/s1/10.pgm")
        driver.find_element_by_id("trainingFiles").submit()
        driver.find_element_by_css_selector(
            "input.swal-content__input").clear()
        driver.find_element_by_css_selector(
            "input.swal-content__input").send_keys("7")
        driver.find_element_by_css_selector(
            "button.swal-button.swal-button--confirm").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                     'button.swal-button.'
                                                     'swal-button--confirm')))
        driver.find_element_by_css_selector(
            "button.swal-button.swal-button--confirm").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
