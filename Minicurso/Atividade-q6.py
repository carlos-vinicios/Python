lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

par = 0
impar = 0
for i in range(0, 9):
    if(lista[i] % 2 == 0):
        par+=1
    else:
        impar+=1

print("Pares: ", par)
print("Impares: ", impar)
    
