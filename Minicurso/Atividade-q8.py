def construc_view(tam):
    p_view = []

    for i in range(0, tam):
        p_view.append("_")

    return p_view

def alter_view(palavra, letra, pos):
    l_palavra = list(palavra)
    l_palavra[pos] = letra
    return l_palavra

print("Digite a palavra")
palavra = input()

view = construc_view(len(palavra)) 
print(view)
for j in range(1, 6):
    print("Tentativa ", j)
    l = input()
    pos = palavra.find(l)
    while pos >= 0:
        view = alter_view(view, l, pos)
        print(view)
        pos = palavra.find(l, pos+1)    

print("Qual a palavra?")
res = input()

if(palavra == res):
    print("Acertou")
else:
    print("Forca")
