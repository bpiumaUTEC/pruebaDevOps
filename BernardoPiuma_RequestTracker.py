import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Ingresamos al servidor (en mi caso en una máquina virtual)
driver.get("http://192.168.70.114:8107/")

#Ingresamos el usuario
elemento1 = driver.find_element(By.NAME, "user")
elemento1.clear()
elemento1.send_keys("root")

#Ingresamos la clave
elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")

#Clickeamos en el botón Entrar
driver.find_element(By.CLASS_NAME, "btn").click()

#Refrescamos la página
driver.get("http://192.168.70.114:8107/")

#Ingresamos el asunto
elemento3 = driver.find_element(By.NAME, "Subject")
elemento3.clear()
elemento3.send_keys("Asunto de prueba")

#Ingresamos el contenido
elemento4 = driver.find_element(By.NAME, "Content")
elemento4.clear()
elemento4.send_keys("Contenido de prueba")

#Clickeamos en el botón Crear
driver.find_element(By.NAME, "SubmitTicket").click()

time.sleep(20)

driver.close()