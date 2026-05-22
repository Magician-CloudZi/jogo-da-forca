import os
from time import sleep

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Boneco ilustrativo
def desenhar_boneco(tentativas):
    boneco = [
        "  _____",
        " |     |",
        " |     " + ("O" if tentativas < 6 else " "),
        " |    " + ("/" if tentativas < 5 else " ") + ("|" if tentativas < 4 else " ") + ("\\" if tentativas < 3 else " "),
        " |    " + ("/" if tentativas < 2 else " ") + (" \\" if tentativas < 1 else " "),
        "_|_"
    ]

    for linha in boneco:
        print(linha)

# Função para exibir o painel, atualizando conforme entrada de letras pelo input
def mostrar_painel():
    #limpar_tela()
    lugar_letra_correta = [letra.upper() for letra in lugar_para_encontrar]
    print(f'Você tem {tentativas} chance{"s" if tentativas != 1 else ""} para acertar a palavra! \U0001f6a8\n')
    print(" ".join(lugar_letra_correta))
    desenhar_boneco(tentativas)

    if len(lista_errada) != 0:
        print('\n\n\u274C Letras erradas: ' + ' - '.join(letra.upper() for letra in lista_errada))

nome_usuario = input('Olá, qual é o seu nome? ')
#limpar_tela()
print(f'\nOlá, {nome_usuario.title()}! Seja Bem-vinda(o) ao Jogo da Forca! \U0001f609\n\n')

#--------------------------------Loop principal do jogo--------------------------------------
while True:
    palavra_escolhida = "alemão"
    numero_letras = len(palavra_escolhida)
    palavra_escondida = ["_" for _ in range(numero_letras)]
    lista_correta = []
    lista_errada = []
    tentativas = 6

    print(f'Sua palavra tem {numero_letras} letras! \U0001f4a1\n')
    siga = input('\nPressione Enter para iniciar o jogo ...')

    while 0 <= tentativas and palavra_escondida != list(palavra_escolhida):

        while True:

            mostrar_painel()

            letra_escolhida = str(input('\n\U0001f449 Escolha uma letra: ').lower())
            if len(letra_escolhida) == 1:
                break
            else:
                print('\nEscolha apenas 1 letra por vez! \u26A0\uFE0F')
                sleep(2)
                limpar_tela()

        if letra_escolhida in lugar_para_encontrar or letra_escolhida in lista_errada:
            print('\nVocê já escolheu esta letra antes! \u26A0\uFE0F')
            sleep(2)
            continue

        elif letra_escolhida in palavra_escolhida:
            print('\nWoow! Essa letra existe na sua palavra! \U0001f64c')
            sleep(2)
            lista_correta.append(letra_escolhida)
            indices = [i for i, letra in enumerate(palavra_escolhida) if letra == letra_escolhida]
            for indice in indices:
                lugar_para_encontrar[indice] = letra_escolhida
        else:
            print('\nVocê errou, essa letra não existe na palavra! \u274C')
            sleep(2)
            tentativas = tentativas - 1
            lista_errada.append(letra_escolhida)

    limpar_tela()

    if contador_erros >= tentativas:
        print(f'Você perdeu!\n')
        desenhar_boneco(tentativas)
        print(f'\nA palavra correta era "{palavra_escolhida.upper()}".\n')
    else:
        print(f'Parabéns! Você acertou a palavra! \U0001f389\n\nA palavra correta era {palavra_escolhida.upper()}!\n')

    jogar_novamente = input('Deseja jogar novamente? (S/N) ')
    limpar_tela()

    if jogar_novamente.lower() != 's':
        limpar_tela()
        print('\nObrigado por jogar!\n')
        break