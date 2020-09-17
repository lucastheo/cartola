from .cbf_servico.download import gerar_data
from .cbf_servico.extraindo_jogos import extrair


def exec():
    with  open( "./programas/data_bruta_download/saida.teste" , "r" ) as arq:
       s = arq.read()
    extrair( s )
    
    

