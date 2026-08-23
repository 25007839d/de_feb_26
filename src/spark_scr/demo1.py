import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

# emptyrdd = spark.sparkContext.emptyRDD
# print(emptyrdd.collect())

df = spark.createDataFrame([])
print(df.count())