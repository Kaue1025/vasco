import random

pontos_CPU = 0
pontos_player = 0
print("Bem-Vindo a o jogo Par ou Impar")
while True:

    escolha_jogador = input("escolha par ou impar:")
    while escolha_jogador not in ['par', 'impar']:
     
     print("ivalido! Escolha par ou impar:")



#player_vs_CPU
    numero_jogador = int(input("Jogador digite seu numero de 0 a 10:"))
   
    numero_cpu = random.randint(0 , 10)
    print("A escolha da CPU é", numero_cpu)
   
    soma = numero_jogador + numero_cpu

    #SOMA

    if soma % 2 == 1:
     resultado = "impar"

    else:
     resultado = "par"

   
    if escolha_jogador == "par" and soma == 1:
        print("Player ganhou.")
        pontos_player += 1

    if  escolha_jogador == "impar" and soma == 1:
        print("CPU ganhou.")
        pontos_CPU += 1 

    if  escolha_jogador == "par" and soma != 1:
        print("CPU ganhou.")
        pontos_CPU += 1

    if  escolha_jogador == "impar" and soma != 1:
        print("Player ganhou.")
        pontos_player += 1
   
    print("Pontos da CPU:", pontos_CPU)
    print("Pontos do Player:", pontos_player)

    if pontos_player == 2:
        print("O PLAYER ganhou, por:", pontos_player, "a", pontos_CPU,"pontos.")
        break
   
    if pontos_CPU == 2:
        print("A CPU ganhou, por:", pontos_CPU, "a", pontos_player,"pontos.")
        break


#CPU_CPU

