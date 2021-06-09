from Serviço import criar_matriz
from Apresentação import jogo_da_velha, escrever_posicao, condicional

def main():
    """ Função principal: Jogo da Velha """

    matriz = criar_matriz()
    decisao =jogo_da_velha(matriz)
    if condicional(decisao):
        main()

if __name__ == '__main__':
    main()
 
