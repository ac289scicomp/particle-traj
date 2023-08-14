# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:44:56 2023

@author: student
"""
import numpy as np
import random as rng
from particleTraj import *



def makeCon():
    N = 10
    
    f = open("initial_conditions.txt", 'w')
    
    for i in range(N):
        linestr = ""
        for j in range(6):
            linestr += (str((rng.random() - 0.5) * 100) + ", ")
        
        linestr += str(1000)
        linestr += "\n"
        
        f.write(linestr)
    
    f.close()
def doData(filePath):
    raw_data = open(filePath, 'r') 
    input_str = raw_data.read()
    input_array = input_str.split('\n')
    data = [input_array[i].split(',') for i in range(len(input_array))]
    for i in range(len(data) - 1):
        print(data[i])
        for j in range(len(data[0])):
            if data[i][j] == '':
                data[i][j] = float(0)
            else:     
                data[i][j] = float(data[i][j])
    data = data[:len(data) - 1]
    return data



def putInClass(arr):
    particleData = []
    for i in range(len(arr)):
        particleData.append(Particles(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5], arr[i][6]))
    return particleData

def addAcceleration(particleArr, startingIndex):
    #starting index is the index that is currently being used, if I was 
    #evalutating the total a on index 3,startingIndex would = 3
    length = len(particleArr)
    startingX = 0
    startingY = 0
    startingZ = 0
    for i in range(length):
        if i == startingIndex:
            pass
        else:
            currentA = particleArr[startingIndex].acceleration(particleArr[i])
            Ax = currentA[0]
            Ay = currentA[1]
            Az = currentA[2]
            
            startingX += Ax
            startingY += Ay
            startingZ += Az
    totalAcceleration = np.array([startingX, startingY, startingZ])
    return totalAcceleration

#main body of code
makeCon()
output = doData('initial_conditions.txt')
particleArr = putInClass(output)
lengthPart = len(particleArr)

for i in range(lengthPart):
    accel = addAcceleration(particleArr, i)
    particleArr[i].ax = accel[0]
    particleArr[i].ay = accel[1]
    particleArr[i].az = accel[2]


    
    
    




#output = doData('initial_conditions.txt')
#final = putInClass(output)




        