lista = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Digite um número")
n = int(input())


for i in range (0, 10):
    if lista[i] < n:
        print(lista[i])
