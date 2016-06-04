from io import StringIO
import numpy as np 
import copy

def oneOrZero (number):
	if number == 0:
	    return 0
	else:
		return 1


input_values = input("Введите число уравнений, число переменных и матрицу:").split(" ")

numRow = int(input_values[0])
numVar = int(input_values[1])
matrix = np.array([[float(x) for x in input_values[1+y:numVar+y+2]] for y in range(1,numRow*(numVar+1),numVar+1)] )


for x in range (0,numRow):
    for y in range(x,numVar):
    	if np.equal(matrix[x,y],0):
        	numChange = numRow-1
        	while np.equal(matrix[x,y],0) | np.not_equal(numChange,0):
        		bufLine = copy.deepcopy(matrix[x])
        		matrix[x] = copy.deepcopy(matrix[numChange])
        		matrix[numChange]=copy.deepcopy(bufLine)
        		numChange=-1



coef = 0.0
print(matrix)
for x in range(0, numVar-1):
	for y in range(x,numRow-1):
		coef = matrix[y+1,x]/matrix[x,x]
		matrix[y+1] = matrix[y+1]- matrix[x]*coef
		




answ2 = [1 for x in range(0,numVar+1)]



for x in range(0,numVar):
	sum = 0.0
	counter = numVar - x -1############# 
	while(np.not_equal(counter,numVar)):
		sum = sum + (matrix[numVar-x-1,counter+1]*answ2[counter+1])*oneOrZero(counter-numVar+1)
		counter= counter + 1
	answ2[numVar-x-1] = (matrix[numVar-x-1,numVar] - sum)/matrix[numVar-x-1,numVar-x-1]


for x in range(0,numVar):
	print("x",x+1,"=",answ2[x])



	    	
	    	

