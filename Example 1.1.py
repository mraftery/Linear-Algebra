# -*- coding: utf-8 -*-

print("Linear Algebra Chapter 1.1")
print("Systems of Linear Equations")

import numpy as np

dim=3

def Replace(target_row,other_row,scale):
    Id=np.eye(dim)
    out=np.matrix(Id)
    out[target_row,:]=Id[target_row,:]+scale*Id[other_row,:]
    return out

def Interchange(row1,row2):
    Id=np.eye(dim)
    out=np.matrix(Id)
    out[row1,:]=Id[row2,:]
    out[row2,:]=Id[row1,:]
    return out
    
def Scale(row,alpha):
    Id=np.eye(dim)
    out=np.matrix(Id)
    out[row,:]=alpha*Id[row,:]
    return out
    
A=np.array([[1,-2,1,0],
            [0,2,-8,8],
            [5,0,-5,10]])
            
print("Matrix notation for Ex 1.1")
print(A)

print("Note: Python begins index count at 0")
print("Step 1:")
print("Replace-5*A[0,] to A[2,]")
print("Add -5 times eqn 1 to eqn 3")
A1=np.dot(Replace(2,0,-5),A)
print(np.array(A1, dtype=int))

print("Step 2:")
print("Scale A[1,] by 1/2")
print("Multiply eqn 2 by 1/2")
A2=np.dot(Scale(1,.5),A1)
print(np.array(A2, dtype=int))

print("Step 3:")
print("Replace -10*A[1,] to A[2,]")
print("Adds -10 times eqn 2 to eqn 3")
A3=np.dot(Replace(2,1,-10),A2)
print(np.array(A3, dtype=int))

print("Step 4:")
print("Scale A[2,] by 1/30")
A4=np.dot(Scale(2,1/30.),A3)
print(np.array(A4, dtype=int))

print("Step 5:")
print("Replace 4*A[2,] to A[1,]")
A5=np.dot(Replace(1,2,4),A4)
print(np.array(A5, dtype=int))

print("Step 6:")
print("Replace -1*A[2,] to A[0,]")
A6=np.dot(Replace(0,2,-1),A5)
print(np.array(A6, dtype=int))

print("Step 7:") 
print("Replace 2*A[1,] to A[0,]")
A7=np.dot(Replace(0,1,2),A6)
print(np.array(A7, dtype=int))

# print("Note":)
# print("The Python function numpy.linalg can solve system of linear eqns")

# A = np.array([[1,-2,1],[0,2,-8],[5,0,-5]])
# B = np.array([0,8,10])
# x=np.linalg.solve(A,B)
# print(np.array(x, dtype=int))
