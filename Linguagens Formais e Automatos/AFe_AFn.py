''' 
    Equipe:
    AFe -> AFn


    Forma de entrada: estado de destino relacionado a um elemento lido
    Formato de saída: elemento lido relacionado a um ou mais estados de destino
'''

def conversao(afe, alfabeto):
    afn = {}

    for i in afe:
        e1 = afe[i]
        d1 = e1.keys()
        el1 = e1.values()
        for j in d1:
            e2 = afe[j]
            el2 = e2.values()
            if('e' in el2):
                d2 = e2.keys()


    #return afn

totalTrans = 0
afe = {} #transições de cada estado do automato
convert = True

estados = int(input("Quantidade de estados:"))

if(estados < 5):
    for i in range(0, estados):
        text = "Quantidade de transições para q"+str(i)+":"
        label = "q"+str(i)
        qtd = int(input(text))
        if(qtd <= 3):
            totalTrans+= qtd
            trans = {}
            print("Entre com as transição: (estado de destino - elemento lido)")
            for j in range (0, qtd):
                estado = input()
                transicao = input()
                trans[estado] = transicao
            afe[label] = trans

        if(totalTrans >= 7):
            print("Quantidade máxima de transições estourados")
            convert = False
            break 
else:
    print("A quantidade de estados deve ser menor que 5")    

print(afe)

#if(convert):
    #afn = conversao(afe)
    #print(afn)