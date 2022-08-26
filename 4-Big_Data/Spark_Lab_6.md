# Spark Lab for Monitoring & Performance Tuning

## Download the data

```sh
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/cars.csv
```

## Initialize the Cluster

Stop any previously running containers with this:

```sh
for i in `docker ps | awk '{print $1}' | grep -v CONTAINER`; do docker kill $i; done
```

Remove any previoysly used containers

```sh
docker rm spark-master spark-worker-1 spark-worker-2
```

Start the Spark Master server:

```sh
docker run \
    --name spark-master \
    -h spark-master \
    -e ENABLE_INIT_DAEMON=false \
    -p 4040:4040 \
    -p 8080:8080 \
    -v `pwd`:/home/root \
    -d bde2020/spark-master:3.1.1-hadoop3.2
```

Start a Spark Worker that will connect to the Master:

```sh
docker run \
    --name spark-worker-1 \
    --link spark-master:spark-master \
    -e ENABLE_INIT_DAEMON=false \
    -p 8081:8081 \
    -v `pwd`:/home/root \
    -d bde2020/spark-worker:3.1.1-hadoop3.2
```

## Connect a PySpark Shell to the Cluster and Open the UI

Launch a PySpark shell in the running Spark Master container:

```sh
docker exec \
    -it `docker ps | grep spark-master | awk '{print $1}'` \
    /spark/bin/pyspark \
    --master spark://spark-master:7077
```

Create a DataFrame in the shell with:

```sh
df = spark.read.csv("/home/root/cars.csv", header=True, inferSchema=True) \
    .repartition(32) \
    .cache()
df.show()
```

Enter localhost:4040 for Spark App UI in your browser. Verify that you can see Jobs page with jobs.

## Run an SQL Query and Debug in UI

In this exercise, you will define a user-defined function (UDF) and run a query that results in an error. 
We will locate that error in the application UI and find the root cause.
Finally, we will correct the error and re-run the query.

### Task A : Run an SQL Query

Define a UDF to show engine type. 
Copy and paste the code and click Enter.

```py
from pyspark.sql.functions import udf
import time

@udf("string")
def engine(cylinders):
    time.sleep(0.2)  # Intentionally delay task
    eng = {6: "V6", 8: "V8"}
    return eng[cylinders]
```

Add the UDF as a column in the DataFrame

```py
df = df.withColumn("engine", engine("cylinders"))
```

Group the DataFrame by “cylinders” and aggregate other columns

```py
dfg = df.groupby("cylinders")

dfa = dfg.agg({"mpg": "avg", "engine": "first"})

dfa.show()
```

The query will have failed and you should see lots of messages and outputs in the console.

### Task B: Debug the error in the Application UI


**1. Find the error in the Application UI**

Open UI to the Jobs, look at list of Failed Jobs, click on first job.

![Ui Failed Jobs](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/Failure-Jobs-tab.png)

This will bring up the Job details with a list of stages for that job. In the list of Failed Stages, click on the first failed stage to show the stage details with a list of tasks for that stage.

![Stages](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/Failure-Jobs-detail.png)

Here we see lots
of failed tasks. Looking at the first one, the far right column shows details of the failure.

![Tasks](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/Failure-Stage-list.png)

Click to expand the details

![Log Details](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/Failure-Task-details.png)

Scroll down a little until you can see the last part of the Python error that shows the cause. 
You should be able to see this was caused by a KeyError in our UDF `engine()`.

You could also view these errors by looking at the column that has links to the logs and click on `“std err”` to show the standard error log.

Close the PySpark browser tab.

In the terminal, fix the UDF by adding an entry to the dictionary of engine types and provide a default for all other types. Copy and paste this code and click `Enter`.

```py
@udf("string")
def engine(cylinders):
    time.sleep(0.2)  # Intentionally delay task
    eng = {4: "inline-four", 6: "V6", 8: "V8"}
    return eng.get(cylinders, "other")
```

Re-run the query. You will have to add the “engine” column again and enter the query since we changed the UDF.

```py
df = df.withColumn("engine", engine("cylinders"))

dfg = df.groupby("cylinders")

dfa = dfg.agg({"mpg": "avg", "engine": "first"})

dfa.show()
```

Once the query completes without errors, you should see output similar to this.

```
+---------+------------------+-------------+                                    
|cylinders|          avg(mpg)|first(engine)|
+---------+------------------+-------------+
|        6|19.985714285714288|           V6|
|        3|             20.55|        other|
|        5|27.366666666666664|        other|
|        4|29.286764705882348|  inline-four|
|        8|14.963106796116506|           V8|
+---------+------------------+-------------+
```

## Exercise 3 : Monitor Application Performance with the UI

Now that we have run our query successfully, we will scale up our application by adding a worker to the cluster. 
This will allow the cluster to run more tasks in parallel and improve the overall performance.

### Task A : Add a Worker to the Cluster

View the Stages tab, then click on the stage with 32 tasks. 
In that stage our UDF is being applied to each partition of the DataFrame.

Looking at the timeline, you can see there is a single worker with id `0 / <ip-address>` that can run up to a certain amount of tasks in parallel at one time.
Adding another worker will allow an
additional tasks to be run in parallel.

Open a new terminal.

Add a second worker to the cluster with the command in the new terminal:

```sh
docker run \
    --name spark-worker-2 \
    --link spark-master:spark-master \
    -e ENABLE_INIT_DAEMON=false \
    -p 8082:8082 \
    -d bde2020/spark-worker:3.1.1-hadoop3.2
```

If the command is successful, there will be a single output showing the container id:

```sh
$ 1935a71827668ae3476e6a16f0bebcd4c2a342a21271dc22be487aa1b1731708
```

Click back to the first terminal that has the PySpark shell open to continue.

### Task B : Re-run the query and check performance

Re-run the query, this time we can simply call `show()` again:

```py
dfa.show()
```

Click on Launch Application and enter the port 4040 to open the PySpark browser, go to the Stages tab and see the most recent stage Id.

You will see that the additional worker with id `1 / <ip-address>` is listed and now allows more tasks to be run in parallel. The task timeline should look similar to the following.

![Double Worker Nodes](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/Perf-parallel-tasks-2.png)










