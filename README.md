# APACHE SPARK

Spark is a platform for cluster computing. Spark lets you spread data and computations over clusters with multiple nodes (think of each node as a separate computer). Splitting up your data makes it easier to work with very large datasets because each node only works with a small amount of data.

As each node works on its own subset of the total data, it also carries out a part of the total calculations required, so that both data processing and computation are performed in parallel over the nodes in the cluster. It is a fact that parallel computation can make certain types of programming tasks much faster.

## Spark vs MapReduce

#### Shortcomings of MapReduce
The shortcomings of how the mapreduce brought to the development of a new system as Apache Spark:
  1] MapReduce force your pipeline into Map and Reduce steps ==> this cannot be suitable every data analysis workflow.
  2] MapReduce read from disk for each job (very critical for performance espacially in iterative algos "ML").
  3] Native Java programming interface(possible with python but requires to go through streaming module ...)
  
#### Spark Solutions
Spark is not a replacement of the entire hadoop stack but just a replacement of the hadoop MapReduce.
  1] Spark provides ~20 highly efficient distributed operations.
  2] Spark uses in-memory caching of data ==> suitable for iterative algos like "ML".
  3] It provides a very rich programming interface , Native Python, Scala, R.
  

# PySpark
PySpark is an interface for Apache Spark in Python.
