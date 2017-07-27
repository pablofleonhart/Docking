import sys
from math import *
from funcoes import *

def rmsd(path,name1,name2):

	ligand = []
	ligand2 = []
	coorX = []
	coorY = []
	coorZ = []
	cX = []
	cY = []
	cZ = []


	refFile = open(path+name1, "r")

	atoms = True
	while atoms:
		bufferLine = refFile.readline().split()
		if(bufferLine[0]!='TORSDOF'):
			ligand.append(bufferLine)
		elif(bufferLine[0]=='TORSDOF'):
			ligand.append(bufferLine)
			atoms = False
	ligand2 = []
	refFile = open(path+name2, "r")
	atoms = True
	while atoms:
		bufferLine = refFile.readline().split()
		if(bufferLine[0]!='TORSDOF'):
			ligand2.append(bufferLine)
		elif(bufferLine[0]=='TORSDOF'):
			ligand2.append(bufferLine)
			atoms = False

	for i in range(len(ligand)):
			if(ligand[i][0]=='HETATM'):
				coorX.append(float(ligand[i][6]))
				coorY.append(float(ligand[i][7]))
				coorZ.append(float(ligand[i][8])) 

	for i in range(len(ligand2)):
			if(ligand2[i][0]=='HETATM'):
				cX.append(float(ligand2[i][6]))
				cY.append(float(ligand2[i][7]))
				cZ.append(float(ligand2[i][8])) 

	soma = 0
	cont = 0
	for i in range(0,len(coorX)):
			dist = sqrt(((coorX[i]-cX[i])**2) + ((coorY[i]-cY[i])**2)+((coorZ[i]-cZ[i])**2))
			soma = soma + dist
			cont += 1
	rmsd = soma/cont
	print "RMSD: " + str(rmsd)
##############################################################################################################
path = ""
name1 = 'ligand.pdbqt'
name2 = '1AJX/ligand.pdbqt'

rmsd(path, name1,name2)
