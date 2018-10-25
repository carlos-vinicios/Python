''' 
    Equipe:
    AFe -> AFn


    Forma de entrada: estado de destino relacionado a um elemento lido
    Formato de saída: elemento lido relacionado a um ou mais estados de destino
'''
def buscarE(afe, estado, elem):
    trans1 = {} #transicoes primarias
    trans2 = {} #transicoes secundarias
    atual = afe[estado]
    for i in atual:
        #trans1[i] = []
        if(atual[i] == 'e'):
            trans1[i] = elem
            trans2 = buscarE(afe, i, elem)
            if(len(trans2) > 0):
                trans1.update(trans2)
    return trans1

def pipeline(afe, estado, elem):
    trans1 = {}
    atual = afe[estado]
    for i in atual:
        trans1[i] = []
        if(atual[i] == elem):
            trans1[i].append(elem)
    return trans1


def conversao(afe, alfabeto): #corrigir apenas a formatação da saída que o mesmo não apresenta da forma correta, olhar folha que está no caderno de LFA
    afn = {}

    for i in afe:
        trans1 = {} #transicoes primarias
        trans2 = {} #transicoes secundarias
        transicoes = afe[i]
        for t in transicoes:
            trans1[t] = []
            for elem in alfabeto:
                if(transicoes[t] == elem):
                    trans1[t].append(elem)
                    trans2 = buscarE(afe, t, elem)
                    if(len(trans2) > 0):
                        trans1.update(trans2)
                elif(transicoes[t] == 'e'):
                    trans2 = pipeline(afe, t, elem)
                    if(len(trans2) > 0):
                        trans1.update(trans2)
        afn[i] = trans1
    return afn
#fim da função de conversão

totalTrans = 0
afe = {} #transições de cada estado do automato
alfabeto = []
convert = True

qtd_alfa = int(input("Quantidade de elementos no alfabeto"))
if(qtd_alfa <= 3):
    for i in range(0, qtd_alfa):
        alfabeto.append(input("Elemento do alfabeto"))

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

#print(afe)

if(convert):
    afn = conversao(afe, alfabeto)
    print(afn)