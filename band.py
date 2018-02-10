# Seniales Band
# 	1. Conectar celular por red usb y activar el bluetooth
# 	2. Abrir SSHelper y BandCompanion
# 	3. Buscar la ip del
# 		3.a ifconfig
# 		3.b sudo nmap -sO 192.168.XX.1/24
# 	4. sudo sshfs -p 2222 admin@192.168.XX.YYY:/data/data/com.arachnoid.sshelper/home/SDCard/CompanionForBand ./band
# 	5. Al final para desmontar la carpeta: umount band

from time import sleep
import sys

# from datetime import datetime
# LAG_ACEPTABLE = 10
# lag = 0
# ultima_hora_recibida = datetime.strptime('23:59:59','%H:%M:%S')
# hora = datetime.strptime(datos[1][-9:-1],'%H:%M:%S')
# if hora <= ultima_hora_recibida:
# 	lag += 1
# 	if lag == LAG_ACEPTABLE:
# 		todo_bien = False
# else:
# 	lag = 0

def enviarValores(tipoData):
	value = 0
	with open('./band/'+tipoData+'/' +tipoData+'_7 feb. 2018.csv','r') as log:
		last_line = log.readlines()[-1]
		dato = last_line.split(',')
		value = float(dato[2].replace("\n", "")[1:-1])
	return value+1*1e-7

def toCSVLine(data):
	stringData = ""
	for value in data:
		stringData += str(value) + ", "
	return stringData[:-2] + "\n"

def save(experimentName, data):
	with open("Data/" + experimentName + ".txt", "a") as file:
		file.write(toCSVLine(data))


def main(argv):
	todo_bien = True

	experimentName = argv[0]

	while(todo_bien):
		try:
			data = [enviarValores('GSR'), enviarValores('SkinTemperature'), enviarValores('HeartRate')]
			save(experimentName, data)
			print data
			sleep(1.0)
		except Exception as e:
			todo_bien = True
			print "Hubo un error: " + str(e)
			pass 

if __name__ == "__main__":
    main(sys.argv[1:])
