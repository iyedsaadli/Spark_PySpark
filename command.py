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
#returns the names of all the tables in the cluster as a list.
sc.catalog.listTables()

# RUN SQL QUERY

query = "FROM Table SELECT * LIMIT 10"

# Get the first 10 rows of the table
first10 = spark.sql(query)

# Show the results
first10.show()
