# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 14:25:22 2016

@author: Omer Javed
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import itertools as it
import time

L= 32000
k = 7

def genSeq(L):
    dnaSeq= "".join(random.choice('GATC') for _ in range(L))
    #print "genome sequence  of length ", L ,"",dnaSeq
    return dnaSeq

def kmer(k):
    combination= it.product("TACG", repeat=k)
    permutseq = list("".join(i) for i in combination)
    #print "No of k-mers are = ", len(permutseq)
    #print permutseq
    return permutseq

def matchedKmers(dnaSeq, permutseq):
    count = 0
    final=[]

    for seq in permutseq:
        count = dnaSeq.count(seq)
        final.append([seq, count])
    #print final
    for i in final:
        ''' print i ''' 
t=[]
a1=[]  

dnaSeq = genSeq(L)
for Kval in range(k):
    start_time = time.clock()
    permutseq=kmer(Kval)
    matchedKmers(dnaSeq, permutseq)
    total_time = time.clock() - start_time
    a1.append(Kval)
    t.append(total_time)
        #print a1,t
print a1,t       
plt.plot(a1,t,color="red")
