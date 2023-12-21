import xml.sax
from graph.Graph import *

class GraphHandler(xml.sax.ContentHandler):
    def __init__(self,g):
        self.g = g

        '''diccionarios para guardar las claves y valores de los atributos'''
        self.vertexDic = {}
        self.edgeDic = {}
        self.graphDic = {}

        '''diccionarios para los datos que se guarden en los vértices y aristas'''
        self.vertexDataDic = {}
        self.edgeDataDic = {}

        '''variables que nos dirán si se está leyendo un nodo o una arista'''
        self.vertexOpen = False
        self.edgeOpen = False

        '''variable auxiliar para almacenar el nombre del atributo cuyo valor se obtendrá en el método characters. Dicho atributo
        será añadido al diccionario de datos de vértices o aristas, dependiendo del elemento que se esté leyendo'''
        self.dato = ""
        self.datoContent=""

    def startElement(self, name, attrs):
        if(name=="key"):
            if(attrs["for"]=="graph"):
                self.graphDic[attrs["id"]]=attrs["attr.name"]
            elif(attrs["for"]=="node"):
                self.vertexDic[attrs["id"]]=attrs["attr.name"]
            elif(attrs["for"]=="edge"):
                self.edgeDic[attrs["id"]]=attrs["attr.name"]

        elif(name=="node"):
            self.vertexOpen=True
            self.vertexDataDic["id"]=attrs["id"]

        elif(name=="edge"):
            self.edgeOpen=True
            self.edgeDataDic["source"]=attrs["source"]
            self.edgeDataDic["target"]=attrs["target"]


        elif(name=="data"):
            if(self.vertexOpen==True):
                self.dato = self.vertexDic[attrs["key"]]
            elif(self.edgeOpen==True):
                self.dato = self.edgeDic[attrs["key"]]

    def endElement(self, name):
        if(name=="node"):
            self.vertexOpen=False
            self.g.addVertexWithId(self.vertexDataDic,int(self.vertexDataDic["id"]))
            self.vertexDataDic = {}
        elif(name=="edge"):
            self.edgeOpen=False
            self.g.addEdge(self.g.getVertice(self.edgeDataDic["source"]),self.g.getVertice(self.edgeDataDic["target"]),self.edgeDataDic)
            self.edgeDataDic = {}
        elif(name == "data"):
            if(self.vertexOpen==True and (self.dato=="x" or self.dato=="y")):
                self.vertexDataDic[self.dato]=self.datoContent
            elif(self.edgeOpen==True and self.dato=="length"):
                self.edgeDataDic[self.dato]=self.datoContent

    def characters(self, content):
            if(self.vertexOpen==True and (self.dato=="x" or self.dato=="y")):
                self.datoContent = str(content)
            elif(self.edgeOpen==True and self.dato=="length"):
                self.datoContent = str(content)