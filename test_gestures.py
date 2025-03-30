from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "16"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.google.android.youtube"
options.app_activity = "com.google.android.apps.youtube.app.WatchWhileActivity"
options.no_reset = True

print("Iniciando prueba de gestos en YouTube...")
driver = webdriver.Remote("http://localhost:4723", options=options)

time.sleep(5)  # Dar tiempo a que YouTube se abra completamente

# Hacer swipe hacia arriba (scroll en los videos)
try:
    driver.perform_actions([{
        "type": "pointer",
        "id": "finger1",
        "parameters": {"pointerType": "touch"},
        "actions": [
            {"type": "pointerMove", "duration": 0, "x": 300, "y": 1000},
            {"type": "pointerDown", "button": 0},
            {"type": "pointerMove", "duration": 800, "x": 300, "y": 300},
            {"type": "pointerUp", "button": 0}
        ]
    }])
    print("✔ Swipe hacia arriba ejecutado en YouTube.")
except Exception as e:
    print("")

time.sleep(3)
driver.quit()
print("🚀 Prueba de gestos en YouTube finalizada.")