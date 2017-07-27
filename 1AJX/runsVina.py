from math import *
from decimal import *
import urllib
import os
import sys
import random
import copy
import commands
import string
#print "oi"
for i in range(30): 
	a = commands.getstatusoutput('./vina --config config.txt')
	#print a
	energiaVina = string.split(string.split(a[1],"\n   1")[1])[0]
	print energiaVina
	b = commands.getstatusoutput('python vinarmsd.py')
	print b
	ar = open("1AJXresultsVina.txt","a")
	ar.write(str(energiaVina)+" "+str(b[1])+"\n") 
	ar.close()