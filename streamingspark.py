from pyspark import SparkContext
from pyspark.streaming import StreamingContext

import sys
from itertools import chain, combinations
from functools import reduce
from time import time
from datetime import datetime
import json

def operador_clausura(P, T, I):
  Pp = [t for t in T if P.issubset(t)] #P'
  if not bool(Pp):
    return set(I)
  return set(reduce(set.intersection, Pp))

def genClosedCandidates(L, k, T, I,NCLOSURES):
  Lk = L.get(k-1, {})
  for P in Lk:
    for i in I:
      Pc = operador_clausura(P.union(set([i])), T, I)
      NCLOSURES+=1
      if len(Pc) not in L:
        L[len(Pc)] = set([])
      L[len(Pc)].add(frozenset(Pc))
  if k in L:
    return {i:0 for i in L[k]},NCLOSURES
  else:
    return {},NCLOSURES


def a_priori_closed(T, I, sigma,NCLOSURES):
  tid = {i:set() for i in I}
  for ti, t in enumerate(T):
    for i in t:
      tid[i].add(ti)

  L = {0:set([frozenset([])])} # Agregamos el conjunto vacío que siempre es frecuente

  for i, it in tid.items():
    if len(it) >= sigma:
      P = set([i])
      Pc = operador_clausura(P, T, I)
      NCLOSURES+=1
      if len(Pc) not in L:
        L[len(Pc)] = set([])
      L[len(Pc)].add(frozenset(Pc))
  
  C = {}
  i = 1
  while i < len(I):
    
    C[i+1],NCLOSURES = genClosedCandidates(L, i+1, T, I,NCLOSURES)
    for t in T:
      for candidate in C[i+1]:
        if candidate.issubset(t):
          C[i+1][candidate] += 1    
    i += 1
    #memoria=memory_usage_psutil()
  return sorted(list(chain(*L.values())), key=len),NCLOSURES,

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    import os
    process = psutil.Process(os.getpid())
    #print(process.memory_info())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem


def apriori(aux_particiones):
	from time import time
	start_time = time()     
	print("#####################")
	print(aux_particiones,"first")
	print(type(aux_particiones),"first")
	print("-------------------------")
	ctx=[]
	for i in aux_particiones:
		linea=i.split("-")
		conjunto_aux=set()
		for i in linea:
			if i != "":
				conjunto_aux.add(int(i))
		ctx.append(conjunto_aux)
	print(ctx)	
	print("#####################")	
	print("INIT")
	NCLOSURES = 0
	
	path = "apriori"
	
	M = set(reduce(set.union, ctx))

	FC_sigma,NCLOSURES = a_priori_closed(ctx, M, 0,NCLOSURES)
	time=time()-start_time
	print("END")		
	results = {
	  'n_results' : len(FC_sigma),
	  'n_closures' : NCLOSURES,
	  'exec_time' : time,
	  'data':FC_sigma
	}

	d = datetime.now()
	timestamp = '{}{}{}-{}-{}-{}'.format(d.year, d.month, d.day, d.hour, d.minute, d.second)
	fname="test"	
	with open('results/{}-{}-{}.json'.format("apriori",fname, timestamp) , 'w') as fout:
	  json.dump(results, fout)	 
	return 

def aux_ctx(line):
	aux1=line.collect()
	print(aux1)
	print(type(aux1))
	if len(aux1)>0:
		apriori(aux1)	
		return line
	return line

#Inicializar contexto
sc = SparkContext("local[2]","NetworkWordCount")
ssc = StreamingContext(sc,10)

lines = ssc.socketTextStream("localhost",9090)



aux=lines.foreachRDD(aux_ctx)
print("jajajajaaaaaaaaaaaaaaaaaaaaa")
print(aux)
print("////////////////////////")

#lines=lines.filter(lambda line: len(line)>1)
#	aux_particiones.append(aux)

#for i in aux_particiones:
#words = lines.flatMap(lambda line: line.split("-"))
#resultado=lines.reduce(apriori(aux))
#pairs = words.map(lambda word: (word, 1))
#wordCounts = pairs.reduceByKey(lambda x, y: x + y) 

#aux.pprint() 

ssc.start()
ssc.awaitTermination()