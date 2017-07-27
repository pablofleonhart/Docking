from funcoes import *
from biopyVector import *
from math import *

def disturbance(deltaX,deltaY, deltaZ, theta_rot,theta1,theta2,theta3,theta4,theta5,theta6,theta7,theta8,theta9,theta10):
	theta=[theta1,theta2,theta3,theta4,theta5,theta6,theta7,theta8,theta9,theta10]
	k=len(theta)
	ligand = []
	vetores = []

	path = ""
	refFile = open(path+"1AJX/ligand.pdbqt", "r")
	
	atoms = True
	while atoms:
		bufferLine = refFile.readline().split()
		#print bufferLine
		if(bufferLine[0]!='TORSDOF'):
			ligand.append(bufferLine)
		elif(bufferLine[0]=='TORSDOF'):
			ligand.append(bufferLine)
			atoms = False

###############################################################################################seleciona o atomo de referencia
	for i in range(len(ligand)): 
		if(len(ligand[i])>2):
			if(ligand[i][2]=='N01'):
				referencia = (float(ligand[i][6]), float(ligand[i][7]), float(ligand[i][8]))	
################################################################################################	

#####################################################################################################conformacao	
	vetor1=[]
	vetor2=[]
	atomos=[]

	for i in range(len(ligand)): #seleciona as branchs dentro do pdb
		if(ligand[i][0]=="BRANCH"):
			vetores.append(ligand[i])

	print vetores
	for j in range(len(vetores)): #busca as coordenadas dos vetores de referencia
		for i in range(len(ligand)):
			if(len(ligand[i])>2):
				if(ligand[i][0]=="HETATM" and ligand[i][1] == vetores[j][1]):	
					vet1 =  (float(ligand[i][6]),float(ligand[i][7]),float(ligand[i][8]))
					vetor1.append(vet1)
				if(ligand[i][0]=="HETATM" and ligand[i][1] == vetores[j][2]):	
					vet2 =  (float(ligand[i][6]),float(ligand[i][7]),float(ligand[i][8]))
					vetor2.append(vet2)

	print "v1", vetor1, "v2", vetor2
	origem = (0.0,0.0,0.0)	
	for i in range(len(vetor1)): # monta o vetor referencia,
		vetRef = (vetores[i][1],vetores[i][2],vetor1[i][0]-vetor2[i][0],vetor1[i][1]-vetor2[i][1],vetor1[i][2]-vetor2[i][2])
		print vetRef
		for j in range(len(ligand)):
				if(len(ligand[j])>2):
					if (ligand[j][0]=="BRANCH" and ligand[j][1]==vetRef[0] and ligand[j][2]==vetRef[1]): #seleciona atomos referentes a cada vetor
						#print ligand[j]
						#print vetRef
						aux=j+1
						k=k-1
						#print k	
						while(ligand[aux][0]!="ENDBRANCH" and ligand[j][1]==vetRef[0] and ligand[j][2]==vetRef[1]):
							if(ligand[aux][0]=="HETATM"): #translada, rotaciona e translada novamente cada atamo
								print ligand[aux]
								ref = (float(vetor1[i][0]), float(vetor1[i][1]), float(vetor1[i][2]))
								#print "Referencia: " + str(referencia)
								matriz = TransladaPraRef([ligand[aux][6], ligand[aux][7], ligand[aux][8]], ref, origem)
								ligand[aux][6] = float(matriz[0][0])
								ligand[aux][7] = float(matriz[1][0])
								ligand[aux][8] = float(matriz[2][0])
								
								vetorRef = Vector(vetRef[2],vetRef[3],vetRef[4])
								mRotacao = rotaxis2m(theta[k], vetorRef)

								point = [[ligand[aux][6]],[ligand[aux][7]],[ligand[aux][8]]] 
								mRotacionada = AxB(mRotacao, point)
								ligand[aux][6]=mRotacionada[0][0]
								ligand[aux][7]=mRotacionada[1][0]
								ligand[aux][8]=mRotacionada[2][0]

								matriz = TransladaPraRef([ligand[aux][6], ligand[aux][7], ligand[aux][8]], origem, ref)
								ligand[aux][6] = float(matriz[0][0])
								ligand[aux][7] = float(matriz[1][0])
								ligand[aux][8] = float(matriz[2][0])

								#print ligand[aux]
							aux=aux+1
						#print "___________________________________________________________________________"
				
#########################################################################################################conformacao		
	pontos = (deltaX,deltaY, deltaZ)
	origem = (0.0,0.0,0.0)
	
##########################################################################################################rotacao	
	for i in range(len(ligand)): #translada para a origem (a partir do atomo de referencia)
		if(ligand[i][0]=='HETATM'):
			matriz = TransladaPraRef([ligand[i][6], ligand[i][7], ligand[i][8]], referencia, origem)
			ligand[i][6] = float(matriz[0][0])
			ligand[i][7] = float(matriz[1][0])
			ligand[i][8] = float(matriz[2][0])

	for i in range(len(ligand)): #seleciona o vetor de rotacao
		if(len(ligand[i])>2):
			if(ligand[i][2]=='N01'):
				v1 = (float(ligand[i][6]), float(ligand[i][7]), float(ligand[i][8]))
			if(ligand[i][2]=='C02'):
				v2 = (float(ligand[i][6]), float(ligand[i][7]), float(ligand[i][8]))
	x_rot= v1[0]-v2[0]
	y_rot= v1[1]-v2[1]
	z_rot= v1[2]-v2[2]

	vetorRef = Vector(x_rot, y_rot, z_rot)
	mRotacao = rotaxis2m(theta_rot, vetorRef)
	for j in range(len(ligand)): #rotaciona
		if(ligand[j][0]=='HETATM'):
			point = [[ligand[j][6]],[ligand[j][7]],[ligand[j][8]]] 
			mRotacionada = AxB(mRotacao, point)
			#rotated_vector=any_vector.left_multiply(m)
			ligand[j][6]=mRotacionada[0][0]
			ligand[j][7]=mRotacionada[1][0]
			ligand[j][8]=mRotacionada[2][0]

	origem = (float(referencia[0]), float(referencia[1]), float(referencia[2])) #nova origem eh a posicao original do atomo

	for i in range(len(ligand)):
		if(len(ligand[i])>2):
			if(ligand[i][2]=='N01'):
				referencia = (float(ligand[i][6]), float(ligand[i][7]), float(ligand[i][8]))
##########################################################################################################rotacao

##########################################################################################################translacao

	for i in range(len(ligand)):
		#print ligand[i]
		if(ligand[i][0]=='HETATM'):
			matriz = TransladaPraRef([ligand[i][6], ligand[i][7], ligand[i][8]], referencia,origem)
			ligand[i][6] = float(matriz[0][0])
			ligand[i][7] = float(matriz[1][0])
			ligand[i][8] = float(matriz[2][0])
			ligand[i][6] = float(ligand[i][6])+deltaX
			ligand[i][7] = float(ligand[i][7])+deltaY
			ligand[i][8] = float(ligand[i][8])+deltaZ


			ligand[i][1] = "{0:>4}".format(ligand[i][1])
			ligand[i][2] = "{0:>4}".format(ligand[i][2])
			ligand[i][5] = "{0:<6}".format(ligand[i][5])
			ligand[i][6] = "{0:>8}".format(str(Decimal(matriz[0][0]+deltaX).quantize(Decimal('1.000'))))
			ligand[i][7] = "{0:>7}".format(str(Decimal(matriz[1][0]+deltaY).quantize(Decimal('1.000'))))
			ligand[i][8] = "{0:>7}".format(str(Decimal(matriz[2][0]+deltaZ).quantize(Decimal('1.000'))))
			ligand[i][9] = "{0:>5}".format(str(ligand[i][9]))
			ligand[i][11] = "{0:>9}".format(str(ligand[i][11]))
			
	arquivo = open('ligand.pdbqt', 'w')
	for i in range(len(ligand)):
		ligand[i] = '[%s]' % ' '.join(map(str, ligand[i]))
		arquivo.write((ligand[i][1:-1]))
		arquivo.write('\n')
	arquivo.close()
############################################################################################################translacao
#theta_rot = pi/2
disturbance(-9.523083375222923, -10.802515838757866, -0.5384470895419433, 0.16615301401793836, 0.7833202792191596, -0.6940337084321806, -0.7852931750834161, 0.4085130459222477, 0.233631335911322, 0.5687371671335328, -0.4227838797689805, 0.4889349388041575, 0.7447999406847958, -0.7812604843465688)