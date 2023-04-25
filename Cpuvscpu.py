import random

#CPU VS CPU

pontos_cpu1 = 0
pontos_cpu2 = 0

print("Bem-Vindo a o jogo Par ou Impar (CPU VS CPU)")

while True:
    print("Par = 1 e impar = 2")
    cpu1 = random.randint(1 , 2)
    print("A escolha da CPU 1 é", cpu1)

    escolha_cpu1 = random.randint(0 , 10)
    print("A escolha da CPU 1 escolheu", escolha_cpu1)
       
    escolha_cpu2 = random.randint(0 , 10)
    print("A escolha da CPU 2 escolheu", escolha_cpu2)
       
    soma = escolha_cpu2 + escolha_cpu1
    print("A soma é", soma)

        #SOMA

    modulo = soma % 2

    if modulo == 1:
     print("Deu impar")

    else:
     print("Deu par")

    if  escolha_cpu1 == 1 and modulo == 1:
        print("CPU 1 ganhou.")
        pontos_cpu1 += 1

    if  escolha_cpu1 == 2 and modulo == 1:
        print("CPU 2 ganhou.")
        pontos_cpu1 += 1 

    if  escolha_cpu2 == 1 and modulo != 1:
        print("CPU 2 ganhou.")
        pontos_cpu2 += 1

    if  escolha_cpu2 == 2 and modulo != 1:
        print("CPU 1 ganhou.")
        pontos_cpu2 += 1
   
        print("Pontos da CPU 1:", pontos_cpu1)
        print("Pontos da CPU 2:", pontos_cpu2)

    if pontos_cpu1 == 2:
        print("O CPU 1 ganhou, por:", pontos_cpu1, "a", pontos_cpu2,"pontos.")
        break
   
    if pontos_cpu2 == 2:
        print("A CPU 2 ganhou, por:", pontos_cpu2, "a", pontos_cpu1,"pontos.")
        break
