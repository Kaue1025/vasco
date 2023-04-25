def par_impar(): 

 while True:

        print("digite um numero:")
        numero= int (input())


            
        resto = numero % 2 

        if resto ==1:
            print("seu numero e impar")

        else:
            print("seu numero e par")


    

        resposta=input ("Digite um '1' para continuar ou '2' para sair")
        if resposta=="2":
         break
                        
par_impar()
