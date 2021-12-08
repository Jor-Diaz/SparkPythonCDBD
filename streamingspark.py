from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#Inicializar contexto
sc = SparkContext("local[2]","NetWorkWordCount")
ssc = StreamingContext(sc,1)

lines = ssc.socketTextStream("localhost",9090)

words = lines.flatMap(lambda line: line.split(" "))
pairs =words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x+y)
wordCounts.pprint()

ssc.start()
ssc.awaitTermination()