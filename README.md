# Informe de Automatización de Pruebas Móviles con Appium

**Estudiante:** Cristian Eulises Sánchez Ramírez  
**Asignatura:** Calidad de Software / Automatización de Pruebas  
**Actividad:** Descubriendo la Automatización de Pruebas Móviles con Appium  
**Matricula:** 25-0688

---

## 🔧 Configuración del Entorno

Se llevó a cabo una configuración completa del entorno para pruebas con Appium en emulador Android. Los pasos principales fueron:

- Instalación de **Node.js** y Appium v2 con `npm install -g appium`.
- Verificación del entorno con `appium-doctor`, corrigiendo errores comunes como permisos `.npm`, variables `JAVA_HOME` y `ANDROID_HOME`.
- Instalación del **driver UiAutomator2** para Android:
  ```bash
  appium driver install uiautomator2
  ```
- Configuración del SDK de Android y emulador con Android 16 (API 36).
- Instalación de `Appium-Python-Client` y uso de `webdriver.Remote()`.

---

## 🔢 Pruebas Realizadas

Se realizaron pruebas prácticas sobre cuatro componentes principales, cada una representada en un archivo Python:

### 1. `test_chrome_basic.py`
- Abre Google Chrome en el emulador
- Salta la pantalla de bienvenida
- Navega automáticamente a `https://www.wikipedia.org`

### 2. `test_gestures_youtube.py`
- Abre la app de **YouTube**
- Realiza un gesto **swipe hacia arriba** simulando un scroll vertical

### 3. `test_unittest_example.py`
- Estructura la automatización en el framework `unittest`
- Incluye `setUp()` y `tearDown()` para iniciar y cerrar Appium
- Navega a Wikipedia y valida el flujo

### 4. `test_calc.py`
- Ejecuta una simulación en una app de calculadora (si está disponible)
- Realiza la operación 2 + 3 y lee el resultado

---

## 📊 Exploración de Conceptos Clave

### ✏️ Identificación de Elementos
Se aplicaron estrategias como:
- `find_element("id", "...")`
- `find_element("accessibility id", "...")`
- `Appium Inspector` para obtener IDs, content-descriptions, etc.

### 👉 Gestos y Eventos
- Se usó `driver.perform_actions()` para simular **tap** y **swipe** sin TouchAction (incompatible en v3+).

### 🛠️ Integración con Frameworks
- Se integró con `unittest` en Python, permitiendo organizar casos de prueba y generar reportes con `assert`, `setUp`, `tearDown`, etc.

### 📱 Dispositivos Reales
- Se trabajó inicialmente con emuladores, pero se dejó configurado el entorno para conectar dispositivos reales vía `adb` y `developer options`.

---

## 📈 Conclusiones

Durante esta actividad se profundizó en la automatización de pruebas para aplicaciones móviles:

- Se superaron problemas comunes como `unauthorized`, errores de adb, configuración de entorno y uso de drivers.
- Se utilizaron estrategias modernas con Appium 2 y Selenium 4, adaptando el código a nuevas APIs.
- Se automatizaron tareas realistas, replicando comportamientos de usuarios sobre apps instaladas en Android (YouTube, Chrome).

Este ejercicio no solo permitió desarrollar pruebas automatizadas, sino también fortalecer el dominio del ecosistema Appium y la adaptación a versiones modernas.

