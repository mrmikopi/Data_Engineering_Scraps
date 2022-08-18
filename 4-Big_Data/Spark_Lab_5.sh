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













