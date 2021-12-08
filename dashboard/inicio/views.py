from django.shortcuts import render
import json

def inicio(request):
	import os
	context={}
	aux = os.listdir('..\\..\\results')
	context["data"]=aux
	return render(request,'index.html',context)

def ver(request):
	import os
	context={}
	path="..\\..\\results\\"+request.GET.get('u')
	print(path)
	file = open(path,"r")
	data = json.load(file)    
	context["n_resultados"]=data["n_results"]
	context["n_closures"]=data["n_closures"]
	context["exec_time"]=data["exec_time"]
	aux=data["data"]
	lineas=[]
	for i in aux:
		aux1=i.replace("frozenset","")
		lineas.append(aux1)
	context["lineas"]=lineas		
	return render(request,'ver.html',context)	
