from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username #instanciando username
        self.password = password # instanciando password
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\user\Documents\jonny\Bot-redes\instagram\explorer.exe') #Passando local onde está o executal do webdriver


    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=pt-br') # site a ser acessado
        time.sleep(3) # esperando pagina carregar antes de continuar executando ações
        
        ''' Botão Conecte-se '''
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")# Achando botão "conecte-se"
        login_button.click() #Clicando no botão "conecte-se"

        ''' Campo do Usuario '''
        user_element = driver.find_element_by_xpath("//input[@name='username']") #Achando campo do usuario
        user_element.clear() #Limpando campo do usuario 
        user_element.send_keys(self.username) # Escrevendo nosso usuario
        
        ''' Campo para senha '''
        password_element = driver.find_element_by_xpath("//input[@name='password']") # Achando campo para senha
        password_element.clear() # Limpando campo da senha
        password_element.send_keys(self.password) # Enviando nossa senha
        
        '''Botão ENTRAR '''
        password_element.send_keys(Keys.RETURN) # Pegando o returno após ser inserido o usuario e a senha, que é o botão "ENTRAR"
        time.sleep(5)