class Edge:
    def __init__(self,v1,v2,data,id_edge):
        self.v1=v1
        self.v2=v2
        self.data=data
        self.id_edge=id_edge
    

    '''nos devuelve el vértice opuesto de una arista, dado el primer vértice de esta'''
    def getOpposite(self,v):
        vertice = None
        if(v==self.v1 or v==self.v2):
            if(v==self.v1):
                vertice=self.v2
            else:
                vertice=self.v1

        return vertice

    def __str__(self):
        cadena = str(self.v1) + " - "
        cadena += str(self.v2) + " : "
        cadena += str(self.data) + "\n"
        return cadena

    def __gt__(self,other):
        result = False

        if(self.id_edge>other.id_edge):
            result=True

    def __lt__(self,other):
        result = False

        if(self.id_edge<other.id_edge):
            result=True