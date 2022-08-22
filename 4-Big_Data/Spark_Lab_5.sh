# Download the repo
git clone https://github.com/ibm-developer-skills-network/fgskh-new_horizons.git

# Change the directory to the downloaded code:
cd fgskh-new_horizons/kind

# Install kind (Kubernetes in Docker)
./install_kind.sh

# Create a KIND Kubernetes Cluster running on top of Docker:
./create_kind_cluster.sh

# Create alias
alias k='kubectl'

# Install the Apache Spark POD:
sudo k apply -f ../spark/pod_spark.yaml -n default

# Make sure that we can interact the the Kubernetes Cluster form inside a POD:
k apply -f rbac.yaml -n default

# Now it is time to check the status of the Pod. Just enter the following command:
k get po -n default

# If you see the following output it means that the Pod is not
# yet available and you need to wait a bit.

# NAME   READY   STATUS              RESTARTS   AGE  
# spark  0/2     ContainerCreating   0          29s

# Just issue the command again after some time:
k get po -n default

# In case you see 0/2 READY all the time, you need to delete the pod and start over again later
# as this usually happens when the image registry is unreliable or offline.

#Just in this case please delete the pod:
k delete po spark -n default

# Then start over:
k apply -f ../spark/pod_spark.yaml -n default

# Again, regularly check status:
k get po -n default 

# Note that this Pod is called spark and contains two
# containers (2/2) of which are both in status Running. 
# Please also note that Kubernetes automatically RESTARTS failed pods
# this hasn’t happened here so far. 
# Most probably because the AGE of this pod is only 10 minutes.

# Now it is time to enter the spark container of this Pod.
# The command exec is told to provide interactive access (-it) 
# to the container called spark (-c). With – we execute a shell (/bin/bash).
k exec  -n default -it spark -c spark  -- /bin/bash

# You’ve now entered container spark in Pod spark inside Kubernetes. 
# This container we will use to submit Spark applications to the Kubernetes cluster. 
# This container is based on an image with 
# the Apache Spark distribution and the kubectl command pre-installed.
# If you are interested you can have a look at the Dockerfile 
# to understand what’s really inside.

# You can also check out the pod.yaml. You'll notice that it contains two containers.
# One is Apache Spark, another one is providing a Kubernetes Proxy 
# - a so called side car container - allowing to 
# interact with the Kubernetes cluster from inside a Pod.

# Container icinde, spark-submit'i calisiricaz.
# Spark'a eklenen Kube Scheduler'i kullanabilecegimiz spark-submit komutu asagidaki gibi.
# Argumanlarin aciklamalari Big_Data_Notes.md'da
./bin/spark-submit \
--master k8s://http://127.0.0.1:8001 \
--deploy-mode cluster \
--name spark-pi \
--class org.apache.spark.examples.SparkPi \
--conf spark.executor.instances=3 \
--conf spark.kubernetes.container.image=romeokienzler/spark-py:3.1.2 \
--conf spark.kubernetes.executor.limit.cores=1 \
local:///opt/spark/examples/jars/spark-examples_2.12-3.1.2.jar \
10

# Monitor running pods (in a different terminal)
kubectl get po -n default

# To check the job's elapsed time just execute 
# (you need to replace the Pod name of course with the one on your system):
kubectl logs -n default spark-pi-6f62d17a800beb3e-driver |grep "Job 0 finished:"

# If you are interested in knowing what value for Pi the application came up with just issue:
kubectl logs -n default spark-pi-6f62d17a800beb3e-driver |grep "Pi is roughly "















