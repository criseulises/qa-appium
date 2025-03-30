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

print("Iniciando sesión con Appium...")
driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(2)  

try:
    driver.find_element("id", "com.android.chrome:id/terms_accept").click()
    time.sleep(1)
    driver.find_element("id", "com.android.chrome:id/negative_button").click()
    print("Pantalla de bienvenida de Chrome omitida.")
except:
    print("No se mostró pantalla de bienvenida.")

# Abrir Wikipedia
try:
    driver.find_element("id", "com.android.chrome:id/search_box_text").click()
    time.sleep(1)
    url_input = driver.find_element("id", "com.android.chrome:id/url_bar")
    url_input.send_keys("https://www.wikipedia.org\n")
    print("Se abrió Wikipedia en Chrome.")
except:
    print("No se pudo encontrar el campo de búsqueda de Chrome.")

time.sleep(5)
driver.quit()
print("Prueba finalizada.")
