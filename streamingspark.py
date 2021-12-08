from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#Inicializar contexto
sc = SparkContext("local[2]","NetworkWordCount")
ssc = StreamingContext(sc,5)

lines = ssc.socketTextStream("localhost",9090)



mayor=[]
menor=[]
words = lines.filter(lambda line: len(line)>10 )
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

wordCounts.pprint() 

ssc.start()
ssc.awaitTermination()