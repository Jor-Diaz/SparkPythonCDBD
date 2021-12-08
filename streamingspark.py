from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#Inicializar contexto
sc = SparkContext("local[2]","NetWorkWordCount")
ssc = StreamingContext(sc,1)

lines = ssc.socketTextStream("localhost",9090)

