#programa que calcula o resultado de n elevado a x

#entrada de datos de: n e x
n = int(input("Informe o valor de n: " ))
x = int(input("Informe o valor de x: "))

#calculo de n elevado a x:
resultado = n ** x 
 
 #condição: se x for 0;  
if x == 0:
   n =  1
print (resultado)
    
    