# -*- coding: utf-8 -*-
#DEV branch
"""
Created on Wed Feb 12 23:03:54 2014

@author: maxwell.mckinnon
"""

from hypercube import *
#from matrice import *
from bit_string import *
import copy
import networkx as nx
import matplotlib.pyplot as plt
from networkx import graphviz_layout

import time

    
tstart = time.ctime()

hcl = getAllHyperCubeConfigs3D() #HCL is a list of all found hypercube configurations, list of objects
nx_hcl = [] # List to put all non cyclical nx versions of hcl hypercubes into
nx_hcl = hcl #fix later
#n = 0
#for hcin in hcl:
#    cycleStatus = hasCycle(hcin)
#    if cycleStatus == True:
#        print("CYCLE FOUND:", hcin.dictionary)
#        n+=1
#    else:
#        nx_hcl.append(convertMyHC_nxHC(hcin))
#    #print("Cycle ==", cycleStatus)
#    
#print("Cycles found:", n)

#print(hcl[0].dictionary)
#newdiG = convertMyHC_nxHC(hcl[0])
#newdiG = nx.from_dict_of_lists(hcl[0].dictionary) #Doesn't work?
#print(newdiG.adj)
#nx.draw(newdiG)

print("hypercubes generated:", len(hcl))
print("hypercubes without cycles:", len(nx_hcl))
print("Time Now:", time.ctime(), "Time Start:", tstart)
print("Dump Memory from hcl")
hlc = 5 #Does this work? tk
print("hcl Dumped")


#i = 0
#d = False

#nx_hcl_copy = copy.deepcopy(nx_hcl) #Can't copy the list without a memory error

#while(not d): #remove graphs that are isomorphic
#    d2 = False
#    j = i + 1
#    while(not d2):
#        print("i,j", i, j)
#        if nx.is_isomorphic(nx_hcl[i],nx_hcl[j]):
#            print("is isomorphic", "i,j", i, j)
#            nx_hcl.remove(nx_hcl[j]) #remove isomorphic graph
#            #DON'T "j+=1" : keep j at the same spot if an element is removed
#        else: # j++ if an element is not removed
#            j += 1
#        if j == len(nx_hcl): #loop until j reaches last element
#            d2 = True
#        
#    print("Length of nx_hcl:", len(nx_hcl))
#    i += 1
#    if i == len(nx_hcl):
#        d = True
        
print("Length of nx_hcl:", len(nx_hcl))
print("Dump of Unique nodes: ")
print("*****")
print("Time of Start of Unique HyperCubes Dump:", time.ctime(), "Time Start:", tstart)

for hc in nx_hcl:
    #print(hc.dictionary)
    print("Nodes", hc.nodes())
    print("Edges", hc.edges())
print("*****")
print("End of dump of Unique HyperCubes")

cnt = 0
for uniqHC in nx_hcl:
    plt.figure()
    
    nx.draw(uniqHC)
    plt.savefig("uniqHC_" + str(cnt))
    plt.close()
    #nx.relabel_nodes(uniqHC, flatten)
    cnt += 1
    
print("Time End:", time.ctime(), "Time Start:", tstart)