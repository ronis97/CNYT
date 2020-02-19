import complejos as comp
import vectmatrices as vmat
import numpy as np
import matplotlib.pyplot as plt


def label(l):
    lista = []
    for i in range(len(l)):
        lista.append("Pto."+" "+str(i))
    return lista
def estados(V):
    l = []
    for i in range(len(V)):
        l.append(V[i][0][0])
    return l
def proceso(V,Matriz,clicks):
    res = vmat.generar(len(V),len(Matriz[0]))
    res = vmat.multiplicarmatriz(Matriz,V)
    if clicks == 0:
        return V
    else:
        
        for i in range(clicks-1):
            res = vmat.multiplicarmatriz(Matriz,res)
        return res
def main():
    
    V = [[[1,0]],[[0,0]],[[0,0]],[[0,0]]]
    colorV = [[[1,0]],[[0,0]]]
    Matriz = [
        [[0,0],[0.2,0],[0.3,0],[0.5,0]],
        [[0.3,0],[0.2,0],[0.1,0],[0.4,0]],
        [[0.4,0],[0.3,0],[0.2,0],[0.1,0]],
        [[0.3,0],[0.3,0],[0.4,0],[0,0]]
        ]
    clicks = 1000
    colorMatriz = [[[0.5,0],[0.6,0]],[[0.5,0],[0.4,0]]]
    V = vmat.productotensorial(V,colorV)
    Matriz = vmat.productotensorial(Matriz,colorMatriz)
    vmat.mostrar(V)
    vmat.mostrar(Matriz)
    res = proceso(V,Matriz,clicks)
    print("Vector estado final", res)
    labels = label(V)
    estado = estados(res)
    #print(labels)
    #print(estado)
    index = np.arange(len(labels))
    print("Esto es 'index': ",index)
    plt.bar(index,estado)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index,labels,rotation = 75)
    plt.title("Evoucion dinamica del sistema despues de "+str(clicks)+" clicks de tiempo")
    plt.show()    
    
    
main()
