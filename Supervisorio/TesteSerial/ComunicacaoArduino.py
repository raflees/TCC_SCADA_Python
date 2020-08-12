import time
import serial

def funcErro():
	portaArduino = serial.Serial("COM3", 9600, timeout=1)
	if not portaArduino.is_open:
	    portaArduino.open()

	nlinhas = 1
	linha = ''
	print('Conexao realizada\n')

	time.sleep(2)

	ini = time.time()
	while (time.time() - ini < 20 and nlinhas < 210):
		while(portaArduino.inWaiting() == 0):
			portaArduino.write(str(nlinhas).encode('UTF-8'))	
			print('{0:.2f}s: {1}'.format(time.time() - ini, nlinhas))
			time.sleep(0.02)

		while(portaArduino.inWaiting() > 0):
			linha = portaArduino.readline().decode()
			print(str(linha))

		nlinhas += 1

	print('Conexao fechada (' + str(nlinhas) + ') linha(s) lidas\n')
	portaArduino.close()


funcErro()