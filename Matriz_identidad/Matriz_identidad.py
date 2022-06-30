# -*- coding: utf-8 -*-
"""
@author: Santiago Ramirez
"""
def matidentidad(n):    
    try:
        identidad=[]
        for i in range(n):
            identidad.append(n*[0])
        for i in range(len(identidad)):
            identidad[i][i]=1
    except:
        pass
    return identidad
n=20
for i in (matidentidad(n)):
    print(i)

    
    
    
    
    
    
    