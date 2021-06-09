def criar_matriz() -> list:
    """ Função que cria uma matriz 4x4 ultilizada para implementar
    no jogo da velha.
    None -> List """

    matriz = []
    
    for i in range(4):
        linha_da_matriz = []

        for j in range(4):
            linha_da_matriz.append('-')

        matriz.append(linha_da_matriz)
        
    return matriz        

def validacao(matriz: list)-> str or bool :
    """ Função que verifica uma possivel vitória ou empate.
    list-> str or bool """

    validacao = []
    empate = []

    if ((matriz[0][0] == matriz[0][1] == matriz[1][0] == matriz[1][1] == 'X')or
        (matriz[0][1] == matriz[0][2] == matriz[1][1] == matriz[1][2] == 'X')or
        (matriz[0][2] == matriz[0][3] == matriz[1][2] == matriz[1][3] == 'X')or
        (matriz[1][0] == matriz[1][1] == matriz[2][0] == matriz[2][1] == 'X')or
        (matriz[1][1] == matriz[1][2] == matriz[2][1] == matriz[2][2] == 'X')or
        (matriz[1][2] == matriz[1][3] == matriz[2][2] == matriz[2][3] == 'X')or
        (matriz[2][0] == matriz[2][1] == matriz[3][0] == matriz[3][1] == 'X')or
        (matriz[2][1] == matriz[2][2] == matriz[3][1] == matriz[3][2] == 'X')or
        (matriz[2][2] == matriz[2][3] == matriz[3][2] == matriz[3][3] == 'X')or
        (matriz[0][0] == matriz[0][1] == matriz[0][2] == matriz[0][3] == 'X')or
        (matriz[1][0] == matriz[1][1] == matriz[1][2] == matriz[1][3] == 'X')or
        (matriz[2][0] == matriz[2][1] == matriz[2][2] == matriz[2][3] == 'X')or
        (matriz[3][0] == matriz[3][1] == matriz[3][2] == matriz[3][3] == 'X')or
        (matriz[0][0] == matriz[1][0] == matriz[2][0] == matriz[3][0] == 'X')or
        (matriz[0][1] == matriz[1][1] == matriz[2][1] == matriz[3][1] == 'X')or
        (matriz[0][2] == matriz[1][2] == matriz[2][2] == matriz[3][2] == 'X')or
        (matriz[0][3] == matriz[1][3] == matriz[2][3] == matriz[3][3] == 'X')or
        (matriz[0][0] == matriz[1][1] == matriz[2][2] == matriz[3][3] == 'X')or
        (matriz[0][3] == matriz[1][2] == matriz[2][1] == matriz[3][0] == 'X')):
        validacao.append('1')



    elif ((matriz[0][0] == matriz[0][1] == matriz[1][0] == matriz[1][1] == 'O')or
          (matriz[0][1] == matriz[0][2] == matriz[1][1] == matriz[1][2] == 'O')or
          (matriz[0][2] == matriz[0][3] == matriz[1][2] == matriz[1][3] == 'O')or
          (matriz[1][0] == matriz[1][1] == matriz[2][0] == matriz[2][1] == 'O')or
          (matriz[1][1] == matriz[1][2] == matriz[2][1] == matriz[2][2] == 'O')or
          (matriz[1][2] == matriz[1][3] == matriz[2][2] == matriz[2][3] == 'O')or
          (matriz[2][0] == matriz[2][1] == matriz[3][0] == matriz[3][1] == 'O')or
          (matriz[2][1] == matriz[2][2] == matriz[3][1] == matriz[3][2] == 'O')or
          (matriz[2][2] == matriz[2][3] == matriz[3][2] == matriz[3][3] == 'O')or
          (matriz[0][0] == matriz[0][1] == matriz[0][2] == matriz[0][3] == 'O')or
          (matriz[1][0] == matriz[1][1] == matriz[1][2] == matriz[1][3] == 'O')or
          (matriz[2][0] == matriz[2][1] == matriz[2][2] == matriz[2][3] == 'O')or
          (matriz[3][0] == matriz[3][1] == matriz[3][2] == matriz[3][3] == 'O')or
          (matriz[0][0] == matriz[1][0] == matriz[2][0] == matriz[3][0] == 'O')or
          (matriz[0][1] == matriz[1][1] == matriz[2][1] == matriz[3][1] == 'O')or
          (matriz[0][2] == matriz[1][2] == matriz[2][2] == matriz[3][2] == 'O')or
          (matriz[0][3] == matriz[1][3] == matriz[2][3] == matriz[3][3] == 'O')or
          (matriz[0][0] == matriz[1][1] == matriz[2][2] == matriz[3][3] == 'O')or
          (matriz[0][3] == matriz[1][2] == matriz[2][1] == matriz[3][0] == 'O')):
        validacao.append('2')

    for i in range(len(matriz)):
        if '-' in matriz[i]:
            empate.append(False)
       
    if '1' in validacao:
        return '1'

    elif '2' in validacao:
        return '2'
    else:
        return False in empate

def funcao_teste():
    return (criar_matriz() == [['-']*4,['-']*4,['-']*4,['-']*4],
            criar_matriz() != [['-']*4,['-']*4,['-']*3,['-']*4],
            criar_matriz() != [['=']*4,['-']*4,['-']*4,['-']*4],
            validacao(criar_matriz()) == True,
            validacao([['O','O','X','O'],['O','X','O','X'],['X','O','X','O'],['X','X','O','X']]) == False,
            validacao([['X','X','-','-'],['X','X','-','-'],['-','-','-','-'],['-','-','-','-']]) == '1',
	          validacao([['-','X','X','-'],['-','X','X','-'],['-','-','-','-'],['-','-','-','-']]) == '1',
	          validacao([['-','-','X','X'],['-','-','X','X'],['-','-','-','-'],['-','-','-','-']]) == '1',
            validacao([['-','-','-','-'],['X','X','-','-'],['X','X','-','-'],['-','-','-','-']]) == '1',
            validacao([['-','-','-','-'],['-','X','X','-'],['-','X','X','-'],['-','-','-','-']]) == '1',
            validacao([['-','-','-','-'],['-','-','X','X'],['-','-','X','X'],['-','-','-','-']]) == '1',
            validacao([['-','-','-','-'],['-','-','-','-'],['X','X','-','-'],['X','X','-','-']]) == '1',
            validacao([['-','-','-','-'],['-','-','-','-'],['-','X','X','-'],['-','X','X','-']]) == '1',
            validacao([['-','-','-','-'],['-','-','-','-'],['-','-','X','X'],['-','-','X','X']]) == '1',
            validacao([['X','X','X','X'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]) == '1',
	          validacao([['-','-','-','-'],['X','X','X','X'],['-','-','-','-'],['-','-','-','-']]) == '1',
            validacao([['X','-','-','-'],['-','X','-','-'],['X','X','X','X'],['-','-','-','-']]) == '1',	
            validacao([['X','-','-','-'],['-','X','-','-'],['-','-','-','-'],['X','X','X','X']]) == '1',
            validacao([['X','-','-','-'],['X','-','-','-'],['X','-','-','-'],['X','-','-','-']]) == '1',
            validacao([['-','X','-','-'],['-','X','-','-'],['-','X','-','-'],['-','X','-','-']]) == '1',
            validacao([['-','-','X','-'],['-','-','X','-'],['-','-','X','-'],['-','-','X','-']]) == '1',
            validacao([['-','-','-','X'],['-','-','-','X'],['-','-','-','X'],['-','-','-','X']]) == '1',
            validacao([['X','-','-','-'],['-','X','-','-'],['-','-','X','-'],['-','-','-','X']]) == '1',
            validacao([['-','-','-','X'],['-','-','X','-'],['-','X','-','-'],['X','-','-','-']]) == '1',
            validacao([['O','O','-','-'],['O','O','-','-'],['-','-','-','-'],['-','-','-','-']]) == '2',
            validacao([['-','O','O','-'],['-','O','O','-'],['-','-','-','-'],['-','-','-','-']]) == '2',
            validacao([['-','-','O','O'],['-','-','O','O'],['-','-','-','-'],['-','-','-','-']]) == '2',
            validacao([['-','-','-','-'],['O','O','-','-'],['O','O','-','-'],['-','-','-','-']]) == '2',
            validacao([['-','-','-','-'],['-','O','O','-'],['-','O','O','-'],['-','-','-','-']]) == '2',
            validacao([['-','-','-','-'],['-','-','O','O'],['-','-','O','O'],['-','-','-','-']]) == '2',
            validacao([['-','-','-','-'],['-','-','-','-'],['O','O','-','-'],['O','O','-','-']]) == '2',
            validacao([['-','-','-','-'],['-','-','-','-'],['-','O','O','-'],['-','O','O','-']]) == '2',
	          validacao([['-','-','-','-'],['-','-','-','-'],['-','-','O','O'],['-','-','O','O']]) == '2',
            validacao([['O','O','O','O'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]) == '2',
	          validacao([['-','-','-','-'],['O','O','O','O'],['-','-','-','-'],['-','-','-','-']]) == '2',
            validacao([['O','-','-','-'],['-','O','-','-'],['O','O','O','O'],['-','-','-','-']]) == '2',	
            validacao([['O','-','-','-'],['-','O','-','-'],['-','-','-','-'],['O','O','O','O']]) == '2',
            validacao([['O','-','-','-'],['O','-','-','-'],['O','-','-','-'],['O','-','-','-']]) == '2',
            validacao([['-','O','-','-'],['-','O','-','-'],['-','O','-','-'],['-','O','-','-']]) == '2',
            validacao([['-','-','O','-'],['-','-','O','-'],['-','-','O','-'],['-','-','O','-']]) == '2',
            validacao([['-','-','-','O'],['-','-','-','O'],['-','-','-','O'],['-','-','-','O']]) == '2',
            validacao([['O','-','-','-'],['-','O','-','-'],['-','-','O','-'],['-','-','-','O']]) == '2',
            validacao([['-','-','-','O'],['-','-','O','-'],['-','O','-','-'],['O','-','-','-']]) == '2')
