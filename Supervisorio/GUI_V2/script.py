def func(): 
	import math 
	
	t = range(100) 		
	series = [[math.sin(i/10) for i in t], [math.cos(i/10) for i in t]] 		
	header = ["seno", "cosseno"] 
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