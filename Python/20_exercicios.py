"""

1. Escreva um programa que exiba "Olá, mundo!" na tela.
2. Solicite ao usuário que insira seu nome e, em seguida, exiba uma saudação com o nome inserido.
3. Crie um programa que calcule a soma de dois números digitados pelo usuário.
4. Escreva um programa que determine se um número digitado pelo usuário é par ou ímpar.
5. Faça um programa que converta graus Celsius para Fahrenheit.
6. Escreva um programa que calcule o fatorial de um número.
7. Crie um programa que verifique se um número é primo.
8. Faça um programa que calcule o máximo divisor comum (MDC) de dois números.
9. Escreva um programa que conte o número de vogais em uma string digitada pelo usuário.
10. Faça um programa que verifique se uma palavra é um palíndromo.
11. Escreva um programa que leia uma lista de números e exiba apenas os números pares.
12. Faça um programa que ordene uma lista de números em ordem crescente.
13. Crie um programa que calcule a média aritmética de uma lista de números.
14. Escreva um programa que leia uma lista de palavras e exiba a mais longa.
15. Faça um programa que conte quantas vezes uma determinada letra aparece em uma string.
16. Escreva um programa que leia uma lista de números e encontre o maior e o menor elemento.
17. Crie um programa que remova elementos duplicados de uma lista.
18. Faça um programa que verifique se uma string é um pangrama (contém todas as letras do alfabeto).
19. Escreva um programa que converta um número decimal para binário.
20. Crie um programa que simule o jogo Pedra, Papel e Tesoura contra o computador.

"""
import math
import random


while True:
    reiniciar = False

    print("===================== Ex1 ========================")
    print(" Olá, mundo!")
    

    print("===================== Ex2 ========================")
    nome = input(str("Qual o seu nome? "))
    print("Olá, ", nome.capitalize())
    
    print("===================== Ex3 ========================")
    num1 = int(input("Insira um número: "))
    num2 = int(input("Insira outro número: "))
    print("A soma dos dois é: ", num1 + num2)

    print("===================== Ex4 ========================")
    num = int(input("Insira um número: "))
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
            


    print("===================== Ex5 ========================")
    celsius = int(input("Insira o número de temperatura: "))
    Fahrenheit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é: ", Fahrenheit)


    print("===================== Ex6 ========================")
    numero = int(input("Fatorial de: ") )
    resultado=1
    for n in range(1,numero+1):
        resultado *= n
    print(resultado) 


    print("===================== Ex7 ========================")
    num = int(input("O número é primo ou não: "))
    if num % 2 == 0:
        print("O número é primo :)")
    else:
        print("Né não :(")


    print("===================== Ex8 ========================")
    num1 = int(input("Insira um número: "))
    num2 = int(input("Insira outro número: "))
    print("MDC dos dois números: ", math.gcd(num1, num2)) 


    print("===================== Ex9 ========================")
    vocais = 'aeiouAEIOU'
    frase = str(input("Insira uma frase ou texto qualquer: "))
    count = 0
    for letra in frase:
        if letra in vocais:
            count+=1
    print(count, "vocais encontradas no texto!")


    print("===================== Ex10 ========================")
    palavra = str(input("Insira uma palavra: "))
    if palavra[::-1] == palavra:
        print("É palíndromo :)")
        
    else:
        print("Né não :(")

        
    print("===================== Ex11 ========================")
    #Escreva um programa que leia uma lista de números e exiba apenas os números pares.
    lista = []
    pares = []

    for i in range(0, 5):
        numeros = int(input("Digite um número: "))
        lista.append(numeros)
  
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    print("Números pares da lista: ", pares)


    print("===================== Ex12 ========================")
    lista = []

    for i in range(0, 5):
        numeros = int(input("Digite um número: "))
        lista.append(numeros)
    print("Lista ordenada: ", sorted(lista, key=int))



    print("===================== Ex13 ========================")
    entrada = input("Digite os números separados por espaço: ")
    numeros_str = entrada.split()
    numeros_inteiros = []

    for num_str in numeros_str:
        try:
            numero = int(num_str)
            numeros_inteiros.append(numero)
        except ValueError:
            print(f"A entrada '{num_str}' não é um número válido.")


    print("A média aritmética da lista é: ", sum(numeros_inteiros) / len(numeros_inteiros))



    print("===================== Ex14 ========================")
    palavras = []
    entrada = str(input("Digite as palavras separadas por espaço: "))
    palavras = entrada.split()
    print(palavras)

    palmaislonga = ""

    for pal in palavras:
        if len(pal) > len(palmaislonga):
            palmaislonga = pal
    print("A palavra mais longa é: ", palmaislonga)


    print("===================== Ex15 ========================")
    #Faça um programa que conte quantas vezes uma determinada letra aparece em uma string.
    string = input("Insira uma palavra: ")
    letra = input("Qual letra deseja contar? ")
    count = 0
    for i in string:
        if i == letra:
            count+=1
    print(f"A Letra {letra} aparece {count} vezes na string :)")



    print("===================== Ex16 ========================")
    #Escreva um programa que leia uma lista de números e encontre o maior e o menor elemento.
    entrada = input("Digite os números separados por espaço: ")
    numeros_str = entrada.split()
    inteiros = []

    for num_str in numeros_str:
        try:
            numero = int(num_str)
            inteiros.append(numero)
        except ValueError:
            print(f"A entrada '{num_str}' não é um número válido.")

    print("O maior valor da lista é: ", max(inteiros))
    print("O menor valor da lista é: ", min(inteiros))



    print("===================== Ex17 ========================")
    entrada = input("Insira os números com espaço: ")
    numeros = entrada.split()
    lista = []

    for num in numeros:
        inteiros = int(num)
        lista.append(inteiros)

    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    print("Lista com duplicados: ", lista)
    print("Lista sem duplicados: ", l)


    print("===================== Ex18 ========================")
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras_na_frase = ''
    oracao = input('Digite uma oração: ').lower()

    for letra in alfabeto:
        if letra in oracao:
            letras_na_frase += letra
        
    if len(letras_na_frase) == 26:
        print("A string é um pangrama :)")
    else:
        print("A String não é um pangrama :(")



    print("===================== Ex19 ========================")
    #Escreva um programa que converta um número decimal para binário.
    decimal = int(input("Digite o número a convertir em binário: "))
    print("O número {decimal} em binário é: ", bin(decimal))

    print("Agora bora relaxar :) ")
    print("============== Pedra/Papel/Tesoura ================")
    print("===================== Ex20 ========================")
    #Crie um programa que simule o jogo Pedra, Papel e Tesoura contra o computador.
    
    while True:
        cont = False
        print("Suas opções de jogo: ")
        print("Pedra (Pe), papel (Pa), Tesoura (t)")

        valores = ['pe', 'pa', 't']
        random.shuffle(valores)

        for valor in valores:
            entrada = input("Insira sua jogada: ")

            if entrada == valor:
                print("O computador escolheu: ", valor)
                print("Empate")

            elif entrada == 'pe' and valor == 'pa':
                print("O computador escolheu: ", valor)
                print("Você perdeu :(")
            elif entrada == 'pa' and valor == 'pe':
                print("O computador escolheu: ", valor)
                print("Você ganhou :)")

            elif entrada == 'pe' and valor == 't':
                print("O computador escolheu: ", valor)
                print("Você ganhou :)")
            elif entrada == 't' and valor == 'pe':
                print("O computador escolheu: ", valor)
                print("Você perdeu :(")

            elif entrada == 't' and valor == 'pa':
                print("O computador escolheu: ", valor)
                print("Você ganhou :)")
            elif entrada == 'pa' and valor == 't':
                print("O computador escolheu: ", valor)
                print("Você perdeu :(")

        continuar = input("Deseja continuar? (s/n) ")
        if continuar == 's':
                cont = True
        else:
            break
    

    repetir = input("Deseja reiniciar tudo de novo? (s/n) ")
    if repetir.lower() == 's':
        reiniciar = True
    else:
        print("Muito Obrigado pela sua atenção :)")
        exit(0)
    











    

