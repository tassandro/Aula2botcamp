!pip install webdriver-manager
!pip install selenium
!pip install html5lib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
url = "https://www.etf.com/etfanalytics/etf-finder"
driver.get(url)
time.sleep(5)

botao_100 = driver.find_element("xpath", '''html/body/div[5]/section/div/div[3]/section/div
                                                /div/div/div/div[2]/
                                section[2]/div[2]/section[2]/div[1]/div/div[4]/button/label/span''')

driver.execute_script("arguments[0].click();", botao_100)
numero_paginas = driver.find_element("xpath", "html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/section[2]/div[2]/div/label[2]")
numero_paginas = numero_paginas.text.replace("of", "")
numero_paginas = int(numero_paginas)
print(numero_paginas)
lista_de_tabela_por_pagina = []

for pagina in range(0, numero_paginas):
    tabela = driver.find_element("xpath", "html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/div/table")

    html_tabela = tabela.get_attribute("outerHTML")

    tabela_final = pd.read_html(html_tabela)[0]

    lista_de_tabela_por_pagina.append(tabela_final)
    
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="nextPage"]')
    
    driver.execute_script("arguments[0].click();", botao_avancar_pagina)
    
base_de_dados_completa = pd.concat(lista_de_tabela_por_pagina)

display(base_de_dados_completa)
botao_aba = driver.find_element("xpath", "html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/ul/li[2]/span")
driver.execute_script("arguments[0].click();", botao_aba) #mudando a aba

for pagina in range(0, numero_paginas):
    
    botao_voltar_pagina = driver.find_element("xpath", '//*[@id="previousPage"]')
    
    driver.execute_script("arguments[0].click();", botao_voltar_pagina)
    
lista_de_tabela_por_pagina = []

for pagina in range(0, numero_paginas):
    tabela = driver.find_element("xpath", "html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/div/table")

    html_tabela = tabela.get_attribute("outerHTML")

    tabela_final = pd.read_html(html_tabela)[0]

    lista_de_tabela_por_pagina.append(tabela_final)
    
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="nextPage"]')
    
    driver.execute_script("arguments[0].click();", botao_avancar_pagina)
    
base_de_dados_performance = pd.concat(lista_de_tabela_por_pagina)

display(base_de_dados_performance)
