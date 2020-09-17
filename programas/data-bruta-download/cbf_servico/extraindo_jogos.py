from bs4 import BeautifulSoup
import re
import json

_JOGOS___ = "jogos"
_RODADAS_ = "rodadas"
_TIMES___ = "times"
_ANO_____ = "ano"
_DATA_H_ = "data-hora"
_TIME_C_ = "time-casa"
_TIME_F_ = "time-fora"


#def get_jogos( page:str ):
    
def extrair( page: str ):
    soup = BeautifulSoup( page , "lxml" )
    out = dict()
    out[_RODADAS_] = set()
    out[_JOGOS___] = list()
    out[_TIMES___] = set()
    out[_ANO_____] = EXTRAIR.ano( soup)
    soup_base = PERCORE.rodadas( soup )
    for soup_rodada in PERCORE.rodada( soup ):
        rodada = EXTRAIR.rodada_str( soup_rodada )
        out[_RODADAS_].add( rodada )
        
        for soup_jogo in PERCORE.jogos():
            out_informacoes_jogo = dict()
            out_informacoes_jogo[_DATA_H_] = EXTRAIR.data_hora( soup_jogo )
            
            for i , soup_time in enumerate( PERCORE.time( soup_jogo ) ):
                if   i == 0: out_informacoes_jogo[_TIME_C_] = EXTRAIR.time_sigla( soup_time)
                elif i == 1: out_informacoes_jogo[_TIME_F_] = EXTRAIR.time_sigla( soup_time)
            out_informacoes_jogo[_ANO_____] = out[_ANO_____]

            out[_TIMES___].add( out_informacoes_jogo[_TIME_C_] )
            out[_TIMES___].add( out_informacoes_jogo[_TIME_F_] )
            
            out[_JOGOS___].append( out_informacoes_jogo)
    
    out[_RODADAS_] = list( out[_RODADAS_]  )
    out[_TIMES___] = list( out[_TIMES___]  )

    print( json.dumps (out) )

class PERCORE:
    @staticmethod
    def rodadas( soup:BeautifulSoup):
        return soup.find("aside" , class_ = "aside-rodadas")
    
    @staticmethod
    def rodada( soup_base:BeautifulSoup):
        return soup_base.find_all("div" , class_ = "swiper-slide")

    @staticmethod
    def jogos(soup_rodadas:BeautifulSoup):
        return soup_rodadas.find("ul").find_all("li")
    
    @staticmethod
    def time( soup_jogos:BeautifulSoup ):
        return soup_jogos.find("div" , class_ = "clearfix").find_all("div", class_ = "time" )
    
class EXTRAIR:
    @staticmethod
    def rodada_str(soup_rodadas:BeautifulSoup):
        return soup_rodadas.find("header").find("h3").string

    @staticmethod
    def data_hora( soup_jogo:BeautifulSoup ):
        var = soup_jogo.find( "span" , class_ ="partida-desc").text
        var = re.split(r'[\n]+' , var )
        for ele in var:
            if ele != '':
                return re.sub(r'[ ]+' , ' ' , ele )
        return var 
    
    @staticmethod
    def time_sigla( soup_time:BeautifulSoup ):
        return soup_time.find("span" , class_="time-sigla").text

    def ano( soup:BeautifulSoup ):
        var = soup.find('article',class_ = 'campeonato').find("div" , class_ = 'container').find("header",class_="m-t-15").find("h2").text
        var = re.findall("[0-9]{4}" , var )
        if len( var ) > 0:
            return var[ 0 ]
        return ''

