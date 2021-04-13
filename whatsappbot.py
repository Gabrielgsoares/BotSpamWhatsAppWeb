# Bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Entrar no WhatsappWeb
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10) # tempo para entrar com o QR CODE no WhatsappWeb

# Definir contatos ou grupos e mensagem que vai ser enviada
contatos=['Nome do contato ou grupo que a mensagem vai ser enviada']
mensagem='Mensagem que você quer enviar'

# Buscar contatos ou grupos
def buscar_contato(contato):
    campo_pesquisa=driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')# campo_de_pesquisa:'copyable-text selectable-text' 
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

# Enviar mensagens para o contato ou grupo
def enviar_mensagem(mensagem):
    for n in range(0,10): # repetição (caso não deseja essa repetição é só excluir a linha)
        campo_mensagem=driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')# campo_de_mensagem_privada:'copyable-text selectable-text'
        time.sleep(4)
        campo_mensagem[1].click()
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

