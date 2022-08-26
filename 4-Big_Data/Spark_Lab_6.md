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




