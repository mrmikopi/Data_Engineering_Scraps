# Spark Docker Example

#
## Setup
#

# Install pyspark
# $ pip install pyspark

# Get related repository
# $ git clone https://github.com/big-data-europe/docker-spark.git

# Enter directory
# $ cd docker-spark

# Start Docker Daemon
# $ sudo dockerd

# Start Cluster
# $ docker-compose up

#
## Code
#

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, StringType

print('debug1')
sc = SparkContext.getOrCreate(SparkConf().setMaster('spark://localhost:7077'))
print('debug2')
sc.setLogLevel("INFO")

spark = SparkSession.builder.getOrCreate()
print('debug3')

df = spark.createDataFrame(
    [
        (1, "foo"),
        (2, "bar"),
    ],
    StructType(
        [
            StructField("id", IntegerType(), False),
            StructField("txt", StringType(), False),
        ]
    ),
)
print(df.dtypes)
df.show()