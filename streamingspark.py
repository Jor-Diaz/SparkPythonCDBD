from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from apriori import apriori


#Inicializar contexto
sc = SparkContext("local[2]","NetworkWordCount")
ssc = StreamingContext(sc,20)

lines = ssc.socketTextStream("localhost",9090)



mayor=[]
menor=[]
aux_particiones=[]
#for i in range(1,19,2):
#aux_particiones.append(lines.filter(lambda line: len(line)<i and len(line)>i-1))	 

#for i in aux_particiones:
resultado=lines.reduce=apriori(i)
#pairs = words.map(lambda word: (word, 1))
#wordCounts = pairs.reduceByKey(lambda x, y: x + y) 

resultado.pprint() 

ssc.start()
ssc.awaitTermination()