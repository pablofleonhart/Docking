from math import *
from decimal import *
import urllib
import os
import sys
#from funcoes import *
from disturbance import *
from rmsd import *
import random
import copy
import commands
import string
ligand=[]
referencia=[]

path = ""
print " DOCKING STARTED "
a = commands.getstatusoutput('./vina --config config.txt --score_only')
energiaVina = string.split(string.split(a[1],"Affinity:")[1])[0]
print "------------------"
print "Energia inicial:"+energiaVina
print "------------------"
refFile = open(path+"config.txt", "r")
var = True
while var:
	bufferLine = refFile.readline().split()
	if(bufferLine[0] == "center_x"):
		center_X = float(bufferLine[2])
	if(bufferLine[0] == "center_y"):
		center_Y = float(bufferLine[2])
	if(bufferLine[0] == "center_z"):
		center_Z = float(bufferLine[2])
	if(bufferLine[0] == "size_x"):
		size_X = float(bufferLine[2])
	if(bufferLine[0] == "size_y"):
		size_Y = float(bufferLine[2])
	if(bufferLine[0] == "size_z"):
		size_Z = float(bufferLine[2])
	if(bufferLine[0] == "out"):
		var = False


################################################################################gera um individuo = vetor(translacao, rotacao, conformacao do ligante)
def  gerarInd(size_X,size_Y,size_Z):
	numero = size_X*(-1)/2
	deltaX = random.uniform(size_X*(-1)/2,size_X/2)
	deltaY = random.uniform(size_Y*(-1)/2,size_Y/2)
	deltaZ = random.uniform(size_Z*(-1)/2,size_Z/2)
	anguloRot = random.uniform(-pi, pi)
	theta1 = random.uniform(-pi/4, pi/4)
	theta2 = random.uniform(-pi/4, pi/4)
	theta3 = random.uniform(-pi/4, pi/4)
	theta4 = random.uniform(-pi/4, pi/4)
	theta5 = random.uniform(-pi/4, pi/4)
	theta6 = random.uniform(-pi/4, pi/4)
	theta7 = random.uniform(-pi/4, pi/4)
	theta8 = random.uniform(-pi/4, pi/4)
	theta9 = random.uniform(-pi/4, pi/4)
	theta10 = random.uniform(-pi/4, pi/4)
	ind = (deltaX, deltaY, deltaZ, anguloRot, theta1,theta2,theta3,theta4,theta5,theta6,theta7,theta8,theta9,theta10)
	return ind

################################################################################
def  calcEnergy():
	path = ""
	
	a = commands.getstatusoutput('./vina --config config.txt --score_only')
	energiaVina = string.split(string.split(a[1],"Affinity:")[1])[0]
	
	return float(energiaVina)

################################################################################
def CrossOverNovo1(parentA,parentBC):
	lenA = int(len(parentA))
	numRfromA = random.randint(int(lenA*.5),int(lenA*0.7))
	offspring = []
	listFromA = []
	while (len(listFromA) < numRfromA):
		x = random.randint(0,lenA-1)
		if x not in listFromA:
			listFromA.append(x)
	for j in range(lenA):
		if j in listFromA:
			offspring.insert(j,parentA[j])
		else:
			offspring.insert(j,parentBC[j])
	return offspring
################################################################################
def checkPop(offspring,population):
    for k in range(len(population)):
        if offspring == population[k][0]:
            return -1            
    return 0
################################################################################

#################################################################################GENETICO

#pop = 150
classA = 30
classB = 75
classC = 45
n_generations = 1000

population = []
score = []
print "------------------"
print "Populacao inicial:"

for individual in range(0, classA + classB + classC):
	ind = gerarInd(size_X,size_Y,size_Z)
	disturbance(ind[0], ind[1], ind[2],ind[3], ind[4],ind[5],ind[6],ind[7],ind[8],ind[9],ind[10],ind[11],ind[12],ind[13])
	score = calcEnergy()
	print 'Energia: ' + str(score)
	population.append([ind, score])
	population.sort(key = lambda x: x[1]) #Sorts the population by the score

#print classA + classB + classC
print "------------------"
print "Tamanho da Populacao: " + str(len(population))
print "------------------"

print("BRKGA STARTED:")
for generation in range(n_generations):
	print "Geracao "+ str(generation+1) + ":"
	new_population = []
# CASTA A:::::::::::::::::::::::::::::::::::::::::::::::::::::	
	for individual in range(classA):
		#print "Populacao inicial: " + str(population[individual][1])
		new_population.append(copy.deepcopy(population[individual]))
# CASTA A:::::::::::::::::::::::::::::::::::::::::::::::::::::

# CASTA B:::::::::::::::::::::::::::::::::::::::::::::::::::::
	indCastaB= classA
	while (indCastaB<(classA+classB)): 
		offspring = []
		parentA = random.randint(0, classA - 1)            
		parentBC = random.randint(classA, classA + classB + classC - 1)
		offspring = CrossOverNovo1(population[parentA][0],population[parentBC][0])	
		if (checkPop(offspring,new_population) == -1): continue
		disturbance(offspring[0], offspring[1], offspring[2],offspring[3], offspring[4], offspring[5], offspring[6],offspring[7],offspring[8],offspring[9],offspring[10],offspring[11], offspring[12],offspring[13])
		score = calcEnergy()
		new_population.append([offspring, score])
		indCastaB+=1
# CASTA B:::::::::::::::::::::::::::::::::::::::::::::::::::::

# CASTA C::::::::::::::::::::::::::::::::::::::::::::::::::::
	for i in range(classA+classB,classA+classB+classC):
		ind = gerarInd(size_X,size_Y,size_Z)
		disturbance(ind[0], ind[1], ind[2],ind[3],ind[4],ind[5],ind[6],ind[7],ind[8],ind[9],ind[10],ind[11],ind[12],ind[13])
		score = calcEnergy()
		new_population.append([ind, score])
# CASTA C::::::::::::::::::::::::::::::::::::::::::::::::::::
	

	population = copy.deepcopy(new_population)
	population.sort(key = lambda x: x[1]) #Sorts the population by the score
	for k in range(20):
		print population[k][1]

	#disturbance(population[0][0][0],population[0][0][1],population[0][0][2],population[0][0][3],population[0][0][4],population[0][0][5],population[0][0][6],population[0][0][7],population[0][0][8],population[0][0][9],population[0][0][10],population[0][0][11],population[0][0][12],population[0][0][13])
	#name1 = 'ligand.pdbqt'
	#name2 = '1AJV/ligand.pdbqt'
	#rmsd(name1,name2)
	#print population[0][0][0]
	#print population[0][0][0]
	arq = open('results.txt', 'a')
	arq.write(str(population[0])+'\n')
	arq.close()
	
disturbance(population[0][0][0],population[0][0][1],population[0][0][2],population[0][0][3],population[0][0][4],population[0][0][5],population[0][0][6],population[0][0][7],population[0][0][8],population[0][0][9],population[0][0][10],population[0][0][11],population[0][0][12],population[0][0][13])
del new_population
#print population[0:9]
#################################################################################GENETICO

