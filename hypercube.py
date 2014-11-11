# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:03:15 2014

Hypercube to be used with question: how many unique hypercubes landscapes are there in 5D?

This file aims to create a graph with vertices and edges that will aid in exploring the question

@author: maxwell.mckinnon
"""
from bit_string import *
import copy
import networkx as nx
import matplotlib.pyplot as plt
from networkx import graphviz_layout

DEBUG_EA_COUNTER = 0
DEBUG_UNIQ_COUNTER = 0

class HyperCube2D:
    """Contains vertices and edge information"""
    """This is a forward connection dictionary. The key is the "base node". A base node may have outward edges. If so, the pairing vertice is in the value of the key, an element in the list"""
    CUBEDIM = 2
    
    def __init__(self):
        self.dictionary = {'00':[], '01':[], '10':[], '11':[]} #Clear dictionary
    
    def getNumEdges(self):
        """Return the number of edges in dictionary"""
        edgecnt = 0
        for value in self.dictionary.values():
            edgecnt += len(value)
        return edgecnt
        
    def forwardConnect(self, vertex1, vertex2):
        """Connect vertex1 forward to vertex2
        no check for cyclical error"""
        if dimDifferent(vertex1,vertex2) != 1:
            print( "Can only connect across one dimension", vertex1, vertex2)
        elif vertex2 in self.dictionary[vertex1]:
            print( "error, edge direction already in dictionary", vertex1, vertex2)
        elif vertex1 in self.dictionary[vertex2]:
            print( "error, edge already in dictionary but in other direction", vertex1, vertex2)
        else:
            self.dictionary[vertex1].append(vertex2)
            
    def getForwardEdgeMatrice(self):
        """return matrice of which vertices are forward connected to which vertices. 
        
        nonepistatic landscape for example:
        element from row forward connects to element from column
           00 01 10 11 (connects to column)
           -----------
       00 | 0  1  1  0
       01 | 0  0  0  1
       10 | 0  0  0  1
       11 | 0  0  0  0
           -----------
         
         
        returned as [[0,1,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
        
        magnitude epistatic landscape for example:
           00 01 10 11
           -----------
       00 | 0  1  1  0
       01 | 0  0  0  1
       10 | 0  0  0  0
       11 | 0  0  1  0
           -----------
        returned as [[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,1,0]]
        
        reciprocal epistatic landscape for example:
           00 01 10 11
           -----------
       00 | 0  1  1  0
       01 | 0  0  0  0
       10 | 0  0  0  0
       11 | 0  1  1  0
           -----------
        returned as [[0,1,1,0],[0,0,0,0],[0,0,0,0],[0,1,1,0]]
        
        
        nonepistatic landscape for example:
           000 001 010 011 100 101 110 111
           -----------
      000 |  0   1   1   0   1   0   0   0
      001 |  0   0   0   1   0   1   1   0
      010 |  0   0   0   1   0   0   1   0
      011 |  0   0   0   0   0   0   0   1
      100 |  0   0   0   0   0   1   1   0
      101 |  0   0   0   0   0   0   0   1
      110 |  0   0   0   0   0   0   0   1
      111 |  0   0   0   0   0   0   0   0
        """
        size = len(self.dictionary.keys()[0]) #Check length of first key to obtain size "01" = 2, "001" = 3
        
    def hasCycle(self):
        """Returns true if the supposedly DAG is not acyclic"""
        
        #start at beginning
        #generate paths recursively
            #Follow current node forward in all directions
            #follow those current nodes forward in all directions
            #if ever a node is added to any of the paths more than once, quit and report a cycle
        
        #make sure it works for incomplete graphs as well, start at other points than beginning if necessary
        
        parentList = ["00"]
        #self.followForward(parentList):
        
    def followForward(self, parentList):
        #start at parentList, node at tail is the most recent explored (e.g. ["00","01"], "01" is most recently explored)
        #generate paths recursively
            #Follow current node forward in all directions
            #follow those current nodes forward in all directions
            #if ever a node is added to any of the paths more than once, quit and report a cycle
        
        #make sure it works for incomplete graphs as well, start at other points than beginning if necessary
    
        #pulls the tail off the parent list and returns nodes it forward connects to, adds them to expansion list
        expansionList = self.dictionary(parentList[-1])
        
        #call follow forward with each newly made list
        for item in expansionList:
            newchildlist = []
            self.followForward()
        
        
    def getPossibleConnectionsList(self, vertex1):
        """Returns a list of vertices it can connect to without listing vertices already connected to (forward/backward check, no cyclical check), eg: ["00","11"]"""      
        oneDiffList = getOneDiffList(vertex1)
        posConnect = copy.deepcopy(oneDiffList)
        #print( "ENTER getPossibleConnectionsList(vertex1), vertex1: ", vertex1)
        for vertex2 in oneDiffList:
            #Check forward connections
            if vertex2 in self.dictionary[vertex1]:
                posConnect.remove(vertex2)
            #Check reverse connections
            if vertex1 in self.dictionary[vertex2]:
                    #print( "Vertex1, 2: ", vertex1, vertex2)
                    #print( "Because this dictionary has it in reverse: ", self.dictionary)
                    #print( "posConnect before removal: ", posConnect)
                    posConnect.remove(vertex2)
                    #print( "posConnect after removal: ", posConnect)
                    #print() 
        return posConnect

    def getFirstUnconnectedNode(self):
        """Returns first node with an open connection, iterating from 00 11
        Returns node in the format of a bitstring, e.g. '01'
        
        tk Untested
        """
        for node in range(0, 2**self.CUBEDIM):
            node = int2binaryStr(node, self.CUBEDIM)
            conList = self.getPossibleConnectionsList(node)
            if len(conList) > 0:
                return node
        return None
            
class HyperCube3D(HyperCube2D):
    
    CUBEDIM = 3
    def __init__(self):
        self.dictionary = {'000':[], '001':[], '010':[], '011':[], '100':[], '101':[], '110':[], '111':[]}
        
class HyperCube4D(HyperCube2D):
    
    CUBEDIM = 4
    def __init__(self):
        self.dictionary = {'0000':[], '0001':[], '0010':[], '0011':[], '0100':[], '0101':[], '0110':[], '0111':[], '1000':[], '1001':[], '1010':[], '1011':[], '1100':[], '1101':[], '1110':[], '1111':[]}
        
def getOneDiffList(vertex1):
    """Returns a list of vertices 1 different from itself, sorted from "00" to "11"
    eg: "01" returns ["00","11"]
    vertex 1 is a bitstring e.g. '01'
    """
    oneDiffList = []
    for i in range(len(vertex1)):
        copied = vertex1[0:i] + flipBit(vertex1[i]) + vertex1[i+1:]
        oneDiffList.append(copied)
    oneDiffList.sort()
    return oneDiffList
    
def flipBit(vertex1):
    """Changes '1' to '0' and '0' to '1'"""
    if vertex1 == '1':
        return '0'
    if vertex1 == '0':
        return '1'
    print("Error in flipBit()")
    print("vertex1: ")
    print(vertex1)
    
def dimDifferent(vertex1, vertex2):
    """Return how many changes must be made for vertices to equal each other. vertex1, 2 == strings"""
    if len(vertex1)!= len(vertex2):
        print( "Error vertices are not same length", vertex1, vertex2)
    n = 0
    diffn = 0
    for bit1 in vertex1:
        if vertex1[n] != vertex2[n]:
            diffn += 1
        n += 1
    return diffn
    
def isIsomorphism(hcube1, hcube2):
    """is hcube1 an Isomorphism of hcube2? (The same automorphism group) That is, is it a reflection and/or rotation?"""
    

def Expand_and_Add_HC(hcPartial, hcL):
    """Recursive function which finds hypergraphs"""
    global DEBUG_EA_COUNTER
    global DEBUG_UNIQ_COUNTER
    print( "DEBUG_EA_COUNTER: ", DEBUG_EA_COUNTER)
    DEBUG_EA_COUNTER += 1
    
    #print( "FUNC ENTER Expand_and_Add_HC(hcPartial): hcPartial Dict: ", hcPartial.dictionary)
    #Find first unconnected node in hcPartial from 00 to 11 
    firstUnconnectedNode = hcPartial.getFirstUnconnectedNode()
    
    #If no unconnected nodes are found, then all cube edge directions are chosen. Add completed HC edge config to list
    if firstUnconnectedNode == None:
        #if cycle: remove
        if hasCycle(hcPartial) == True:
            print( "CYCLE FOUND:", hcPartial.dictionary)
            return            
        
        #Change to networkX graph object
        hcPartial_nx = convertMyHC_nxHC(hcPartial)
        #if isomorphism to any already found: don't add just found graph to the list
        if isIsomorphicDuplicate(hcL, hcPartial_nx):
            return
        else:
            hcL.append(hcPartial_nx)
            print( "DEBUG_UNIQ_COUNTER: ", DEBUG_UNIQ_COUNTER)
            DEBUG_UNIQ_COUNTER += 1
    else:
        #List all legal edge choices for hcPartial
        posConnections = hcPartial.getPossibleConnectionsList(firstUnconnectedNode)
    
        #For each legal choice: expand to and from that choice (both directions)
        for choice in posConnections: #Each choice is bitstring e.g. '10'
            #Make new_hcPartial copy
            new_hcPartial_forwardConn = copy.deepcopy(hcPartial)
            new_hcPartial_revConn = copy.deepcopy(hcPartial)
            #print("ID 1: ", "ID Forward: ", id(hcPartial), "ID Rev: ", id(new_hcPartial_forwardConn), id(new_hcPartial_revConn))
            #Add choice forward and rev to hypergraph
            new_hcPartial_forwardConn.forwardConnect(firstUnconnectedNode, choice)
            new_hcPartial_revConn.forwardConnect(choice, firstUnconnectedNode)
            
            #print("new new_hcPartial_forwardConn.forwardConnect(firstUnconnectedNode, choice)")
            #print(firstUnconnectedNode, choice)
            #print(new_hcPartial_forwardConn.dictionary, id(new_hcPartial_forwardConn))
            #print()
            
            #print("new new_hcPartial_revConn.forwardConnect(choice, firstUnconnectedNode)")
            #print(choice, firstUnconnectedNode)
            #print(new_hcPartial_revConn.dictionary, id(new_hcPartial_revConn))
            #print())
            
            Expand_and_Add_HC(new_hcPartial_forwardConn, hcL)
            Expand_and_Add_HC(new_hcPartial_revConn, hcL)
            
def getAllHyperCubeConfigs2D():
    #put all possible hypercubes into list
    hcPartial = HyperCube2D() #blank graph
    print("START")
    hcL = []
    hyperCList = Expand_and_Add_HC(hcPartial, hcL)
    hyperCList = hcL
    print("DONE")
    print()
    print("Length: ", len(hyperCList))
    print("Sample 1: ", hyperCList[0].adj)
    print("Sample 2: ", hyperCList[1].adj)
    
    t = 1
    print("Quick Check:")
    for hc in hyperCList:
        if 4 != len(hc.edge.values()):
            print("ERROR! Not all hc's have 4 edges defined")
            t = 0
    if t == 1:
        print("All hc's have 4 edges defined")

    return hyperCList
    
def getAllHyperCubeConfigs3D():
    #put all possible hypercubes into list
    hcPartial = HyperCube3D() #blank graph tk
    print("START getAllHyperCubeConfigs3D()")
    hcL = []
    hyperCList = Expand_and_Add_HC(hcPartial, hcL)
    hyperCList = hcL
    print("DONE getAllHyperCubeConfigs3D()")
    print("Length: ", len(hyperCList))
    print("Sample 1: ", hyperCList[0].adj)
    print("Sample 2: ", hyperCList[1].adj)
    
    t = 1
    failCnt = 0
    print("Quick Check:")
    for hc in hyperCList:
        if 12 != len(hc.edge.values()):
            print("ERROR! Not all hc's have 12 edges defined. This one has:", len(hc.edge.values()))
            if failCnt == 0:
                print(hc.dictionary)
            failCnt += 1
            t = 0
    if t == 1:
        print("All hc's have 12 edges defined")  

    print("Number of Hc without 12 edges: ", failCnt)
    print("Number of HC: ", len(hyperCList))
    return hyperCList    

def getAllHyperCubeConfigs4D():
    #put all possible hypercubes into list
    hcPartial = HyperCube4D() #blank graph tk
    print("START getAllHyperCubeConfigs4D()")
    hcL = []
    hyperCList = Expand_and_Add_HC(hcPartial, hcL)
    hyperCList = hcL
    print("DONE getAllHyperCubeConfigs4D()")
    print("Length: ", len(hyperCList))
    print("Sample 1: ", hyperCList[0].adj)
    print("Sample 2: ", hyperCList[1].adj)
    
    t = 1
    failCnt = 0
    print("Quick Check:")
    for hc in hyperCList:
        if 32 != len(hc.edge.values()):
            print("ERROR! Not all hc's have 32 edges defined. This one has:", len(hc.edge.values()))
            if failCnt == 0:
                print(hc.dictionary)
            failCnt += 1
            t = 0
    if t == 1:
        print("All hc's have 32 edges defined")   

    print("Number of Hc without 32 edges: ", failCnt)
    print("Number of HC: ", len(hyperCList))
    return hyperCList    

def hasCycle(hc):
    """Check if a 2D hc has a cycle"""
    
    """
    Start at node 00
        follow forward connections, adding each node visited to a list
        when stuck, check to see if all nodes have been reached
        repeat process from untouched node
    
    """
    hcCopy = copy.deepcopy(hc) #version of hc to manipulate
    sortedNodes = []
    SetofNoIncomingEdges = getSetofNoIncomingEdges(hcCopy)
    #print("SetofNoIncomingEdges:", SetofNoIncomingEdges)
    
    while len(SetofNoIncomingEdges) > 0:
        #print("SetofNoIncomingEdges:", SetofNoIncomingEdges)
        #print("sortedNodes:", sortedNodes)
        #print("hcCopy.dicionary:", hcCopy.dictionary)
        n = SetofNoIncomingEdges.pop()
        sortedNodes.append(n)
        hcCopyCopy = copy.deepcopy(hcCopy)
        for m in hcCopyCopy.dictionary[n]: #For each node m with edge from n to m
            #print("hcCopy.dictionary[n], m:", hcCopy.dictionary[n], m)
            hcCopy.dictionary[n].remove(m)
            #print("hcCopy.dictionary[n].remove(m)", hcCopy.dictionary, n, m)
            if not( m in hcCopy.dictionary.values()): #If m has no other incoming edges
                SetofNoIncomingEdges.add(m)
            
    #If graph has edges
    #print("hcCopy.dictionary after running cycle checker algorithm", hcCopy.dictionary)
    for node in hcCopy.dictionary:
        #print("node: ", node, "hcCopy.dictionary[node]", hcCopy.dictionary[node])
        if len(hcCopy.dictionary[node]) > 0:
            print("GRAPH HAS A CYCLE remaining node = ", node)
            return True
    #print("Topologically sorted list:", sortedNodes)
    return False #no cycles
            
def getSetofNoIncomingEdges(hc):
    """Return a set of all the nodes with no incoming edges. e.g. hc with '00' -> '01' should not return '01'
    """
    S = set()
    SIZE = hc.CUBEDIM
    for i in range(2**SIZE):
        i_s = int2binaryStr(i,SIZE)
        S.add(i_s)
    for connections in hc.dictionary.values():
        for j in connections:
            S.discard(j) #Remove any node that has at least one incoming connection from ANY node
    return S
    
def isIsomorphicDuplicate(hcL, hc):
    """checks if hc is an isomorphism of any of the hc's in hcL
    Returns True if hcL contains an isomorphism of hc
    Returns False if it is not found"""
    #for each cube in hcL, check if hc could be isomorphic
    #if it could be isomorphic, then check if it is
    #if it is isomorphic, then return True
    #if all comparisons have been made already, then it is not an isomorphism and return False
    
    for saved_hc in hcL:
        if nx.faster_could_be_isomorphic(saved_hc, hc):
            if nx.is_isomorphic(saved_hc, hc):
                return True
    return False
    
def convertMyHC_nxHC(hc):
    """Pass in a hybercube object, return nxHC (a graph from networkx egg)
    
    """
    nxHC = nx.DiGraph()
    
    for node in hc.dictionary.keys():
        for connectedNode in hc.dictionary[node]:
            nxHC.add_edge(node, connectedNode)
        
    return nxHC