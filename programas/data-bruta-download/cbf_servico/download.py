from selenium import webdriver
from pyvirtualdisplay import Display
from tqdm import tqdm

URL_CBF         = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"
ANO_INICIO      = 2020
ANO_FIM         = 2020

class CONTROLE_BIBLIOTECAS:
    @staticmethod
    def inicializar():
        display = Display(visible=1, size=(1024, 768))
        display.start()
        driver = webdriver.Firefox()
        return display, driver

    @staticmethod    
    def finalizar( display , driver ):
        if driver  != None: driver.close()
        if display != None: display.stop()



class DRIVER_CBF:
    @classmethod
    def __init__( self , driver:webdriver.Firefox ):
        self.driver = driver
        self.url = URL_CBF
    @classmethod
    def get_page( self , page ):
        url = f"{self.url}/{page}"

        self.driver.get( url )
        return str( self.driver.page_source )



class DOWNLOAD_DATA:
    def __init__( self , class_drive:DRIVER_CBF):
        self.classDrive = class_drive
        self.ANO_INICIO = ANO_INICIO
        self.ANO_FIM = ANO_FIM

    def get_paginas( self ):
        lista_retorno = list()
        for ano in tqdm( range( self.ANO_INICIO , self.ANO_FIM + 1) ):
            pagina = self.classDrive.get_page( ano )
            lista_retorno.append( pagina )
        return lista_retorno


def gerar_data()->list:
    display, driver = CONTROLE_BIBLIOTECAS.inicializar()

    driver_cbf = DRIVER_CBF( driver )
    downloadData = DOWNLOAD_DATA( driver_cbf )
    lista_retorno = downloadData.get_paginas()
    
    
    CONTROLE_BIBLIOTECAS.finalizar( display , driver )
    return lista_retorno


if __name__ == "__main__":
    gerar_data()
