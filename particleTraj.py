# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:55:16 2023

@author: student
"""
import numpy as np

G = 1

class Particles(object):
    
    def __init__(self, posx, posy, posz, vx, vy, vz, m):
        self.x = posx
        self.y = posy
        self.z = posz
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m = m
        
    def findDistance(self, particle2):
        deltaX = self.x - particle2.x
        deltaY = self.y - particle2.y
        deltaZ = self.z - particle2.z
        
        return np.sqrt(np.power(deltaX, 2) + np.power(deltaY, 2) + np.power(deltaZ, 2)), np.array([deltaX, deltaY, deltaZ])
    
    def acceleration(self, particle2):
        rMag, rVec = self.findDistance(particle2)
        acc = ((G * particle2.m)/np.power(rMag, 3)) * rVec
        return acc
    
    def __repr__(self):
        x = self.x
        y = self.y
        z = self.z
        
        pos_str = f'Position: {x}, {y}, {z}'
        mass = self.m
        
        return f'Mass: {mass}. {pos_str}'
        
    
    
    


        
        
    

