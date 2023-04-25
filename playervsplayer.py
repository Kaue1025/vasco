#PLAYER VS PLAYER
from getpass import getpass

pontos_player1 = 0
pontos_player2 = 0

print("Bem-Vindo a o jogo Par ou Impar (PLAYER VS PLAYER)")

while True:
    escolha_jogador1 = input("Jogador 2 escolha par ou impar?")
    while escolha_jogador1 not in ['par', 'impar']:
     
     print("ivalido! Escolha par ou impar:")

    numero_jogador1 = int(getpass("Jogador 2 digite seu numero de 0 a 10:"))

    escolha_jogador2 = input("Jogador 1 escolha par ou impar?")
    while escolha_jogador2 not in ['par', 'impar']:
     
     print("ivalido! Escolha par ou impar:")
   
    numero_jogador2 = int(getpass("Jogador 1 digite seu numero de 0 a 10:"))
   
    soma = numero_jogador1 + numero_jogador2
    print("A soma é", soma)

    #SOMA

    if soma % 2 == 1:
     resultado = "impar"

    else:
     resultado = "par"

   
    if escolha_jogador1 == "par" and soma == 1:
        print("Jogador 1 ganhou.")
        pontos_player2 += 1

    if  escolha_jogador1 == "impar" and soma == 1:
        print("Jogador 2 ganhou.")
        pontos_player1 += 1 

    if  escolha_jogador2 == "par" and soma != 1:
        print("Jogador 2 ganhou.")
        pontos_player1 += 1

    if  escolha_jogador2 == "impar" and soma != 1:
        print("Jogador 1 ganhou.")
        pontos_player2 += 1
   
    print("Pontos da Jogador 2:", pontos_player1)
    print("Pontos do Jogador 1:", pontos_player2)

    if pontos_player1 == 2:
        print("O Jogador 2 ganhou, por:", pontos_player1, "a", pontos_player2,"pontos.")
        break
   
    if pontos_player2 == 2:
        print("O Jogador 1 ganhou, por:", pontos_player2, "a", pontos_player1,"pontos.")
        break