from funcEnergy import EnergyFunction
from pdbReader import PDBReader
from acor import ACOR
import math
import numpy as np
import random
import rmsd
import sys

class Builder( object ):
	experimental = None
	modified = None
	mod = None

	def __init__( self ):
		proteinName = "files/macro.pdbqt"
		expName = "orig_ligand.pdbqt"
		modName = "ligand.pdbqt"

		protein = PDBReader( proteinName )
		experimental = PDBReader( expName )
		modified = PDBReader( modName )

		print experimental.posAtoms

		'''print len( protein.atoms )
		print ( experimental.posAtoms )

		e = EnergyFunction()
		print e.getEnergy()'''

		refFile = open( "config.txt", "r")
		var = True
		while var:
			bufferLine = refFile.readline().split()
			if(bufferLine[0] == "size_x"):
				size_X = float(bufferLine[2])
			if(bufferLine[0] == "size_y"):
				size_Y = float(bufferLine[2])
			if(bufferLine[0] == "size_z"):
				size_Z = float(bufferLine[2])
			if(bufferLine[0] == "out"):
				var = False

		deltaX = random.uniform(size_X*(-1)/2,size_X/2)
		deltaY = random.uniform(size_Y*(-1)/2,size_Y/2)
		deltaZ = random.uniform(size_Z*(-1)/2,size_Z/2)
		anguloRot = random.uniform(-math.pi, math.pi)
		theta1 = random.uniform(-math.pi/4, math.pi/4)
		theta2 = random.uniform(-math.pi/4, math.pi/4)
		theta3 = random.uniform(-math.pi/4, math.pi/4)
		theta4 = random.uniform(-math.pi/4, math.pi/4)
		theta5 = random.uniform(-math.pi/4, math.pi/4)
		theta6 = random.uniform(-math.pi/4, math.pi/4)
		theta7 = random.uniform(-math.pi/4, math.pi/4)
		theta8 = random.uniform(-math.pi/4, math.pi/4)
		theta9 = random.uniform(-math.pi/4, math.pi/4)
		theta10 = random.uniform(-math.pi/4, math.pi/4)

		e = EnergyFunction()
		e.transform( deltaX, deltaY, deltaZ, anguloRot, theta1, theta2, theta3, theta4, theta5, theta6, theta7, theta8, theta9, theta10, 'files/original_ligand.pdbqt' )

		params = ['tx', 'ty', 'tz', 'thetarot', 'theta1', 'theta2', 'theta3', 'theta4', 'theta5', 'theta6', 'theta7', 'theta8', 'theta9', 'theta10']
		acor = ACOR( self.experimental, self.modified, params, False, 200 )
		acor.evolve()

	def readFiles( self, fileA, fileB ):
		self.experimental = PDBReader( fileA )
		self.modified = PDBReader( fileB )

		self.modified.adjustAtoms( self.experimental.atoms, self.experimental.aminoAcids )
		self.experimental.adjustAtoms( self.modified.atoms, self.modified.aminoAcids )

		'''print self.experimental.atoms
		print self.experimental.posAtoms
		print self.modified.atoms
		print self.modified.posAtoms'''

		self.experimental.calcBackbonePos()
		self.modified.calcBackbonePos()
		self.experimental.calcCaPos()
		self.modified.calcCaPos()

	def calcKabschRMSD( self ):
		P = np.array( self.experimental.posAtoms )
		Q = np.array( self.modified.posAtoms )
		#print rmsd.kabsch_rmsd( P, Q )
		P -= rmsd.centroid( P )
		Q -= rmsd.centroid( Q )
		print "{:15s} {:6.2f}".format( "Kabsch RMSD:", rmsd.kabsch_rmsd( P, Q ) )

	def calcRMSD( self ):
		'''print( len( self.experimental.atoms ), len( self.modified.atoms ) )
		print( self.experimental.atoms )
		print( self.modified.atoms )
		print( len( self.experimental.backbone ), len( self.modified.backbone ) )
		print( len( self.experimental.alpha ), len( self.modified.alpha ) )'''

		aligner = PDBAligner()
		print "{:15s} {:6.2f}".format( "CA RMSD:", aligner.calcRMSD( self.experimental.alpha, self.modified.alpha ) )
		print "{:15s} {:6.2f}".format( "Backbone RMSD:", aligner.calcRMSD( self.experimental.backbone, self.modified.backbone ) )
		print "{:15s} {:6.2f}".format( "All atoms RMSD:", aligner.calcRMSD( self.experimental.posAtoms, self.modified.posAtoms ) )

builder = Builder()