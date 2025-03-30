from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "16"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"
options.no_reset = True

driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(2)

try:
    driver.find_element("id", "com.android.chrome:id/terms_accept").click()
    time.sleep(1)
    driver.find_element("id", "com.android.chrome:id/negative_button").click()
except:
    print("Pantalla de bienvenida no detectada.")

try:
    driver.find_element("id", "com.android.chrome:id/search_box_text").click()
    time.sleep(1)
    url_input = driver.find_element("id", "com.android.chrome:id/url_bar")
    url_input.send_keys("https://www.wikipedia.org\n")
    print("Se abrió Wikipedia en Chrome.")
except:
    print("No se pudo encontrar el campo de búsqueda.")

time.sleep(5)
driver.quit()