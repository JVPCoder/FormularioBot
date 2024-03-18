from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="A:\Coding\Codes\Python\Sele\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://jvpcoder.github.io/Projeto-Portifolio/")

driver.execute_script("window.scrollTo(0, 4508)")

time.sleep(2)

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "nome"))
 )

input_element = driver.find_element(By.ID, "nome")
input_element.clear()
input_element.send_keys("John")

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "sobrenome"))
 )

input_element = driver.find_element(By.ID, "sobrenome")
input_element.clear()
input_element.send_keys("Doe")

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "email"))
 )

input_element = driver.find_element(By.ID, "email")
input_element.clear()
input_element.send_keys("john_doe@gmail.com")

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "telefone"))
 )

input_element = driver.find_element(By.ID, "telefone")
input_element.clear()

telefone = ["1","3","9","9","6","5","3","8","4","3","8"]

for numero in telefone:
 input_element.send_keys(numero)

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.ID, "mensagem"))
 )

input_element = driver.find_element(By.ID, "mensagem")
input_element.clear()
input_element.send_keys("Gostaria de entrar em contato.")

# WebDriverWait(driver,5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "joao-vitor"))
# )

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "joao-vitor")
# link.click()

WebDriverWait(driver,5).until(
     EC.presence_of_element_located((By.CLASS_NAME, "btn-form-send"))
 )

botao = driver.find_element(By.CLASS_NAME, "btn-form-send")
botao.click()

time.sleep(5)

driver.quit()
