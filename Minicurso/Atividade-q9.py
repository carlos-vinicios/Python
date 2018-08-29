import random

def char():
    charlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return charlist[random.randint(0, 25)] 

print("Digite o tamanho da senha")
tam = int(input())

senha = ""

for i in range(0, tam):
    n = random.randint(0, 320)
    if n % 5 == 0:
        senha += str(random.randint(0, 9))
    else:
        if n % 2 == 0:
            senha += char().upper()
        else:
            senha += char()

print(senha)
