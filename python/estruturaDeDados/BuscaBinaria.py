#extra
import time

#lista
l = [1,2,3,4,5,6,7,8,11]

def busca(lista):
    
    #item inicio da lista
    inicio = lista [0]
    
    #item final da lista
    final = lista [ len(lista) - 1 ]
    
    #item meio da lista
    meio = len(lista) // 2
    
    #auxiliar
    aux = lista[meio]
    
    cond = True
    
    #definir o item
    num = int(input())
    
    #verificar se está na lista
    if num not in lista:
        print("numero fora da lista")
        
        #buscar o item
    else:
        while cond:
            
            #verificar se encontrou
            if num == aux:
                cond = False
                print(aux)
                
                #caso seja menor que o auxiliar
            elif num <= aux:
                meio -= 1
                aux = lista [meio]
                
                #caso seja maior que o auxiliar
            else:
                meio += 1
                aux = lista [meio]
                
                #rota percorrida pelo auxiliar parra encontrar o item
            time.sleep(1)
            print(aux)
    
busca(l)