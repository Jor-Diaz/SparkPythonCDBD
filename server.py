import socket
from time import time
import random
import sys

def generar_evento(eventos_segundo,cant_atributos):
    mensaje=[]
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
        mensaje.append(atributos)
        print("[°] Nuevo Caso Registrado: " + atributos)
    return mensaje

def send_tweets_to_spark(tcp_connection):
    eventos = generar_evento(5,10)    
    for evento in eventos:
        try:                    
            tcp_connection.send((evento + '\n').encode())
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)


#49152-6535 puertos disponibles
port = 9090 #Puerto ocupado en TCP
BUFFER_SIZE = 2048 
MAQUINA="localhost"
TCP_SOCKET_SERVIDOR=socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creamos un objeto socket tipo TCP
TCP_SOCKET_SERVIDOR.bind((MAQUINA, port)) 
TCP_SOCKET_SERVIDOR.listen(1) # Esperamos la conexión del cliente 
print('[°] Conexión abierta. Escuchando solicitudes en el puerto ' +str(port)) 
TCP_SOCKET_CLIENTE, addr = TCP_SOCKET_SERVIDOR .accept() # Establecemos la conexión con el cliente 
print('[°] Conexión establecida con el cliente')
time_aux=time() 
while True:
    if time()-time_aux>1:
        time_aux=time()    
        send_tweets_to_spark(TCP_SOCKET_CLIENTE)
        print("\n")
        print("[°] Datos Enviados a Spark ")
        print("\n")
print("[°] Apagando servidor")       
TCP_SOCKET_CLIENTE.close()#terminamos la conexion TCP

