from graph.Vertex import *
from graph.Edge import *
class Graph:

    def __init__(self,directed):
        self.vertexList=list()
        self.edgeList=list()
        self.directed=directed

        self.unique_id = 0
        self.unique_id_edges = 0

        self.M = 0
        self.N = 0

    ''''método para agregar un vértice al grafo'''
    def addVertex(self,data):

        vertex = Vertex(data,self.unique_id)
        self.vertexList.append(vertex)
        self.unique_id+=1
        self.M+=1
        return vertex

    ''''método para agregar un vértice al grafo con un id dado por el método, es importante no mezclar este método con el anterior'''
    def addVertexWithId(self,data,id):
        vertex = Vertex(data,id)
        self.vertexList.append(vertex)
        self.M+=1
        return vertex

    '''método para añadir una arista al grafo, pasándole los dos vértices, el dato (etiqueta) de la arista y su peso.
    Si el grafo es no dirigido, se crea otra arista en sentido contrario'''
    def addEdge(self,v1,v2,data):
        edges=list()
        edges.append(Edge(v1,v2,data,self.unique_id_edges))
        v1.addOutEdge(edges[0])
        v2.addInEdge(edges[0])
        self.edgeList.append(edges[0])
        self.unique_id_edges+=1

        if not self.directed:
            edges.append(Edge(v2,v1,data,self.unique_id_edges))
            v2.addOutEdge(edges[1])
            v1.addInEdge(edges[1])
            self.edgeList.append(edges[1])
            self.unique_id_edges+=1
            self.N+=1

        self.N+=1

        return edges

    '''método para añadir una arista al grafo, pasándole los dos vértices, el dato (etiqueta) de la arista y su peso.
    Si el grafo es no dirigido, se crea otra arista en sentido contrario. Este método permite insertar un id cualquiera
    para las aristas. No se debe mezclar con el otro método para añadir aristas'''

    def addEdgeWithId(self,v1,v2,data,id):
        edges=list()
        edges.append(Edge(v1,v2,data,id))
        v1.addOutEdge(edges[0])
        v2.addInEdge(edges[0])
        self.edgeList.append(edges[0])

        if not self.directed:
            edges.append(Edge(v2,v1,data,id))
            self.getVertice(v2).addOutEdge(edges[1])
            self.getVertice(v1).addInEdge(edges[1])
            self.edgeList.append(edges[1])
            self.N+=1

        self.N+=1

        return edges

    ''''método que nos permite eliminar un vértice del grafo. Primero borra todas sus aristas de entrada y salida (estas también
    se eliminan de edgeList )y luego se borra el vértice de vertexList'''
    def removeVertex(self, vertex):
        iterOutEdges = vertex.getOutEdges()

        fin1 = False
        while(fin1==False):
            try:

                current=next(iterOutEdges)

                vTo = current.v2

                vTo.removeInEdge(current)

                self.edgeList.remove(current)

                self.N-=1

            except StopIteration:
                fin1=True

        iterInEdges = vertex.getInEdges()
        fin2=False

        while(fin2==False):
            try:

                current=next(iterInEdges)

                vFrom = current.v1

                vFrom.removeOutEdge(current)

                self.edgeList.remove(current)

                self.N-=1

            except StopIteration:
                fin2=True

        self.vertexList.remove(vertex)

        self.M-=1

    '''nos busca un vértice en función de su id'''
    def getVertice(self,id):
        return self.vertexList[int(id)]

    '''método que elimina una arista'''
    def removeEdge(self,edge):
        edge.v1.removeOutEdge(edge)
        edge.v2.removeInEdge(edge)
        self.edgeList.remove(edge)

        self.N-=1

        if(self.directed==False):
            a = self.findEdge(edge.v2,edge.v1)
            a.v1.removeOutEdge(a)
            a.v2.removeInEdge(a)
            self.edgeList.remove(a)
            self.N-=1


    '''métodos que nos dan un iterador a los vértices y aristas del grafo'''
    def vertices(self):
        return iter(self.vertexList)

    def edges(self):
        return iter(self.edgeList)

    '''método que nos dice si dos vértices son adyacentes'''
    def areAdjacent(self,v1,v2):
        v = None
        adjacents=False
        if(self.directed or len(v1.outEdges)<len(v2.outEdges)):
            v=v1
        else:
            v=v2
        
        iterOutEdges = v.getOutEdges()

        fin = False
        while(fin==False):
            try:
                if(v==v1 and next(iterOutEdges).v2 == v2) or (v==v2 and next(iterOutEdges).v2 == v1):
                    adjacents=True

            except StopIteration:
                fin=True

        return adjacents

    '''método que nos devuelve una arista en función de sus dos vértices'''
    def findEdge(self,v1,v2):
        arista = None
        for i in self.edgeList:
            if i.v1 == v1 and i.v2 == v2:
                arista = i
                break
        return arista

    '''método que nos devuelve una arista en función de su id'''
    def findEdgeById(self,id):
        return self.edgeList[int(id)]

    def __str__(self):
        output="vertices\n"

        verIter = self.vertices()

        finv = False
        while(finv==False):
            try:
                output+=str(next(verIter)) + " \n"

            except StopIteration:
                finv=True

        output+="\n"

        output += "aristas\n"
        edIter = self.edges()

        fine=False
        while(fine==False):
            try:
                output+=str(next(edIter)) + "\n"
            except StopIteration:
                fine=True

        output+="\n"

        return output