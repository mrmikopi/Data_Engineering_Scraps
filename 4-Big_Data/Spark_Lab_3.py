# Spark SQL Lab

# Installing required packages
# !pip install pyspark
# !pip install findspark
# !pip install pyarrow==1.0.0
# !pip install pandas
# !pip install numpy==1.19.5

import findspark
findspark.init()

import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Create context and session
sc = SparkContext()
spark = SparkSession \
    .builder \
    .appName('Python Spark SQL Basic Example') \
    .config('spark.some.config.option','some-value') \
    .getOrCreate()

# Initialize Session
spark

# Read file from the internet
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')

# Preview a few records
mtcars.head()

# Rename first column
mtcars.rename( columns={'Unnamed: 0':'name'}, inplace=True )

# Create DataFrame from Pandas DF
sdf = spark.createDataFrame(mtcars) 

# Schema of DataFrame
sdf.printSchema()

# Create a Temp View form SDF
sdf.createTempView("cars")

# Showing the whole table
spark.sql("SELECT * FROM cars").show()

# Showing a specific column
spark.sql("SELECT mpg FROM cars").show(5)

# Basic filtering query to determine cars that have a high mileage and low cylinder count
spark.sql("SELECT * FROM cars where mpg>20 AND cyl < 6").show(5)

# Aggregating data and grouping by cylinders
spark.sql("SELECT count(*), cyl from cars GROUP BY cyl").show()

# import pandas UDF function
from pyspark.sql.functions import pandas_udf, PandasUDFType

# Create UDF
@pandas_udf("float")
def convert_wt(s: pd.Series) -> pd.Series:
    # The formula for converting from imperial to metric tons
    return s * 0.45


# Register UDF
spark.udf.register("convert_weight", convert_wt)

# Call UDF inside SQL Query
spark.sql("SELECT *, "
    + "wt AS weight_imperial, " 
    + "convert_weight(wt) as weight_metric "
    + "FROM cars").show()

#
# Questions
#

# Display all Mercedez car rows from the cars table view we created earlier. 
# The Mercedez cars have the prefix "Merc" in the car name column.
spark.sql("select * from cars where upper(name) like 'MERC%'").show()

# create a pandas UDF to convert the mpg column to kmpl (kilometers per liter). 
# You can use the conversion factor of 0.425.
@pandas_udf("float")
def convert_fuelCons(s: pd.Series) -> pd.Series:
    return s * 0.425

spark.udf.register('convert_fcs', convert_fuelCons)

spark.sql('select name, mpg as Miles_Per_Gallon, convert_fcs(mpg) as KMs_Per_Liter'
          + ' from cars order by 3 desc').show()