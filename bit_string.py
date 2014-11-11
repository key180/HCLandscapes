# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:32:36 2014
Helpful bitstring functions
@author: maxwell.mckinnon
"""

def invertBitStr(iStr):
    """Inverts bits in bitstr e.g. "011" returns "100" """
    invStr = ""
    for i in iStr:
        if i == "0":
            invStr += "1"
        if i == "1":
            invStr += "0"
    return invStr
    
def bitcount(iStr):
    """Count the number of '1' bits inbitstring i. ie 9 = 1001, bc(9) = 2"""
    numberOfOnes = iStr.count('1')
    return numberOfOnes
    
def int2binaryStr(i, size = -1):
    """integer, pad with zeros to make total size this length integer pad if possible. If size == -1, then return non-padded
    converts a positive integer to a string of the binary representation, 9 = "1001", returns "E" if negative integer,
    Can only pad with zeros, can't reduce answer string to certain size
    """
    r = 0
    binaryStr = ""
    if i < 0:
        return "E"
    while 1:
        r = i%2
        i = int(i/2)
        binaryStr = str(r)+binaryStr
        if i == 0:
            break

    if size == -1:
        #zeros_needed = len(binaryStr)
        #binaryStr = '0' * zeros_needed + binaryStr
        return binaryStr
    #Pad with zeros to match number of bits in mask and other genes
    zeros_needed = size - len(binaryStr)
    binaryStr = '0' * zeros_needed + binaryStr
    return binaryStr
    
def binaryStr2int(strg):
    sum = 0
    power = 0
    while(1):
        if len(strg) < 1:
            break
        pop = strg[-1]
        strg = strg[:-1]
        sum += int(pop) * 2**power
        power += 1
    return sum