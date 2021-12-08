import socket

#49152-6535 puertos disponibles
port = 9090 #Puerto ocupado en TCP
BUFFER_SIZE = 2048 
MAQUINA="localhost"
TCP_SOCKET_SERVIDOR=socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creamos un objeto socket tipo TCP
TCP_SOCKET_SERVIDOR.bind(('', port)) 
TCP_SOCKET_SERVIDOR.listen(1) # Esperamos la conexión del cliente 
print('[°] Conexión abierta. Escuchando solicitudes en el puerto ' +str(port)) 
TCP_SOCKET_CLIENTE, addr = TCP_SOCKET_SERVIDOR .accept() # Establecemos la conexión con el cliente 
print('[°] Conexión establecida con el cliente')
while True:    
    # Recibimos bytes, convertimos en str
    data = TCP_SOCKET_CLIENTE.recv(BUFFER_SIZE)       
    mensaje = data.decode()                
    print("\n")
    print('# Mensaje recibido de cliente: {}'.format(data.decode('utf-8')))         
print("[°] Apagando servidor")       
TCP_SOCKET_CLIENTE.close()#terminamos la conexion TCP

