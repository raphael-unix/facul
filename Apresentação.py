from Serviço import validacao

def jogo_da_velha(matriz: list) -> bool:
        """ Função que executa o jogo recebendo sua dimenção. Retorna a decisão do pós jogo. """

        jogador = 0
        
        while((validacao(matriz) != '1') and (validacao(matriz) != '2')
        and ( validacao(matriz) == True)):

                jogador += 1
                imprimir_dimensao(matriz)
                escrever_posicao(matriz, jogador)
        
        imprimir_dimensao(matriz)

        decisao = validacao(matriz)

        return decisao
        

def condicional(decisao: bool)-> bool:
        """ Função que recebe a decisão da função jogo da velha e informa quem ganhou ou se empatou. Dependendo da interação com
        o usúario o retorno será True caoso o usuário decidir continuar jogando ou False caso ele deseje encerrar.
        bool -> bool """

        if decisao == '1':
                SN = str.lower(input('\nO jogador 1 Venceu! Deseja jogar novamente novamente?(S/N)\n\n'))
                
        elif decisao == '2':
                SN = str.lower(input('\nO jogador 2 Venceu! Deseja jogar novamente?(S/N)\n\n'))

        else:
                SN = str.lower(input('\nEmpate! Quem diria!? Deseja jogar novamente?(S/N)\n\n'))


        while ((len(SN) != 1) and (SN != 's') and (SN != 'n')):
                SN = str.lower(input('\nComando invalido!! Siga nossa formatação exigida:[S/N] \n\nDeseja jogar novamente novamente(S/N)?\n\n'))

        if SN == 's':
                return True

        elif SN == 'n':
                print('\nQue pena.. volte sempre!! ',' Fim de jogo',sep='-')
                return False


def escrever_posicao(matriz: list,jogador: int):
        """ Função que interage com o usúario pedindo para cada jogador informar a posição
        desejado, um de cada vez.
        list(list) -> None """

        intervalo_texto = '0123'

        i_t = intervalo_texto

        if jogador%2 != 0:

                posicao = input("\nJogador 1 - escolha uma posição [x,y]:\n\n")

                while ((len(posicao) != 5) or (posicao[1] not in i_t) or (posicao[3] not in i_t ) or
                       (int(posicao[1]) not in range(4)) or (int(posicao[3]) not in range(4)) or (posicao[0] != '[') or
                       (posicao[2] != ',') or (posicao[4] != ']')):
                        posicao = input("\nPosição invalida! - Siga a formatação exigida -> [x,y]:\n\n")

                i = int(posicao[1])
                j = int(posicao[3])
    
                while (matriz[i][j] == 'O') or (matriz[i][j] == 'X' ):

                        posicao = input("\nPosição já marcada! - Escolha outra posição -> [x,y]:\n\n")

                        while ((len(posicao) != 5) or (posicao[1] not in i_t) or (posicao[3] not in i_t ) or
                               (int(posicao[1]) not in range(4)) or (int(posicao[3]) not in range(4)) or
                               (posicao[0] != '[') or (posicao[2] != ',') or (posicao[4] != ']')):

                                posicao = input("\nPosição invalida! - Siga a formatação exigida -> [x,y]:\n\n")

                        i = int(posicao[1])
                        j = int(posicao[3])
            
                matriz[i][j] = 'X'
                jogador += 1

        elif jogador%2 == 0:

                posicao = input("\nJogador 2 - escolha uma posição -> [x,y]:\n\n")

                while ((len(posicao) != 5) or (posicao[1] not in i_t) or (posicao[3] not in i_t ) or
                       (int(posicao[1]) not in range(4)) or (int(posicao[3]) not in range(4)) or
                       (posicao[0] != '[') or (posicao[2] != ',') or (posicao[4] != ']')):

                        posicao = input("\nPosição invalida! - Siga a formatação exigida -> [x,y]:\n\n")

                i = int(posicao[1])
                j = int(posicao[3])
    
                while ((matriz[i][j] == 'O') or (matriz[i][j] == 'X' )):

                        posicao = input("\nPosição já marcada! - Escolha outra posição -> [x,y]:\n\n")

                        while ((len(posicao) != 5) or (posicao[1] not in i_t) or (posicao[3] not in i_t ) or
                               (posicao[0] != '[') or (posicao[2] != ',') or (posicao[4] != ']') or
                               (int(posicao[1]) not in range(4)) or (int(posicao[3]) not in range(4))) :

                                posicao = input("\nPosição invalida! - Siga a formatação exigida -> [x,y]:\n\n")

                        i = int(posicao[1])
                        j = int(posicao[3])
            
                matriz[i][j] = 'O'
                jogador += 1


def imprimir_dimensao(matriz: list):
        """ Função que imprime uma matriz4x4 para o úsuario com uma dimensão correspondente
        para ser usada no jogo da velha.
        list -> None """
        print('\n#JOGO DA VELHA#\n')
        for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                        if j!=3:
                                print(2*'',matriz[i][j],sep=' ',end=' ')
                        elif j==3:
                                print(2*'',matriz[i][j],sep=' ',end='\n')

