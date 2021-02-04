from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("myApp") \
.config("spark.mongodb.input.uri", "mongodb://host.docker.internal:27017/sample1.zips") \
.config("spark.mongodb.output.uri", "mongodb://host.docker.internal:27017/sample1.zips") \
.config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.3.2') \
.getOrCreate()

df = spark.read.format("mongo").load()
df.printSchema()

#./spark-submit --master spark://1a54c6392a6f:7077 ../mycode/spark_batch1.py