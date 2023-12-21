from GraphHandler import GraphHandler
from graph.Graph import *
import xml.sax
from Estado import *
from queue import PriorityQueue
from Nodo import *
import math


def objetivo(e):
    is_obj=False

    if(len(e.por_visitar)==0):
        is_obj=True

    return is_obj

def leerGrafo(ruta):
    g = Graph(True)

    parser = xml.sax.make_parser()
    handler = GraphHandler(g)
    parser.setContentHandler(handler)
    parser.parse(ruta)

    return g

def algoritmo(n0,estrategia,prof_max,nombre_heuristica,d1,a1):
    frontera = PriorityQueue()
    visitados=set()
    solucion=False
    secuencia=""
    frontera.put(n0)

    n=None
    idnodo=1
    while(frontera.qsize()>0 and solucion==False):
        n=frontera.get()


        if(objetivo(n.estado)):
            solucion=True
        elif(n.estado.id_estado.hexdigest() not in visitados and n.profundidad<=prof_max):
            visitados.add(n.estado.id_estado.hexdigest())
            sucs = n.estado.sucesores()


            #Se ha probado con todos los IDs [8fd649, 0f465c, 2dfdd7, 12daf6] dados en MD5 y se ha llegado a 
            #la conclusion que es con ese ID con el que se obtiene la menor profundidad
            if(n.estado.id_estado.hexdigest()[-6:]=="12daf6"):
                print("el nodo " + str(n))

            for i in sucs:
                naux = Nodo(idnodo,n,i,estrategia,i.costeEstado,nombre_heuristica,d1,a1)

                frontera.put(naux)
                    
                idnodo+=1
                #Se ha probado con todos los IDs dados en MD5 [8fd649, 0f465c, 2dfdd7, 12daf6] y se ha llegado a 
                #la conclusion que es con ese ID con el que se obtiene la menor profundidad
                if(naux.estado.id_estado.hexdigest()[-6:]=="12daf6"):
                    print("el nodo aux" + str(naux))


    if(solucion):
        secuencia_stack = list()
        while(n!=None):
            secuencia_stack.append(str(n) + "\n")
            n=n.padre
        while(len(secuencia_stack)>0):
            secuencia+=secuencia_stack.pop()

        return secuencia
        
    else:
        secuencia="no hay solucion"

    return secuencia


def calcularDistancia(vertice1,vertice2):
    distancia = math.sqrt(((float(vertice1.data["x"]) - float(vertice2.data["x"]))**2) + ((float(vertice1.data["y"]) - float(vertice2.data["y"]))**2))
    return distancia

def distaciaMinEstadoInicial(e0):
    i=0
    j=0

    pv = e0.por_visitar
    min = calcularDistancia(pv[0],pv[1])
    aux=0
    while(i<len(pv)):
        j=i+1
        while(j<len(pv)):
            aux = calcularDistancia(pv[i],pv[j])
            if(aux<min):
                min=aux
            j+=1

        i+=1

    return min

def calcularLongitudMinima(g):
    lista = g.edgeList

    lmin=float(lista[0].data["length"])

    
    for i in lista:
        if float(i.data["length"]) < lmin:
            lmin = float(i.data["length"])

    return lmin


if __name__ == '__main__':
    g=leerGrafo("./grafos/nuevo.graphXML")
    (37,[248,528,896,1097])
    pv = list()
    pv.append(g.getVertice(242))
    pv.append(g.getVertice(817))
    pv.append(g.getVertice(915))
    pv.append(g.getVertice(1105))
    pv.append(g.getVertice(1202))

    v0=g.getVertice(1163)
    e0=Estado(v0,pv,0)

    d1 = distaciaMinEstadoInicial(e0)
    a1 = calcularLongitudMinima(g)

    #variables usadas para indicar la estrategia, heuristica y profundidad maxima
    estrategia = "greedy"
    heuristica="arco"
    pmax=600

    n0=Nodo(0,None,e0,estrategia,0,heuristica,d1,a1)

    
    s=algoritmo(n0,estrategia,pmax,heuristica,d1,a1)
    print("solucion")
    print(s)