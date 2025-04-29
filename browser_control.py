from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Kelias iki tavo ChromeDriver (jei jis nėra PATH)
service = Service("chromedriver.exe")  # arba "./chromedriver" Linux/Mac
driver = webdriver.Chrome(service=service)

# Atidarome svetainę
driver.get("https://delfi.lt")
driver.get("https://google.com")
# from google backs to delfi
driver.back()

# atnaujina puslapį (tarsi paspaustum F5)
driver.refresh()

# grąžina dabartinį adresą
print(driver.current_url)

# puslapio pavadinimas (title tag)
print(driver.title)

#Maksimaliai padidinti langą
driver.maximize_window()

# Nustato tikslų naršyklės dydį pagal plotį (px) ir aukštį (px).
# Gali naudoti get_window_size() – grąžina dabartinį dydį (plotį ir aukštį).
driver.set_window_size(1024, 768)

# Yra ir set_window_position(x, y) – jei reikia keisti naršyklės lango vietą ekrane.
driver.set_window_position(50,50)

# Narsykles veikimo laikas
time.sleep(20)
# Uždaryti naršyklę

driver.quit()
