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
		proteinName = "files/1ajx.pdb"
		ligandName = "files/ligand.pdb"

		protein = PDBReader( proteinName )
		experimental = PDBReader( ligandName )

		print len( protein.atoms )
		print len( ligand.atoms )

		'''aminoPhiPsi = AminoPhiPsi( name )

		aminoPhiPsi.adjustOmegas()
		print "Omega", aminoPhiPsi.getOmegas()
		aminoPhiPsi.adjustPeptideBonds()
		
		pis = [[2*math.pi, 0.78766641318045494], [1.9619568954480233, -0.3926234782058633], [2.8972257829426411, 2.392633396637823], [-2.8523435162747171, 0.72494244869207547], [-3.0785316739166211, -0.22173366098256864], [-0.25380223822002446, 3.1156954233232712], [-0.265604738452486, -2.9423963187754865], [-1.1518136260623859, -2.3575016094821897], [-1.1361907208868818, -1.9858385654213251], [-0.65731885163558434, 2.3099062538169877], [-0.91206294478395966, -1.9296740354450992], [1.6371569283481886, 0.39174957372689168], [1.3228419331070986, -2.6193279409384869], [0.012010356882607542, -0.11397529817012808], [-1.7439758400705712, 2.6277230323945941], [-0.32066427317354362, 0.064963736914675163], [-1.1601808993336808, 2.3989325371272372], [2.4038821049421131, -2.0686758680423685], [-1.2149707121270155, -1.1060392531148531], [2.8269253417981117, 2*math.pi]]

		aminoPhiPsi.adjustPhiPsi()
		print "Phi e Psi", aminoPhiPsi.getPhiPsi()
		aminoPhiPsi.writeAngles()
		aminoPhiPsi.plotRamanchandran()
		print "OK - The file 'aminoPhiPsi.txt' with the dihedral angles by amino acid was generated."
		print "OK - The file 'ramachandran.png' with the ramachandran map was generated."
		aminoPhiPsi.writePDBFile( "1L2Y-P.pdb" )

		aminoPhiPsi.adjustPhiPsi( pis )
		aminoPhiPsi.writePDBFile( "1L2Y-F.pdb" )'''
		'''self.readFiles( "files/1L2Y.pdb", "1L2Y-P.pdb" )
		self.calcRMSD()
		self.calcKabschRMSD()

		print( len( self.experimental.atoms ), len( self.modified.atoms ) )
		params = ['psi1', 'phi2', 'psi2', 'phi3', 'psi3', 'phi4', 'psi4', 'phi5', 'psi5', 'phi6', 'psi6', 'phi7', 'psi7', 'phi8',\
				  'psi8', 'phi9', 'psi9', 'phi10', 'psi10', 'phi11', 'psi11', 'phi12', 'psi12', 'phi13', 'psi13', 'phi14', 'psi14',\
				  'phi15', 'psi15', 'phi16', 'psi16', 'phi17', 'psi17', 'phi18', 'psi18', 'phi19', 'psi19', 'phi20']
		acor = ACOR( self.experimental, self.modified, params, False, 1 )
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