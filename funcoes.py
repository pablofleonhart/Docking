from decimal import *
########################################################
def TransladaPraRef(individuo, primeiro, referencia):
	A = [[1,0,0,((referencia[0]) -(primeiro[0]))],
		 [0,1,0,((referencia[1])-(primeiro[1]))],
		 [0,0,1,((referencia[2])-(primeiro[2]))],
		 [0,0,0,1]]
	B = [[float(individuo[0])],
		 [float(individuo[1])],
		 [float(individuo[2])],
		 [1]]
	C = AxB(A,B)
	
	return C
#multiplica matrizes
def AxB(A, B):   
	A_linhas = len(A)
	A_colunas = len(A[0])
	B_linhas = len(B)
	B_colunas = len(B[0])
	if A_colunas == B_linhas:
		comum = A_colunas
		M = [[sum(A[m][n] * B[n][p] for n in range(comum)) \
			for p in range(B_colunas)] for m in range(A_linhas)]
		return M
	else:
		return -1
def Trans(referencia, origem):
	A = [((referencia[0]) -(origem[0])),
		((referencia[1])-(origem[1])),
		((referencia[2])-(origem[2]))]
	return A
#########################################################
def create_PDB_ligand(molecula, amino, numero, coorX, coorY, coorZ, newname):
	path = "/home/eduardo/Dropbox/Mestrado/Docking/"
#	newname = "new.pdb"
	endFile = open(path+str(newname),"w")
    	endFile.seek(0)

	
	for i in range(0,len(coorX)):
		if(len(molecula[i])<4):
			endFile.write("{0:6}".format("HETATM")+"{0:>5}".format(str(i+1))+"  "+"{0:<4}".format(molecula[i])+"{0:4}".format(amino[i])+"A"+"{0:>4}".format(str(numero[i]))+"    "+"{0:>8}".format(str(Decimal(coorX[i]).quantize(Decimal('1.000'))))+"{0:>8}".format(str(Decimal(coorY[i]).quantize(Decimal('1.000'))))+"{0:>9}".format(str(Decimal(coorZ[i]).quantize(Decimal('1.000')))+"\n"))
		else:
			endFile.write("{0:6}".format("HETATM")+"{0:>5}".format(str(i+1))+" "+"{0:<5}".format(molecula[i])+"{0:4}".format(amino[i])+"A"+"{0:>4}".format(str(numero[i]))+"    "+"{0:>8}".format(str(Decimal(coorX[i]).quantize(Decimal('1.000'))))+"{0:>8}".format(str(Decimal(coorY[i]).quantize(Decimal('1.000'))))+"{0:>9}".format(str(Decimal(coorZ[i]).quantize(Decimal('1.000')))+"\n"))
	endFile.write("END")
	endFile.close()
#########################################################
def create_PDB_macro(molecula, amino, numero, coorX, coorY, coorZ, newname):
	path = "/home/eduardo/Dropbox/Mestrado/Docking/"
#	newname = "new.pdb"
	endFile = open(path+str(newname),"w")
    	endFile.seek(0)

	
	for i in range(0,len(coorX)):
		if(len(molecula[i])<4):
			endFile.write("{0:6}".format("ATOM")+"{0:>5}".format(str(i+1))+"  "+"{0:<4}".format(molecula[i])+"{0:4}".format(amino[i])+"A"+"{0:>4}".format(str(numero[i]))+"    "+"{0:>8}".format(str(Decimal(coorX[i]).quantize(Decimal('1.000'))))+"{0:>8}".format(str(Decimal(coorY[i]).quantize(Decimal('1.000'))))+"{0:>9}".format(str(Decimal(coorZ[i]).quantize(Decimal('1.000')))+"\n"))
		else:
			endFile.write("{0:6}".format("ATOM")+"{0:>5}".format(str(i+1))+" "+"{0:<5}".format(molecula[i])+"{0:4}".format(amino[i])+"A"+"{0:>4}".format(str(numero[i]))+"    "+"{0:>8}".format(str(Decimal(coorX[i]).quantize(Decimal('1.000'))))+"{0:>8}".format(str(Decimal(coorY[i]).quantize(Decimal('1.000'))))+"{0:>9}".format(str(Decimal(coorZ[i]).quantize(Decimal('1.000')))+"\n"))
	endFile.write("END")
	endFile.close()
#############################################################
def create_PDBQT(ligand):
	print ligand
	path = "/home/eduardo/autodock_vina/bin/"
	endFile = open(path+'ligand.pdb',"w")
    	endFile.seek(0)
	for i in range(len(ligand)):
		print ligand[i]
		endFile.write(ligand)
	endFile.write("END")
	endFile.close()

