import numpy as np

#questão 1

a = np.array([0, 5, 22, 10, 15, 99, 18], dtype=int)
print("Digite o número")
n = int(input())
b = np.where( a > n)
print(b)

#questão 2

print("Tamanho:")
t = int(input())
a1 = []
for i in range(0, t):
    a1.append(int(input()))

a2 = np.int32(a1)
print("Máximo: ", a2.max())
print("Mínimo: ", a2.min())
print("Soma", a2.sum())
print("Desvio Padrão", a2.std())
print("Média", a2.mean())

#questão 3

a = np.array([[[230, 250, 222], [10, 23, 49], [55, 250, 212], [130, 245, 255]], [[230, 250, 222], [10, 23, 49], [55, 250, 212], [130, 245, 255]]])

a[:,:,0] = 255
a[:,:,1] = 135
a[:,:,2] = 0

print(a)
