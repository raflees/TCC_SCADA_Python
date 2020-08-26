def func(): 
	


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