def func(): 
	import math 
	
	t = range(180) 		
	series = [[1 for i in t], [0.099 for i in t]] 		
	header = ["hss", "u2ss"] 
	return series, t, header
	


obj = func() 
import pickle 
try: 
	open("returned_obj", "x") 
except: 
	pass
with open('returned_obj', 'wb') as f: 
	pickle.dump(obj, f) 
	f.close() 
exit(0)