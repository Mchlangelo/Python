"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	
556

Exemplo de Saída
0:9:16

"""

print("========== SOLUÇÃO ==========")
N = int(input(" "))
h = N // 60**2
N = N - h * 60**2
m = N //60
N = N - m * 60
s = N
print("{}:{}:{}".format(h, m, s))



