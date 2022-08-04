# Install these packages
# !pip install pyspark
# !pip install findspark
# !pip install pandas

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Create a Spark Context class
sc = SparkContext()

# Create a Spark Session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames Basic Example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Initialize Spark Session
spark

# Read the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# Preview
mtcars.head()

# Use the `createDataFrame` function to load the data into a spark dataframe
sdf = spark.createDataFrame(mtcars)

# Schema of loaded Spark DataFrame
sdf.printSchema()

# Pandas'daki .head() yerine .show()
sdf.show(5)

# Sadece belli kolonlari goster
sdf.select('mpg','carb').show(5)

# Filter results
sdf.filter(sdf['mpg'] < 18).show(5)

# Add a column with columnar operation
sdf.withColumn('wtTon', sdf['wt'] * 0.45).show(5)

# Aggregation
sdf.groupby(['cyl'])\
.agg({'wt': 'AVG'})\
.show(5)


# With sort
car_counts = sdf.groupby(['cyl'])\
.agg({'wt': 'count'})\
.sort('count(wt)', ascending=False)\
.show(5)

# Questions

# Display the first 5 rows of all cars that have atleast 5 cylinders.
sdf.filter(sdf['cyl']>4).show(5)

# Using the functions and tables shown above
# print out the mean weight of a car in our database in metric tons.
sdf.withColumn('wtTon', sdf['wt'] * 0.45).agg({'wtTon':'mean'}).show(5)

# create a new column for mileage in kmpl (kilometer-per-liter) 
# instead of mpg(miles-per-gallon) by using a conversion factor of 0.425.
# Additionally sort the output in decreasing order of mileage in kmpl.
from pyspark.sql.functions import round
sdf.withColumn('kmpl', round((sdf['mpg'] * 0.425), 4))\
.sort('kmpl', ascending=False).show()
