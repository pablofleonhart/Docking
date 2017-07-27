from funcEnergy import EnergyFunction
from pdbReader import PDBReader
import math
import numpy as np
import rmsd
import sys

class Builder( object ):
	experimental = None
	modified = None
	mod = None

	def __init__( self ):
		proteinName = "files/macro.pdb"
		ligandName = "files/ligand.pdb"

		protein = PDBReader( proteinName )
		experimental = PDBReader( ligandName )

		print len( protein.atoms )
		print len( experimental.atoms )

		print " DOCKING STARTED "

		e = EnergyFunction()
		print e.getEnergy()

		params = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'theta1', 'theta2', 'theta3', 'theta4', 'theta5', 'theta6', 'theta7', 'theta8', 'theta9', 'theta10']
		'''acor = ACOR( self.experimental, self.modified, params, False, 1 )
		acor.evolve()'''

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