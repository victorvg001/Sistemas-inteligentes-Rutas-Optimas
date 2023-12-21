from unicodedata import name
from graph.Graph import *
import hashlib


class Estado:

    '''nodo y por_v son objetos Vertex y list de Vertex, respectivamente'''

    def __init__(self,nodo,por_v,costeEstado):
        self.por_visitar = sorted(por_v)
        self.nodo=nodo
        self.cadena=bytes("("+str(self.nodo.id_vertex)+",["+self.cadenaSinEspacios()+"])",'utf-8')
        self.id_estado = hashlib.md5(self.cadena)
        self.costeEstado=costeEstado


    def cadenaSinEspacios(self):
        cadena=""

        i=0

        while(i<len(self.por_visitar)):

            if i==len(self.por_visitar)-1:
                cadena+=str(self.por_visitar[i].id_vertex)
            else:
                cadena+=str(self.por_visitar[i].id_vertex)+","

            i+=1

        return cadena

    def sucesores(self):
        suc=list()
        
        adj = self.nodo.getOutElements()

        for i in adj:
            por_v_aux = self.por_visitar.copy()
            
            if por_v_aux.__contains__(i.vertice):
                por_v_aux.remove(i.vertice)


            suc.append(Estado(i.vertice,por_v_aux,i.dato))


        return suc


    def __str__(self):
        c = str("[("+str(self.nodo.id_vertex)+",["+self.cadenaSinEspacios()+"])|"+self.id_estado.hexdigest()[len(self.id_estado.hexdigest())-6:]+"]")
        return c

    def __eq__(self,other):
        return self.id_estado.hexdigest()==other.id_estado.hexdigest()

    def __lt__(self,other):
        return self.id_estado.hexdigest()<other.id_estado.hexdigest()

    def __gt__(self,other):
        return self.id_estado.hexdigest()>other.id_estado.hexdigest()

    def __hash__(self):
        return int(self.id_estado.hexdigest(),16)
