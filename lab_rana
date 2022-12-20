#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  first_multiple_input = input().rstrip().split()
  n = int(first_multiple_input[0])
  m = int(first_multiple_input[1])
  k = int(first_multiple_input[2])

  board = [list(input()) for _ in range(n)]
 # for n_itr in range(n):
  #  row = [list(input())]
 
  dict_salida = dict()
# Write your code here
  for k_itr in range(k):
    second_multiple_input = input().rstrip().split()
    i1 = int(second_multiple_input[0]) - 1
    j1 = int(second_multiple_input[1]) - 1
    i2 = int(second_multiple_input[2]) - 1
    j2 = int(second_multiple_input[3]) - 1
    dict_salida[(i1,j1)]=(i2,j2)
    dict_salida[(i2,j2)]=(i1,j1)

  estado = [(-1,-1)] # la rana muere
  dict_estado = dict()
  probabilidad = [0.0]
  s_init = -1
  transicion = [[(0,1.0)]]

  for i1 in range(n):
    for j1 in range(m):
      x = board[i1][j1]
      if x in ["A", "%", "O"]:

        dict_estado[(i1,j1)] = len(estado)
        estado.append((i1,j1))

      elif x in ["#","*"]:
        
        dict_estado[(i1,j1)] = 0

      else:
                
        assert False, x

  for i1 in range(n):
   for j1 in range(m):
     x = board[i1][j1]
     estado_idx = dict_estado[(i1,j1)]
     if x in ["A", "%", "O"]:     
       if x == "A" :
          s_init = estado_idx
          probabilidad.append(0.0)    
       elif x == "%" :
         probabilidad.append(1.0)
         transicion.append([(estado_idx, 1.0)])     
       elif x == "O" :
         probabilidad.append(0.0)
 
       else:
         assert  False, x

       if x in ["A", "O"]:
         i2,j2 = dict_salida[(i1,j1)] if (i1,j1) in dict_salida else (i1,j1)
   
         exito = []
         muertes = 0 
         for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
           i3,j3 = i2 + a , j2 + b
          
           if (0 <= i3 < n) and (0 <= j3 < m):
             posicion = board[i3][j3]
             if posicion in ["A", "%", "O"]:
               exito.append((i3,j3))
             elif posicion == "*":
               muertes += 1

         if len(exito) == 0:
           transicion.append([(0,1.0)])
         else:
           r = [(dict_estado[d], 1 / (len(exito) + muertes)) for d in exito]
           if muertes > 0:
             r.append((0, muertes/(len(exito)+muertes)))           
           transicion.append(r)
  while True:
    posicion_antigua = probabilidad.copy()
    for e in range(len(estado)):
      x = 0.0
      for e2, prob in transicion[e]:
      
        x += probabilidad[e2] * prob
      probabilidad[e] = x
    keep_going = False
    for e3 in range(len(estado)):
            if abs(probabilidad[e3] - posicion_antigua[e3]) > 1e-10:
                keep_going = True
                break
    if not keep_going:
            break

  print(probabilidad[s_init])
