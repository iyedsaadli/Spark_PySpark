# APACHE SPARK

Spark is a platform for cluster computing. Spark lets us spread data and computations over clusters with multiple nodes (we can think of each node as a separate computer). Splitting up our data makes it easier to work with very large datasets because each node only works with a small amount of data.
As each node works on its own subset of the total data, it also carries out a part of the total calculations required, so that both data processing and computation are performed in parallel over the nodes in the cluster. It is a fact that parallel computation can make certain types of programming tasks much faster.

## Spark vs MapReduce

#### Shortcomings of MapReduce
The shortcomings of how MapReduce brought to the development of a new system as Apache Spark: 
  1] MapReduce forces your pipeline into Map and Reduce steps ==> this cannot be suitable every data analysis workflow. 
  2] MapReduce read from disk for each job (very critical for performance especially in iterative algos "ML"). 
  3] Native Java programming interface(possible with python but requires to go through streaming module ...)
  
#### Spark Solutions
Spark is not a replacement of the entire Hadoop stack but just a replacement of the Hadoop MapReduce. 
  1] Spark provides ~20 highly efficient distributed operations. 
  2] Spark uses in-memory caching of data ==> suitable for iterative algos like "ML". 
  3] It provides a very rich programming interface, Native Python, Scala, R.
  

# PySpark
PySpark is an interface for Apache Spark in Python.
The first step in using Spark is connecting to a cluster.

In practice, the cluster will be hosted on a remote machine that's connected to all other nodes. There will be one computer, called the *master* that manages splitting up the data and the computations. The master is connected to the rest of the computers in the cluster, which are called *worker*. The master sends the workers data and calculations to run, and they send their results back to the master.
When we're just getting started with Spark it's simpler to just run a cluster locally. 
Creating the connection is as simple as creating an instance of the `SparkContext` class. The class constructor takes a few optional arguments that allow us to specify the attributes of the cluster we're connecting to.
