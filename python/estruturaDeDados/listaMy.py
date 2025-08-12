class elemento:
    def __init__(self, valor, proximo):
        self.proximo = proximo
        self.valor = valor

class lista:
    def __init__(self):
        self.primeiro = None

    def criar(self, valor):
        e = elemento(valor, None)
        return e
    
    def addFinal(self, item):
        aux = self.primeiro

        if aux != None:
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = self.criar(item)
        else:
            self.primeiro = self.criar(item)

    def printa(self):
        aux = self.primeiro
        if aux != None:
            while aux != None:
                print(aux.valor)
                aux = aux.proximo
        else:
            print("vazio")

    def removerFinal(self):
        aux = self.primeiro
        if aux != None:
            while aux.proximo.proximo != None:
                aux = aux.proximo
            del(aux.proximo)
            aux.proximo = None
        else:
            print("vazio")

    def addInicio(self, item):
        aux = self.primeiro
        if aux != None:
            new = self.criar(item)
            new.proximo = self.primeiro
            self.primeiro = new
        else:
            self.primeiro = self.criar(item)

    def removerInicio(self):
        aux = self.primeiro
        if aux != None:
            if aux.proximo != None:
                self.primeiro = aux.proximo
                del (aux)
            else:
                del(aux)
                self.primeiro = None
        else:
            print("vazio")

    def removerQualquer(self, item):
        aux = self.primeiro
        ant = None
        if aux is not None:
            while aux is not None:
                if aux.valor == item:
                    if ant is None:
                        # Remover o primeiro elemento
                        self.primeiro = aux.proximo
                    else:
                        ant.proximo = aux.proximo
                    del aux
                    return
                ant = aux
                aux = aux.proximo
            print("not found")
        else:
            print("vazio")



ml = lista()

b = [1,2,3,4,5,6,7,8,9,10]

a = [11,12,13,14,15,16,17,18,19,20]

for i in a:
    ml.addFinal(i)

print("_________________________________________________________________________________")
ml.printa()
print("_________________________________________________________________________________")

ml.removerFinal()

print("_________________________________________________________________________________")
ml.printa()
print("_________________________________________________________________________________")

for i in b:
    ml.addInicio(i)

print("_________________________________________________________________________________")
ml.printa()
print("_________________________________________________________________________________")

ml.removerInicio()

print("_________________________________________________________________________________")
ml.printa()
print("_________________________________________________________________________________")

ml.removerQualquer(9)

print("_________________________________________________________________________________")
ml.printa()
print("_________________________________________________________________________________")
