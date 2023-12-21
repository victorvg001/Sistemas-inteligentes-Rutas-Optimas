class Vertex:
    def __init__(self,data,id_vertex):
        self.data = data
        self.id_vertex=id_vertex
       
        self.inEdges = list()
        self.outEdges = list()


    '''Con este método obtenemos las aristas salientes a nuestro vértice'''
    def getNeighbors(self):
        neighbors = list()
        iterador = iter(self.outEdges)
        current=None

        fin = False
        while fin==False:
            try:
                current=next(iterador)
                neighbors.append(current)
            except StopIteration:
                fin=True

        return neighbors


    
    '''este importante método, nos devuelve una lista de objetos Elemento (ver clase elemento más abajo), los cuales
    son un básicamente un par vértice-longitud_arista, con todos los vértices adjacentes a nuestro vértice y el coste
    (longitud) de sus respectivas aristas. Al final de este método, la lista se devuelve ordenada, en función de los
    ids de los vértices. También se hace una comprobación para evitar incluir un vértice más de una vez, en el caso de que
    ambos vértices estén unidos por más de una arista'''
    def getOutElements(self):
        adj = self.getNeighbors()

        elements = list()

        elementsSet = set()

        for i in adj:

            if(i.getOpposite(self).id_vertex not in elementsSet):
                elements.append(Elemento(i.getOpposite(self),float(i.data["length"])))
                elementsSet.add(i.getOpposite(self).id_vertex)

            
        elements = sorted(elements)

        return elements

    def opposite(self,edge):
        v=Vertex(None,None)

        if(self==edge.v1):
            v=edge.v2
        else:
            v=edge.v1

        return v

    '''obtenemos un iterador a las aristas de salida'''
    def getOutEdges(self):
        return iter(self.outEdges)

    '''obtenemos un iterador a las aristas de entrada'''
    def getInEdges(self):
        return iter(self.inEdges)

    '''añadimos una arista de salida'''
    def addOutEdge(self,e):
        return self.outEdges.append(e)

    '''añadimos una arista de entrada'''
    
    def addInEdge(self,e):
        return self.inEdges.append(e)

    '''eliminamos una arista de entrada'''
    def removeInEdge(self,e):
        self.inEdges.remove(e)

    '''eliminamos una arista de salida'''
    def removeOutEdge(self,e):
        self.outEdges.remove(e)

    def __eq__(self,v):
        return self.id_vertex==v.id_vertex

    def __gt__(self,v2):
        result = False

        if self.id_vertex>v2.id:
            result=True

        return result

    def __lt__(self,v2):
        result = True

        if self.id_vertex>v2.id_vertex:
            result=False

        return result
        

    def __str__(self):
        return str(self.data) + ""


class Elemento:
    def __init__(self,vertice,dato):
        self.vertice = vertice
        self.dato = dato


    def __lt__(self, other):

        result = False

        if(self.vertice.id_vertex<other.vertice.id_vertex):
            result = True

        return result


    def __gt__(self,other):
        result = False

        if(self.vertice.id_vertex>other.vertice.id_vertex):
            result = True

        return result

    def __str__(self):
        return self.vertice.id_vertex