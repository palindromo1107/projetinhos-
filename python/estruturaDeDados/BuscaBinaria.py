#extra
import time

#lista
l = [1,2,3,4,5,6,7,8,9]

def busca(lista, alvo):
    
    #definição inicio da lista
    inicio = 0
    
    #definição final da lista
    final = len(lista) - 1
    
    while inicio < final:
        
        #definição meio da lista
        meio = (inicio + final) // 2
        
#_______________________________________#
    #extra
        time.sleep(1.5)
        
        lis = []
        lis.append(lista[inicio : final])
        
        print()
        print(meio)
        print()
        print(lis)
        print()
        #esta parte é meio confusa mas funciona
        #nao entendo o porque
#_______________________________________#
        
        #verificar se o item está no meio
        if alvo != lista [ meio ]:
            
            #verificar se está a esquerda
            if alvo < lista[meio]:
                
                #o fim da lista se move para a esquerda e fica após o meio
                final = meio - 1
                
            #se nao estiver está a direita
            else:
                
                #o inicio se move para a direita e fica após o meio
               inicio = meio + 1
               
        #quando o item estiver no meio
        else:
            
            #retorna o valor do item
            return meio
            
    #retorna o index do item
    return -1
    
    #alvo
target = 8

#executar função e atribuir a variável a
a = busca(l, target)

print()
print(f"item {target} encontrado no index {a}")
print()