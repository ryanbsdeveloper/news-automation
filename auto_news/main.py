from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os


class AutoWpp():
    def __init__(self):
        self._Userdata = os.path.abspath('User Data')  # caminho da pasta para abrir o navegador com perfil
        options = webdriver.ChromeOptions()
        options.add_argument(fr'user-data-dir={self._Userdata}')
        chrome_service = Service(executable_path=r'chromedriver.exe')
        self.chrome = webdriver.Chrome(service=chrome_service, options=options)
        self.chrome.implicitly_wait(20)  # espera os find_elements carregar para pegar o elemento, num tempo de 10s
        self.chrome.minimize_window()

    def get_a_news(self, noticia=None):
        self.chrome.get('https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419')
        search = self.chrome.find_element(By.XPATH,
                                          '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
        search.send_keys(noticia)
        search.send_keys(Keys.ENTER)

        try:
            try:
                first = self.chrome.find_element(By.XPATH,
                                                 '/html/body/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div/article/a')
            except:
                first = self.chrome.find_element(By.XPATH,
                                                 '/html/body/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/div/div/a')
        except:
            print(f'Nenhuma noticia relacionada a: {noticia}')
            self._fechar()
        else:
            link = first.get_attribute('href')
            return link

    def open_wpp(self, contato, link, noticia=''):
        self.chrome.get('https://web.whatsapp.com/')
        search = self.chrome.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')
        search.send_keys('Ryan')
        search.send_keys(Keys.ENTER)
        sleep(0.7)

        send_msg = self.chrome.find_element(By.XPATH,
                                            '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        send_msg.send_keys(
            f'Olá *{contato.capitalize()}*, Acesse a *principal* noticia sobre *{noticia.capitalize()}*: {link}')
        send_msg.send_keys(Keys.ENTER)
        self._fechar()

    def _fechar(self):
        self.chrome.close()



if __name__ == '__main__':
    # noticia = input('Sobre qual noticia gostaria de receber? ')
    # contato = input('Para qual contato enviar a noticia? ')
    # print('Aguarde...')
    app = AutoWpp()
    # link_news = app.get_a_news(noticia)
    # app.open_wpp(contato, link_news, noticia=noticia)
    # print(f'\033[1;32mPrincipal Noticia sobre \033[;1m{noticia}\033[1;32m enviada\033[m')
