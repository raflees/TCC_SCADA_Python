def add_function ():
	num = '[1, 2]'

	num = num.replace('[', '')
	num = num.replace(']', '')
	num = num.replace(',', ' ')
	num = num.strip()

	nums = num.split(' ')
	formatted_nums = '['
	for n in nums:
		if n != '': formatted_nums += str(n) + ' '
	if (len(formatted_nums) > 2): formatted_nums = formatted_nums[:-1]
	formatted_nums += ']'

def import_series_csv_file(path):
		import csv
		import pprint
		import matplotlib.pyplot as plt

		with open(path) as f:
			lines = []
			header = []
			reader = csv.reader(f)
			n_lines = 0
			for line in reader:
				if n_lines == 0 and True:
					header = line
				else:
					lines.append(line)
				n_lines += 1

		series = np.array(lines).astype(np.float)
		time_serie = series.transpose()[0]
		series = (series.transpose()[1:]).transpose()

		pprint.pprint(header)

		return time_serie, series, header[1:]

def script():
	import os
	import pickle
	func = "s=[] \nfor t in range(100): \n\ts.append(t**2) \nreturn s, range(100), [['Header1'],]"
	file = 'teste_script.py'

	try:
		open('teste_script.py', 'x')
	except:
		pass
	with open(file, 'w') as f:
		f.write('def func(): \n')
		lines = func.split('\n')
		for line in lines:
			f.write('\t' + line + '\n')
		f.write('\n\nobj = func() \n')
		f.write('import pickle \ntry: \n\topen("returned_obj", "x") \nexcept: \n\tpass')
		f.write("\nwith open('returned_obj', 'wb') as f: \n\tpickle.dump(obj, f) \n\tf.close() \nexit(0)")
			
	os.system('python ' + file)
	#exit(0)

	with open('returned_obj', 'rb') as f:
		#f.seek(0)
		obj = pickle.load(f)
	print(obj[0])