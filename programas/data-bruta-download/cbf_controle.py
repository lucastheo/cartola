from cbf_servico.download import gerar_data
from cbf_servico.extraindo_jogos import extrair
if __name__ == "__main__":
    with  open( "saida.teste" , "r" ) as arq:
       s = arq.read()\
    extrair( s )
    
    

