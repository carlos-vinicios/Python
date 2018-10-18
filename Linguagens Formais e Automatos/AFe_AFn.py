''' 
    Equipe:
    AFe -> AFn


    Forma de entrada: estado de destino relacionado a um elemento lido
    Formato de saída: elemento lido relacionado a um ou mais estados de destino
'''

def buscaE(trans, afe):
    t1 = []
    destinos = list(trans.keys())
    elementos = list(trans.values())
    for i in range(0, len(elementos)):
        if elementos[i] == 'e':
            t1.append(destinos[i])
            t2 = buscaE(afe[destinos[i]], afe)
            if isinstance(t2, list) and len(t2) > 0:
                return t1 + t2
            else:
                return t1
#fim da função de busca por elementos e

def conversao(afe): #corrigir apenas a formatação da saída que o mesmo não apresenta da forma correta, olhar folha que está no caderno de LFA
    afn = {}

    for i in afe:
        transicoes = {}
        e1 = afe[i]
        d1 = list(e1.keys()) #d1: destinos que o automato pode ter, de acordo com cada elemento lido
        el1 = list(e1.values()) #el1: são os elementos lido
        for j in range(0, len(d1)):
            d2 = d1[j] #esse é o estado que vai ser verificado
            el2 = el1[j] #esse é o elemento do alfabeto lido da vez
            transicoes[d2] = el2            
            if 'e' in afe[d2].values():
                te = buscaE(afe[d2], afe)
                for k in te:
                    transicoes[k] = el2
                afn[i] = transicoes

    return afn
#fim da função de conversão

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

if(convert):
    afn = conversao(afe)
    print(afn)