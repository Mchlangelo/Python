# Calculadora...

#funções das operações:
import math
def soma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b
def potencia(a, b):
    return a**b
def raizquadrada(a):
    return math.sqrt(a)


while True:   
    
    #opções:
    print ("="* 10, "Calculadora", "="* 10)
    print("1 - Somar")
    print ("2 - Restar")
    print ("3 - Multiplicar")
    print ("4 - Dividir")
    print("5 - Potencia do 1er número elevado ao 2do número")
    print("6 - Raíz quadrada")
    
    opcao = input("Qual opção? ")
   
   #recebendo numeros para somar:
    if opcao == "1":
        num = int(input("Informe um número: "))
        num2 = int(input("Informe outro número: "))
        rsuma = soma(num, num2)
        print ("O resultado da soma é: ", rsuma)
        
   #recebendo numeros para restar : 
  
    elif opcao == "2":
        num = int(input("Informe um número: "))
        num2 = int(input("Informe outro número: "))
        rresta = resta(num, num2)
        print ("O resultado da resta é: ", rresta)
    
    
   #recebendo numeros para multiplicar : 
  
    elif opcao == "3":
        num = int(input("Informe um número: "))
        num2 = int(input("Informe outro número: "))
        rmul = multiplicacao(num, num2)
        print ("O resultado da multiplicação é: ", rmul)
        
    #recebendo numeros para dividir:
    
    elif opcao == "4":
        num = int(input("Informe um número: "))
        num2 = int(input("Informe outro número: "))
        rdiv = divisao(num, num2)
        print ("O resultado da divisão é: ", rdiv)
    
    #recebendo numeros para potencia do primeiro num elevado ao segundo num:
      
    elif opcao == "5":
        num = int(input("Informe um número: "))
        num2 = int(input("Informe outro número: "))
        rpot = potencia(num, num2)
        print ("O resultado da potência é: ", rpot)
    
    #recebendo um num para calcular a sua raíz quadrada
    elif opcao == "6":
       num = int(input("Informe um número: "))
       rraiz = math.sqrt(num)
       print ("O resultado da raíz quadrada de {} é: ".format(num), rraiz)
    
    elif opcao != ["1", "2", "3", "4", "5", "6"]:
        print ("Opção Inválida!! Erro...")

