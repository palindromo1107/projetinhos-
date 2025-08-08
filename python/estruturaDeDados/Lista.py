class Elemento:

    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.primeiro = None

    #fabrica de criar novos elementos:
    def criarNovoElemento(self, valorQualquer):
        e = Elemento(valorQualquer, None)
        return e
    
    def imprimeLista(self):
        aux = self.primeiro
        if(aux != None):
            while(aux != None):
                print(aux.valor)
                aux = aux.proximo
        else:
            print("--- Lista Vazia ---")

    def addElementoNoFinal(self, valorQualquer):
        aux = self.primeiro
        if(aux != None):
            #se nao for vazio JA TEM ELEMENTO
            while(aux.proximo != None):
                aux = aux.proximo
            #neste ponto o aux aponta para o ultimo elemento
            aux.proximo = self.criarNovoElemento(valorQualquer)     
        else:
            # NAO TEM ELEMENTO
            self.primeiro = self.criarNovoElemento(valorQualquer)

    def removeElementoNoFinal(self):
        aux = self.primeiro
        if(aux != None):
            #Se tiver 2 ou mais elementos
            if(aux.proximo != None):
                #Este laço faz com que o ponteiro aux
                #pare no penultimo elemento de uma lista qualquer
                while(aux.proximo.proximo != None):
                    aux = aux.proximo
                del(aux.proximo)
                aux.proximo = None
            #se só tem 1 elemento
            else:
                del(aux)
                self.primeiro = None
                print("--- Lista Vazia novamente ---")  
        else:
            # NAO TEM ELEMENTO
            print("--- Lista Vazia ---")
    
    def addElementoNoInicio(self, valorQualquer):
        aux = self.primeiro
        if(aux != None):
            #CRIAR MAIS UM Elemento
            novo = self.criarNovoElemento(valorQualquer)
            #PEGAR ESSE NOVO Elemento e apontar para o primeiro
            novo.proximo = self.primeiro
            #PEGAR O PONTEIRO PRIMEIRO e apontar para o novo primeiro
            self.primeiro = novo
        else:
            # NAO TEM ELEMENTO
            self.primeiro = self.criarNovoElemento(valorQualquer)

    def removeElementoNoInicio(self):
        aux = self.primeiro
        if(aux != None):
            #PEGAR O PONTEIRO PRIMEIRO e apontar para o SEGUNDO
            self.primeiro = self.primeiro.proximo
            #DEPOIS eu apago o aux, pois o aux estava apontando
            #para o primeiro elemento:
            del(aux)
        else:
            # NAO TEM ELEMENTO
            print("--- Lista Vazia ---")

    def removeQualquerElemento(self, v):
        aux = self.primeiro
        if(aux != None):
            ant = self.primeiro
            #pesquisar o elemento na lista
            while(aux != None):
                if(aux.valor != v):
                    ant = aux
                    aux = aux.proximo
                else:
                    #ACHEI O QUE TAVA PROCURANDO
                    #depois que achou o elemento:

                    #se for o 1o chama a fn removeDoInicio
                    if(aux.valor == self.primeiro.valor):
                        self.removeElementoNoInicio()
                        break
                    #se for o ultimo chama a fn removeDoFinal
                    elif(aux.proximo == None):
                        self.removeElementoNoFinal()
                        break
                    #caso contrario, atualiza os apontamentos e
                    #depois remove o elemento
                    else:
                        ant.proximo = aux.proximo
                        del(aux)
                        break
            #--FIM DO WHILE--#
            print("--- Valor nao encontrado ---")
        else:
            # NAO TEM ELEMENTO
            print("--- Lista Vazia ---")
##------------------------------------------------##
## MAIN ##

#Criando uma lista VAZIA
minhaLista = Lista()
minhaLista.addElementoNoFinal(91)
minhaLista.addElementoNoFinal(92)
minhaLista.addElementoNoFinal(93)
minhaLista.addElementoNoFinal(94)

minhaLista.imprimeLista()
print("---------------------")

minhaLista.removeQualquerElemento(100)
minhaLista.imprimeLista()