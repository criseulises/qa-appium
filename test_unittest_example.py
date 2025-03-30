import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

class ChromeWikipediaTest(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "16"
        options.device_name = "emulator-5554"
        options.automation_name = "UiAutomator2"
        options.app_package = "com.android.chrome"
        options.app_activity = "com.google.android.apps.chrome.Main"
        options.no_reset = True

        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        self.driver.implicitly_wait(5)

        # Omitir pantalla de bienvenida si aparece
        try:
            self.driver.find_element("id", "com.android.chrome:id/terms_accept").click()
            self.driver.find_element("id", "com.android.chrome:id/negative_button").click()
        except:
            pass

    def test_navegar_a_wikipedia(self):
        try:
            self.driver.find_element("id", "com.android.chrome:id/search_box_text").click()
            url_input = self.driver.find_element("id", "com.android.chrome:id/url_bar")
            url_input.send_keys("https://www.wikipedia.org\n")
            print("✔ Navegación a Wikipedia completada")
            time.sleep(3)
        except Exception as e:
            self.fail(f"No se pudo navegar: {e}")

    def tearDown(self):
        self.driver.quit()
        print("🚀 Prueba con unittest finalizada")

if __name__ == "__main__":
    unittest.main()
