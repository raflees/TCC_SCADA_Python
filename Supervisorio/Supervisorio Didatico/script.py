def func(): 
	import control 
	
	sys1 = control.tf([2,], [1, 0.1, 1]) 			
	sys2 = control.tf([1,], [1, 2]) 
	sys = control.series(sys1, sys2) 			
	t = range(100) 
	t, u = control.step_response(control.tf([1,],[10,1]), t) 			
	t, y, x = control.forced_response(sys, t, u) 			
	h = ["u(t)", "y(t)"] 
	return [u, y], t, h


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