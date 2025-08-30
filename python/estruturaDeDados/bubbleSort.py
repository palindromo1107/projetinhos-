#extra
import time

#lista
l = [10, 91, 18, 111, 27, 19, 271, 14, 36, 3]

def bubbleSort(lista):
    
    #auxiliares
    X = 0
    Y = 1
    
    #lista de exemplo
    org = []
    for i in lista:
        org.append(i)
    org.sort()
    
    while True:
        
        #definição dos item usando os auxiliares
        x = lista[X]
        y = lista[Y]
        
        #funçao de troca
        if x > y:
            lista[Y] = x
            lista[X] = y
            
        #avançar na lista
        X += 1
        Y += 1
        
        #voltar ao início da lista
        if Y == len(lista):
            X = 0
            Y = 1
            
        #olhar se a lista está organizada
        if lista == org:
            print(lista)
            break
        
        #extra
        time.sleep(0.5)
        print()
        print(lista)
        print()
    
bubbleSort(l)