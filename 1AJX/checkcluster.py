def checkcluster(size_X,size_Y,size_Z, off0, off1, off2):
	#print off0
	#print off1
	#print off2
	
	#####centro	
	if((off0>=(size_X*(-1)/6) and off0<(size_X/6)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y*(1)/6)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=1
	#####centro_esq		
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z/6))): 
		rotulo=2
	#####centro_dir	
	if((off0>=(size_X*(1)/6) and off0<(size_X/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z/6))): 
		rotulo=3	
	#####centro_frente
	if((off0>=(size_X*(-1)/6) and off0<(size_X/6)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=4
	#####centro_tras
	if((off0>=(size_X*(-1)/6) and off0<(size_X/6)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))):
		rotulo=5	
	#####centro_diagonal1
	if((off0>=(size_X*(1)/6) and off0<(size_X/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=6
	#####centro_diagonal2 
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=7
	#####centro_diagonal3
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=8
	#####centro_diagonal4
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1>=(size_Y*(-1)/6) and  off1<(size_Y/6)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=9
	#####cima_centro	
	if((off0>=(size_X*(-1)/6) and off0<(size_X/6)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=10
	#####cima_esq
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=11
	#####cima_dir
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z/6))): 
		rotulo=12
	#####cima_frente
	if((off0>=(size_X*(-1)/6) and off0<(size_X*(1)/6)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=13
	#####cima_tras
	if((off0>=(size_X*(-1)/6) and off0<(size_X*(1)/6)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=14
	#####cima_diagonal1
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=15
	#####cima_diagonal2
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=16
	#####cima_diagonal3
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=17
	#####cima_diagonal4
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1>=(size_Y*(1)/6) and  off1<(size_Y/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=18
	#####baixo_centro	
	if((off0>=(size_X*(-1)/6) and off0<(size_X*(1)/6)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=19
	#####baixo_esq
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=20
	#####baixo_dir
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(-1)/6) and off2<(size_Z*(1)/6))): 
		rotulo=21
	#####baixo_frente
	if((off0>=(size_X*(-1)/6) and off0<(size_X*(1)/6)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=22
	#####baixo_tras
	if((off0>=(size_X*(-1)/6) and off0<(size_X*(1)/6)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=23
	#####baixo_diagonal1
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=24
	#####baixo_diagonal2
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2<=(size_Z*(-1)/6) and off2>(size_Z*(-1)/2))): 
		rotulo=25
	#####baixo_diagonal3
	if((off0<=(size_X*(-1)/6) and off0>(size_X*(-1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=26
	#####baixo_diagonal4
	if((off0>=(size_X*(1)/6) and off0<(size_X*(1)/2)) and (off1<=(size_Y*(-1)/6) and  off1>(size_Y*(-1)/2)) and (off2>=(size_Z*(1)/6) and off2<(size_Z*(1)/2))): 
		rotulo=27
	#print rotulo
	return rotulo
