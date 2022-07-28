### Excercise 1 : Spark Initializing

import findspark
findspark.init()

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a spark context class
sc = SparkContext()

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Spark Session'un varligini teyit etmek icin:
spark

### Excercise 2 : RDDs

data = range(1,30)
# print first element of iterator
print(data[0])
print(len(data))
xrangeRDD = sc.parallelize(data,4)

# Bir RDD yarattigimizi teyit eder:
xrangeRDD

### Transformations:
subRDD = xrangeRDD.map(lambda x: x-1)
filteredRDD = subRDD.filter(lambda x: x<10)

# Actions: Outputu almak icin
print(filteredRDD.collect())
filteredRDD.count()
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 10

### Caching test:
import time
test = sc.parallelize(range(1,50000),4)
test.cache()

# Ilk count'ta count() ve cache()'in costu var.
t1 = time.time()
count1 = test.count()
dt1 = time.time() - t1
print("dt1: ", dt1)
# 1.5 s

# Ikincide cache() oldugu icin cachelenmis datada count() alacak.
t2 = time.time()
count2 = test.count()
dt2 = time.time() - t2
print("dt2: ", dt2)
# 0.3 s

### SparkSQL & DataFrames

# SQL icin Spark Session acik olmali. Check
spark

# Dosya indirelim:
# curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/people.json >> people.json

# Spark'in read.json()'u ile dosyayi okuyalim:
df = spark.read.json("people.json").cache()

# DataFrame'i ve semasini yazdir:
df.show()
df.printSchema()

# DF'i temp SQL View'i olarak register et:
df.createTempView('people')

# Select ve Show islemleri DF ile:
df.select('name').show()        # kolon adi insert ettik
df.select(df['name']).show()    # kolonun kendisini insert ettik
# Aynisi SQL ile:
spark.sql('SELECT name FROM people').show()

# Filtering yapalim ikisinde de
df.filter(df['age'] > 21).show()
spark.sql('SELECT name FROM people WHERE age > 21').show()

# Aggregation islemleri yapalim, group by:
df.groupBy('age').count().show()
spark.sql('SELECT age, COUNT(age) as count FROM people GROUP BY age').show()

### ORNEKLER:

# Q1: 1-50 arasi integerlardan bir RDD yarat. 
# Sonra her sayiyi 2 ile carp.
numbers = range(1,50)
numbers_RDD = sc.parallelize(numbers,4)
even_numbers_RDD = numbers_RDD.map(lambda x: x*2)
print(even_numbers_RDD.collect)

# Q2 people2.json'u indir, df'e aktar,
# SQL ile average age'i bul
df = spark.read.json('people2.json').cache()
spark.catalog.dropTempView('people2')
df.createTempView('people2')
spark.sql('SELECT AVG(age) FROM people2')

# Q3 Stop sparkSession
spark.stop()