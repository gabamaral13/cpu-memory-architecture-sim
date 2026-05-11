import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

tabelaMapeamento = []

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso da tecnica de mapeamento direto
def mapeamentoDireto(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global tabelaMapeamento

    paginaRequisitada = endereco >> 2
    byteRequisitado = endereco & 3

    #print("PAGINA REQUISITADA", paginaRequisitada)
    #print("BYTE REQUISITADO", byteRequisitado)
    #print("TABELA MAPEAMENTO", tabelaMapeamento)

    indiceTabelaMapeamento = paginaRequisitada % qtPaginasMemoriaPrincipal
    # pagina 3 <- 3
    # pagina 11 <- 3
    # verifica na tabela se ja mapeei a pagina
    if tabelaMapeamento[indiceTabelaMapeamento] == paginaRequisitada:
        # entao retorna o indice
        return indiceTabelaMapeamento
    # senao 
    else:
        # mapeia atualiza a tabela e retorna o indice
        paginaDestino = indiceTabelaMapeamento
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        memoriaPrincipal.setPagina(pagina, paginaDestino)
        
        tabelaMapeamento[indiceTabelaMapeamento] = paginaRequisitada

        #retorna endereco
        return indiceTabelaMapeamento


#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    global tabelaMapeamento
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas
    
    tabelaMapeamento = [-1] * qtPaginasMemoriaPrincipal

if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoDireto,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoDireto, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)