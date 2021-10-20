# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:47:53 2020

@author: Shaan
"""
import time
start_time = time.time()

def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = nlist = [1, 9, 11, 11, 13, 14, 14, 21, 27, 32, 32, 34, 34, 41, 43, 45, 46, 55, 55, 55,55,55,55,55,55, 57, 64, 64, 64, 64, 65, 70, 83, 86, 94, 95, 96, 97, 98, 98, 99, 99, 100, 101,101,101,101,101]
selectionSort(nlist)
print(nlist)

print("--- %s seconds ---" % (time.time() - start_time))