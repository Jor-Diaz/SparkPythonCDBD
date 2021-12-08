import socket
from time import time
import random

def generar_evento(eventos_segundo,cant_atributos):
	mensaje=""
	prob=6
	for i in range(0,eventos_segundo):		
		atributos=""
		for j in range(0,cant_atributos):
			aux=random.randint(1,10)
			aux_constructor=""
			if j+1!=cant_atributos:
				aux_constructor="-"			
			if aux>prob:				
				atributos+=str(j)+aux_constructor					
		mensaje+="|"+atributos
	return mensaje

	
def main(eventos_segundo,cant_atributos,TCP_SOCKET_CLIENTE):
	print("[°] Iniciando Generador de Eventos")
	time_aux=time()
	while True:
		if time()-time_aux>1:
			time_aux=time()
			eventos = generar_evento(eventos_segundo,cant_atributos)
			TCP_SOCKET_CLIENTE.send(eventos.encode())
			print("[°]",time_aux,"-",eventos)
	return

#49152-6535 puertos disponibles
host='localhost'
port = 9090 #Puerto ocupado en TCP
BUFFER_SIZE = 2048

TCP_SOCKET_CLIENTE=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos Conexion TCP
TCP_SOCKET_CLIENTE.connect((host, port)) #Nos conectamos al server
opcion=""
print("[°]Conexión establecida con el servidor en el puerto "+str(port))
print("\n")
while True: 
	main(5,10,TCP_SOCKET_CLIENTE)
TCP_SOCKET_CLIENTE.close()#terminamos la conexion 	
print("\n")
print("[°] Conexion TCP terminada")