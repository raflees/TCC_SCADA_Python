def func(): 
	s=[] 
	for t in range(100): 
		s.append(t**2) 
	return s, range(100), [['Header1'],]


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