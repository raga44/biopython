# -*- coding: utf-8 -*-
"""
Created on Sun Oct 02 14:25:22 2016

@author: Omer Javed
"""
import random
import time
seqf = lambda L: ''.join(random.choice('ATGC') for _ in range(L))

def kmerCount(seq,k = 1):
    D = {}
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        try:
            D[kmer]+=1
        except KeyError:
            D[kmer] = 1
    return D

Ls = [1000,10000,100000,1000000,10000000]
Ks = [1,2,3,4,5]
for L in Ls:
    for k in Ks:
        tmin = 1e10
        for tries in range(5): #Repeat the experiment 5 times!
            random.seed()
            seq = seqf(L)
            t0 = time.time()
            D = kmerCount(seq,k)
            dt = time.time()-t0
            if dt<tmin: #stoe only the minimum time!
                tmin = dt
        
        print "L = %d, k = %d : %f (s)" %(L,k,tmin)
