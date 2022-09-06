import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings('ignore')
import time


def extraer_tabla(driver):
    tabla=driver.find_element(By.TAG_NAME, 'tbody')
    filas=tabla.find_elements(By.TAG_NAME,'tr')
    datos=[]
    for f in filas:
        elementos=f.find_elements(By.TAG_NAME,'td')
        tmp=[]
        for e in elementos: 
            tmp.append(e.text) 
        datos.append(tmp)
    return datos