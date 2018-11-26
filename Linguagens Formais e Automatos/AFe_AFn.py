''' 
    Equipe:
    - Carlos Vinicios Martins Rocha
    AFe -> AFn

    Forma de entrada: estado de destino relacionado a um elemento lido
    Formato de saída: estado vigente com seus respectivos estados de destino, de acordo com cada elemento lido
'''
def union(a, b): #realiza a união de duas listas (união de conjuntos)
    for e in b:
        if not e in a:
            a.append(e)
    return a

def buscarE(afe, estado, elem): #realiza a busca por elementos epsilons 
    trans1 = {} #transicoes primarias
    trans2 = {} #transicoes secundarias
    atual = afe[estado] #pega o estado que está buscando mais elementos epsilons
    for a in atual: #realiza a busca por cada transição contida no estado dado
        trans1[a] = []
        if(atual[a] == 'e'):
            trans1[a].append(elem) #adiciona caso encontre um elemento epsilon
            trans2 = buscarE(afe, a, elem) #realiza uma busca recursiva no estado encontrado
            if(len(trans2) > 0): #caso a busca recursiva tenha elementos, adiciona os mesmos as transições anteriormente encontradas
                for t in trans2:
                    if t in trans1.keys():
                        trans1[t] = union(trans1[t], trans2[t])
                    else:
                        trans1[t] = trans2[t]
    return trans1

def pipeline(afe, estado, elem): #verifica as transições paralelas para os estados epsilons 
    trans1 = {}
    trans2 = {}
    atual = afe[estado]
    for i in atual:
        trans1[i] = []
        if(atual[i] == elem): #verifica se o dado estado apresenta transição com o elemento especifico lido
            trans1[i].append(elem)
        if(atual[i] == 'e'):
            trans1[i].append(elem)
            trans2 = pipeline(afe, i, elem)
        if(len(trans2) > 0):
            for t2 in trans2:
                if t2 in trans1.keys() and len(trans2[t2]) > 0:
                    trans1[t2] = union(trans1[t2], trans2[t2])
                elif len(trans2[t2]) > 0:
                    trans1[t2] = trans2[t2]
            trans2.clear()
    return trans1


def conversao(afe, alfabeto, es_finais): #corrigir apenas a formatação da saída que o mesmo não apresenta da forma correta, olhar folha que está no caderno de LFA
    afn = {}
    finais = []
    for i in afe:
        trans1 = {} #transicoes primarias
        trans2 = {} #transicoes secundarias
        transicoes = afe[i]
        for t in transicoes:
            if not t in trans1.keys(): #verifica se já existe tal estado dentro as transições, caso não, cria um novo
                trans1[t] = []
            for elem in alfabeto:
                if(transicoes[t] == elem): #para cada elemento do alfabeto, verifica se apresenta o dado elemento
                    trans1[t].append(elem) #adiciona ele as transições
                    trans2 = buscarE(afe, t, elem) #realiza uma busca por transições epsilons
                    for f in es_finais: #verifica se através de um estado não final, atinge-se um final, fazendo uso da transições epsilons
                        if f in trans2.keys() and len(trans2[f]) > 0:
                            finais.append(i)
                elif(transicoes[t] == 'e'): #caso trate diretamente um transição epsilon, verifica o pipeline dela para o dado elemento do alfabeto
                    trans2 = pipeline(afe, t, elem)
                if(len(trans2) > 0):  #adiciona os retornos de ambas as funções de busca por transições, sempre evitando redundâncias
                    for t2 in trans2:
                        if t2 in trans1.keys() and len(trans2[t2]) > 0:
                            trans1[t2] = union(trans1[t2], trans2[t2])
                        elif len(trans2[t2]) > 0:
                            trans1[t2] = trans2[t2]
                    trans2.clear()
        afn[i] = trans1 #adiciona todas as transições mapeadas
    finais = finais + es_finais
    afn["finais"] = finais #verifica e adiciona os estados finais existentes e mapeados pelas funções ao AFN
    return afn #retorna o AFN com seus estados finais
#fim da função de conversão

totalTrans = 0
afe = {} #transições de cada estado do automato
alfabeto = [] #elementos presentes no alfabeto do AFe
finais = [] #estados finais do AFe
afnFinais = [] #estados finais do AFn
convert = True #flag para realização da conversão

qtd_alfa = int(input("Quantidade de elementos no alfabeto: "))
if(qtd_alfa <= 3):#deve ser limitado a no máximo 3 elementos
    for i in range(0, qtd_alfa):#lê os elementos do alfabeto
        alfabeto.append(input("Elemento " + str(i+1) + " do alfabeto: "))

    qtd_estados = int(input("Quantidade de estados: "))#quantidades de elementos presentes no autômato 
    if(qtd_estados < 5):#só deve ser executado para no máximo 4 estados
        for i in range(0, qtd_estados):
            text = "Quantidade de transições para q"+str(i)+": "
            label = "q"+str(i) #texto para a chave do dict
            qtd = int(input(text)) #quantidade de transições do estado
            totalTrans+= qtd 
            trans = {} #cria um dicionario para as transições lidas
            if(qtd <= 3 and qtd > 0):
                print("Entre com as transição: (estado de destino - elemento lido)")
                for j in range (0, qtd):
                    estado = input() #ler o estado de destino
                    transicao = input() #ler o elemento lido do alfabeto
                    trans[estado] = transicao #salva essa transição no dict
            afe[label] = trans #adiciona a transição do dado estado ao AFe

            if(totalTrans >= 7): #não deixa estourar o limite máximo de transições para o autômato
                print("Quantidade máxima de transições estourados")
                convert = False
                break 
        qtd_finais = int(input("Quantidade de estados finais: "))
        if qtd_finais > 0:
            for i in range(0, qtd_finais): #faz a leitura dos estados finais caso possua ao menos um estado
                finais.append(input("Estado final: "))
        else: #caso não possua ao menos 1, deve dar erro
            print("O automato deve possuir ao menos 1 estado final")
            convert = False
    else:
        print("A quantidade de estados deve ser menor que 5")    

if(convert):
    afn = conversao(afe, alfabeto, finais) #chama a função de conversão
    afnFinais = afn["finais"] #pega os estados finais
    del afn["finais"] #remove os mesmos do autômato
    print("AFN final:") #imprime o autômato convertido
    print(afn)
    print("Estados finais:") #imprime os seus estados finais
    print(afnFinais)