print("Digite a frase")
frase = str(input())

subs = frase.split(" ")
print(subs)

for i in range(0, len(subs)):
    print("Palavra: " + subs[i] + " repetições: " + frase.count(subs[i]))    
