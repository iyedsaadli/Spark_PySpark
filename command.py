import pyspark
#Create a Spark Session
from pyspark.sql import SparkSession
#Create an Entry point
sc = SparkSession.builder.appName('PySpark_command').getOrCreate()
print(sc)
> SparkSession - in-memory
	SparkContext
	Spark UI
	Version
	v3.0.1
	Master
	local[*]
	AppName
	PySpark_command
