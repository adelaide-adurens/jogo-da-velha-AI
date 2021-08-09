import re

#Função exibeTabuleiro é chamada toda vez que se quer mostrar o tabuleiro e as posições já preenchidas ao usuário.
def exibeTabuleiro(tabuleiro):
    print(*tabuleiro[0][0],*tabuleiro[0][1], *tabuleiro[0][2])
    print(*tabuleiro[1][0],*tabuleiro[1][1], *tabuleiro[1][2])
    print(*tabuleiro[2][0],*tabuleiro[2][1], *tabuleiro[2][2], "\n")

#Função recebe a string da posição no tabuleiro e retorna somente o marcador do jogador para ser usado nas funções que verificam o resultado do jogo.
def remover(texto):
    charRemover = "[ |_]"
    elementNovo = re.sub(charRemover,'',texto)
    
    return elementNovo

#Funçao usada na jogada do computador para tentar vencer
def vencer(listaTabuleiro):

    #verificando linhas
    posicaoLinha = 0
    colunaVazia = 0 
    for element in listaTabuleiro: 
        x = 0
        vazio = False
        posicaoLinha +=1
        posicaoColuna = 0
        for item in element:
            posicaoColuna += 1
            if remover(item[0]) == 'X':
                x +=1
            elif remover(item[0]) == '':
                vazio = True
                colunaVazia = posicaoColuna
        if x == 2 and vazio == True:
            return [posicaoLinha, colunaVazia]
        
    #verificando colunas
    i = 0
    while i <= 2:
        vazio = False
        x = 0
        z = 0
        while z <= 2:
            item = listaTabuleiro[z][i][0]
            if remover(item) == 'X':
                x +=1
            elif remover(item) == '':
                vazio = True
                colunaVazia = i
                linhaVazia = z
            if x == 2 and vazio == True:
                return [(linhaVazia+1), (colunaVazia+1)]
            z +=1
        i+=1

    #verificando diagonais
    diagonal = [[[0,0], [1,1], [2,2]],[ [0,2], [1,1], [2,0]]]
    
    linhaVazia = 0
    colunaVazia = 0 
    for lista in diagonal:
        x = 0
        vazio = False
        for element in lista:
            linha = element[0]
            coluna = element[1]
            item = listaTabuleiro[linha][coluna][0]
            if remover (item) == 'X':
                x +=1
            elif remover(item) == '':
                vazio = True
                linhaVazia = linha
                colunaVazia = coluna
        if x == 2 and vazio == True:
            return [(linhaVazia+1), (colunaVazia+1)]
    return []

#Funçao usada quando se joga contra o computador que impede jogador de ganhar
def defesa (listaTabuleiro):
    
    x = 0
    vazio = False
    posicaoColuna = 0
    for item in listaTabuleiro[1]:
        posicaoColuna+=1
        if remover (item[0]) == 'O':
            x +=1
        elif remover(item[0]) == '':
            vazio = True
            colunaVazia = posicaoColuna
    if x == 2 and vazio == True:
            return [2, colunaVazia]
    return []

#Função para quando o jogo chega na última rodada e só resta um espaço pro computador
def ultimoEspaco(listaTabuleiro):
        
    posicaoLinha = 0
    for element in listaTabuleiro: 
        posicaoLinha +=1
        posicaoColuna = 0
        for item in element:
            posicaoColuna += 1
            if remover(item[0]) == '':
                return [posicaoLinha, posicaoColuna]   

# Função entradaValida recebe o input do usuário e verifica se está entre as opções válidas, retornando True ou False.
def entradaValida(entrada, listaTabuleiro):
    valido = True
    entradasValidas = ["1", "2", "3"]
    if entrada not in entradasValidas:
        valido = False
        print("Jogada Inválida.\n")
        exibeTabuleiro(listaTabuleiro)
        
    return valido  

# Função para determinar onde será a jogada do computador
def jogadaComputador(rodada, listaJogadas, listaTabuleiro):
    posicao = []
    if rodada == 1:
        posicao = [1,1]
    elif rodada == 3:
        posicaoBolinha = listaJogadas[1]
        if posicaoBolinha == [1,2] or posicaoBolinha == [1,3]:
            posicao = [2,1]
        elif posicaoBolinha == [2,1] or posicaoBolinha == [3,2]:
            posicao = [2,2]
        elif posicaoBolinha == [2,3] or posicaoBolinha ==[3,3] or posicaoBolinha == [2,2]:
            posicao = [1,3]
        elif posicaoBolinha == [3,1]:
            posicao = [1,2]
    elif rodada == 5:
        posicao = vencer(listaTabuleiro)
        if posicao != []:
            return posicao
        if listaJogadas[2] == [2,1] and listaTabuleiro[2][0] != ['  ']:
            posicao = [2,2]
        elif listaJogadas[1] == [2,1] and listaJogadas[2] == [2,2] and listaTabuleiro[2][2] != ['|   ']:
            posicao = [1,3]
        elif listaJogadas[1] == [3,2] and listaJogadas[2] == [2,2] and listaTabuleiro[2][2] != ['|   ']:
            posicao = [3,1]
        elif listaJogadas[2] == [1,3] and listaTabuleiro[0][1] != ['| __'] and listaTabuleiro [1][1] == ['| __']:
            posicao = [3,1]
        elif listaJogadas[2] == [1,3] and listaTabuleiro[0][1] != ['| __'] and listaTabuleiro [1][1] != ['| __']:
            posicao = [3,2]
        elif listaJogadas[2] == [1,2] and listaTabuleiro[0][2] != ['| __']:
            posicao = [2,2]
    elif rodada == 7:
        posicao = vencer(listaTabuleiro)
        if posicao != []:
            return posicao
        posicao = defesa(listaTabuleiro)
        if posicao != []:
            return posicao
        if listaJogadas[2] == [1,3] and listaJogadas[4] == [3,2] and listaTabuleiro[2][0]!=['  ']:
            posicao = [2,3]
        elif listaJogadas[2] == [1,3] and listaJogadas[4] == [3,2] and listaTabuleiro[2][2]!=['|   ']:
            posicao = [2,1]
    elif rodada == 9:
        posicao = ultimoEspaco(listaTabuleiro)
    return posicao 

#Função posicaoJogada perguntará a posição que o jogador quer colocar seu marcador. 
# Recebe o número da jogada e se será contra o computador e retorna a posição da mesma.
def posicaoJogada(n, modo, listaJogadas, listaTabuleiro):
    jogador = ''
    if n % 2 != 0:
        jogador = 'X'
    else:
        jogador = 'O'
    #a variável 'n' é usada para decidir se é o jogador 1 (X) ou jogador 2    
    jogada = [] 
        
    opcao = ['linha', 'coluna']

    if modo == '1' and jogador == 'X':
        jogada = jogadaComputador(n, listaJogadas, listaTabuleiro)
    else:
        while jogada in (listaJogadas) or jogada == []:

            n = 0
            while n <= 1:
                #nesse laço recebe-se a opção de posição do jogador e verifica-se se é válida com a Função entradaValida
                jogadaInvalida = False
                while jogadaInvalida == False:
                    jogadaOpcao = input(f"Em que {opcao[n]} você quer colocar seu {jogador}? Digite '1', '2' ou '3'.")    
                    jogadaInvalida = entradaValida(jogadaOpcao, listaTabuleiro)
                jogada.append(int(jogadaOpcao))
                n+=1
            #nesse if eu verifico se a opção de posição do jogador, apesar de válida, já não está ocupada
            if jogada in (listaJogadas):
                jogada = []
                print("Essa posição do tabuleiro já está ocupada. Por favor, tente outra jogada.\n")
                exibeTabuleiro(listaTabuleiro)
    listaJogadas.append(jogada)
        
    return jogada, listaJogadas

#Função recebe o número da jogada e as coordenadas de posição para poder retornar a alteração do tabuleiro com a jogada.
def tabuleiro (n, jogadaLinha, jogadaColuna, listaTabuleiro):    
    jogador = ''
    if n % 2 != 0:
        jogador = 'X'
    else:
        jogador = 'O'
    
    fim = '_'
    if jogadaLinha == 3:
        fim = ' '

    barra = '| '
    if jogadaColuna == 1:
        barra = ''

    listaTabuleiro[jogadaLinha-1][jogadaColuna-1] = [barra+jogador+fim]
    return listaTabuleiro

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas linhas dos tabuleiros.
def linhasIguais(tabuleiro, jogador):
    ganhou = False
    for element in tabuleiro:
        if remover(element[0][0]) == remover(element[1][0]) and remover(element[1][0]) == remover(element[2][0]) and remover(element[2][0]) == jogador:
            ganhou = True
    return ganhou

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas colunas dos tabuleiros.
def colunasIguais(tabuleiro, jogador):
    ganhou = False
    n = 0
    while n <= 2:
        if remover(tabuleiro[0][n][0]) == remover(tabuleiro[1][n][0]) and remover(tabuleiro[1][n][0]) == remover(tabuleiro[2][n][0]) and remover(tabuleiro[2][n][0]) == jogador:
            ganhou = True
        n+=1 
    return ganhou

#Função que recebe as posições do tabuleiro e o marcador para verificar vitórias nas diagonais dos tabuleiros.
def diagonal(tabuleiro, jogador):
    ganhou = False
    if remover(tabuleiro[0][0][0]) == remover(tabuleiro[1][1][0]) and remover(tabuleiro[1][1][0]) == remover(tabuleiro[2][2][0]) and remover(tabuleiro[2][2][0]) == jogador:
        ganhou = True
    elif remover(tabuleiro[0][2][0]) == remover(tabuleiro[1][1][0]) and remover(tabuleiro[1][1][0]) == remover(tabuleiro[2][0][0]) and remover(tabuleiro[2][0][0]) == jogador:
        ganhou = True
    return ganhou

#Recebe o número da jogada e utiliza outras funções para analisar o resultado do jogo a partir da 5ª jogada.
def vitoria(n,listaTabuleiro):
    acabou = False
    if n >=5:
        if linhasIguais(listaTabuleiro, 'X') or colunasIguais(listaTabuleiro, 'X') or diagonal(listaTabuleiro, 'X'):
            print("Parabéns o Jogador 1 ganhou!")
            acabou = True
        elif linhasIguais(listaTabuleiro, 'O') or colunasIguais(listaTabuleiro, 'O') or diagonal(listaTabuleiro, 'O'):
            print("Parabéns o Jogador 2 ganhou!") 
            acabou = True
        elif n == 9:
            print("Deu velha!")
    return acabou   

# Código principal

def __main__():

    listaTabuleiro = [
        [['__'],['| __'],['| __']],
        [['__'],['| __'],['| __']],
        [['  '],['|   '],['|   ']]
    ]

    listaJogadas = []
    exibeTabuleiro(listaTabuleiro)

    n=1
    #Menu para jogador decidir se quer jogar contra computador ou outro jogador
    opcao = 0
    print("Escolha uma das alternativas:")
    print("1 - Jogar contra o computador.")
    print("2 - Dois jogadores.")
    opcao = input ()

    while (opcao not in ['1','2']):
        print("Opção inválida.")
        print("Escolha uma das alternativas:")
        print("1 - Jogar contra o computador.")
        print("2 - Dois jogadores.")
        opcao = input ()

    #Laço que se repete por 9 vezes (número de jogadas possíveis) e chama as funções para posicionar as jogadas e verificar o resultado do jogo.
    while n < 10:
        posicaoTabuleiro, listaJogadas= posicaoJogada(n, opcao, listaJogadas, listaTabuleiro)
        tabuleiro(n,posicaoTabuleiro[0], posicaoTabuleiro[1], listaTabuleiro)
        exibeTabuleiro(listaTabuleiro)
        acabou = vitoria(n, listaTabuleiro)
        if acabou == True:
            break

        n +=1

if __name__ == "__main__":
    __main__()