import math
class Nodo:
    def __init__(self,idnodo,padre,estado,estrategia,costo,nombre_heuristica,d1,a1):
        self.idnodo=idnodo
        self.padre=padre
        self.estado=estado
        self.heuristica=None
        self.d1=d1
        self.a1=a1

        if padre != None:
            self.costo=self.padre.costo + costo
            self.profundidad = self.padre.profundidad + 1
            self.accion = str(self.padre.estado.nodo.id_vertex) + "->" + str(self.estado.nodo.id_vertex)

        else:
            self.costo=round(0,2)
            self.profundidad=round(0,2)
            self.accion="None"


        if(estrategia=="depth"):
            self.heuristica=self.calcularHeuristica(nombre_heuristica)
            self.valor=1/(self.profundidad + 1)
        elif(estrategia=="breadth"):
            self.heuristica=self.calcularHeuristica(nombre_heuristica)
            self.valor=self.profundidad
        elif(estrategia=="uniform"):
            self.heuristica=self.calcularHeuristica(nombre_heuristica)
            self.valor=self.costo
        elif(estrategia=="A"):
            self.heuristica=self.calcularHeuristica(nombre_heuristica)
            self.valor = self.costo + self.heuristica
        elif(estrategia=="greedy"):
            self.heuristica=self.calcularHeuristica(nombre_heuristica)
            self.valor=self.heuristica


    
        
    def calcularDistanciaEuclidea(self,vertice1,vertice2):
        distancia = math.sqrt(((float(vertice1.data["x"]) - float(vertice2.data["x"]))**2) + ((float(vertice1.data["y"]) - float(vertice2.data["y"]))**2))
        return distancia

    def calcularHeuristica(self,nombre_heuristica):
        if(nombre_heuristica=="euclidea"):

            if(len(self.estado.por_visitar)==0):
                h=0

            else:
                n=self.estado.nodo
                pv=self.estado.por_visitar

                d2=self.calcularDistanciaEuclidea(n,pv[0])
                aux=0
                
                for i in pv:
                    aux=self.calcularDistanciaEuclidea(n,i)

                    if(aux<d2):
                        d2=aux

                h=min(self.d1,d2) * len(pv)
            return h

        elif(nombre_heuristica=="arco"):
            pv=self.estado.por_visitar
            h=len(pv)*self.a1

            return h

    #[0][0.00,[(37,[248,528,896,1097])|eef167],None,None,0,0.00,0.00]
    def __str__(self):
        if(self.padre==None):
            id = "None"
        else:
            id = str(self.padre.idnodo)

        return "[" + str(self.idnodo) + "]" + "[" + str("{:.2f}".format(self.costo)) + "," + str(self.estado) + "," + id + "," + self.accion + "," + str(self.profundidad) + "," + str("{:.2f}".format(self.heuristica)) + "," + str("{:.2f}".format(self.valor)) + "]"


    def __lt__(self, other):

        result = False

        if (self.valor < other.valor) or ((self.valor == other.valor) and (self.idnodo < other.idnodo)):
            result=True

        return result

    def __gt__(self, other):

        result = False

        if (self.valor > other.valor) or ((self.valor == other.valor) and (self.idnodo > other.idnodo)):

            result = True
        return result