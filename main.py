from time import time
import random

def generar_evento(eventos_segundo,cant_atributos):
	mensaje=[]
	prob=6
	for i in range(0,eventos_segundo):
		atributos=""
		for j in range(0,cant_atributos):
			aux=random.randint(1,10)
			aux_constructor=""
			if j+1!=cant_atributos:
				aux_constructor=" "			
			if aux>prob:				
				atributos+=str(j)+aux_constructor					
		mensaje.append(atributos)
	return mensaje

	


def main(eventos_segundo,cant_atributos):
	print("[°] Iniciando Generador de Eventos")
	time_aux=time()
	while True:
		if time()-time_aux>1:
			time_aux=time()
			print("[°]",time_aux,"-",generar_evento(eventos_segundo,cant_atributos))
	return

main(5,10)
