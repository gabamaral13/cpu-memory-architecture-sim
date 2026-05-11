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
# Altere a funcao para fazer uso da tecnica de mapeamento associativo
def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global tabelaMapeamento

    paginaRequisitada = endereco >> 2

    indiceEncontrado = -1
    for i in range(qtPaginasMemoriaPrincipal):
        if tabelaMapeamento[i] == paginaRequisitada:
            indiceEncontrado = i
            break

    if indiceEncontrado != -1:
        return indiceEncontrado
    else:
        indiceLivre = -1
        for i in range(qtPaginasMemoriaPrincipal):
            if tabelaMapeamento[i] == -1:
                indiceLivre = i
                break
                
        if indiceLivre == -1:
            indiceLivre = random.randint(0, qtPaginasMemoriaPrincipal - 1)

        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        memoriaPrincipal.setPagina(pagina, indiceLivre)
        
        tabelaMapeamento[indiceLivre] = paginaRequisitada

        #retorna endereco
        return indiceLivre

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
                               funcaoMapeamento=mapeamentoAssociativo,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativo, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)