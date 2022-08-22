# Apache Spark on Kubernetes Lab

<center>
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/labs/5_FinalProject_Coursera/images/labs_module_1_images_IDSNlogo.png" width="300">
</center>

# Objectives

In this lab, you will:

*   Install *kind* - Kubernetes in Docker - an easy way to install and run a Kubernetes cluster inside a single docker container
*   Create a Kubernetes Pod - a set of containers running inside Kubernetes - here, containing Apache Spark which we use to submit jobs against Kubernetes
*   Submit Apache Spark jobs to Kubernetes

# Prerequisites

Note: If you are running this lab within the Skillsnetwort Lab environment, all prerequisites are already installed for you

The only pre-requisites to this lab are:

*   A working *docker* installation
*   The *git* command line tool

# Project Overview

Welcome to the lab on how to submit Apache Spark applications to a Kubernetes cluster. This exercise is straightforward thanks to the new native Kubernetes scheduler that has been added to Spark recently.

Kubernetes is a container orchestrator which allows to schedule millions of "docker" containers on huge compute clusters containing thousands of compute nodes. Originally invented and open-sourced by Google, Kubernetes became the de-facto standard for cloud-native application development and deployment inside and outside IBM. With RedHat OpenShift, IBM is the leader in hybrid cloud Kubernetes and within the top three companies contributing to Kubernetes' open source code base.

# Install KIND - Kubernetes in Docker

On the right hand side to this instructions you'll see the Theia IDE. Select the *Lab* tab. On the menu bar select *Terminal>New Terminal*.

<center>
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/terminal_ide.png" width="80%">
</center>

Please enter the following commands in the terminal:

Get the latest code:

```
git clone https://github.com/ibm-developer-skills-network/fgskh-new_horizons.git
```

{: codeblock}

Change the directory to the downloaded code:

```
cd fgskh-new_horizons
```

{: codeblock}

Change into the "Kubernetes in Docker" installation folder:

```
cd kind
```

{: codeblock}

Install the "Kubernetes in Docker" install tool (kind):

```
./install_kind.sh
```

{: codeblock}

Create a KIND Kubernetes Cluster running on top of Docker:

```
./create_kind_cluster.sh
```

{: codeblock}

Add an alias to for less typing:

```
alias k='kubectl'
```

{: codeblock}

# Deploy the Apache Spark Kubernetes Pod

Please continue entering the following commands in the terminal:

Install the Apache Spark POD:

```
k apply -f ../spark/pod_spark.yaml -n default
```

{: codeblock}

Make sure that we can interact the the Kubernetes Cluster form inside a POD:

```
k apply -f rbac.yaml -n default
```

{: codeblock}

Now it is time to check the status of the Pod. Just enter the following command:

```
k get po -n default
```

{: codeblock}

If you see the following output it means that the Pod is not
yet available and you need to wait a bit.

```
NAME   READY   STATUS              RESTARTS   AGE  
spark  0/2     ContainerCreating   0          29s
```

Just issue the command again after some time:

```
k get po -n default
```

{: codeblock}

After a while you should see an output like this:

```
NAME  READY   STATUS    RESTARTS   AGE
spark 2/2     Running   0          10m
```

In case you see the following status you need to delete the pod and start over again later
as this usually happens when the image registry is unreliable or offline.

```
NAME   READY   STATUS              RESTARTS   AGE  
spark  0/2     ImagePullBackOff    0          29s
```

Just in this case please delete the pod:

```
k delete po spark -n default
```

{: codeblock}

Then start over:

```
k apply -f ../spark/pod_spark.yaml -n default
```

{: codeblock}

Again, regularly check status:

```
k get po -n default 
```

{: codeblock}

Note that this Pod is called *spark* and contains two
containers *(2/2)* of which are both in status *Running*. Please also note that Kubernetes automatically *RESTARTS* failed pods - this hasn't happened here so far. Most probably because the *AGE* of this pod is only 10 minutes.

# Submit Apache Spark jobs to Kubernetes

Now it is time to enter the *spark* container of this Pod.
The command *exec* is told to provide interactive access (*-it*) to the container called *spark* (-c). With *--* we execute a shell (/bin/bash).

```
k exec  -n default -it spark -c spark  -- /bin/bash
```

{: codeblock}

You've now entered container *spark* in Pod *spark* inside Kubernetes. This container we will use to submit Spark applications to the Kubernetes cluster. This container is based on an image with the Apache Spark distribution and the *kubectl* command pre-installed.

If you are interested you can have a look at the [Dockerfile](https://github.com/romeokienzler/new_horizons/blob/main/spark/Dockerfile) to understand what's really inside.

You can also check out the [pod.yaml](https://github.com/romeokienzler/new_horizons/blob/main/spark/pod_spark.yaml). You'll notice that it contains two containers. One is Apache Spark, another one is providing a Kubernetes Proxy - a so called side car container - allowing to interact with the Kubernetes cluster from inside a Pod.

Inside the container you can use the *spark-submit* command which makes use of the new native Kubernetes scheduler that has been added to Spark recently.

The following command submits the *SparkPi* sample application to the cluster. SparkPi computes Pi and the more iterations you run, the more precise it gets:

```
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
```

{: codeblock}

You should see output like below, please ignore the WARNINGS. Unless you don't see ERRORS all is fine:

<center>
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/images/kube_lab_spark_submit_output.png" width="80%">
</center>

# Understanding the spark-submit command

So let's have a look what's going on here:

*   *./bin/spark-submit* is the command to submit applications to a Apache Spark cluster
*   *--master k8s://<http://127.0.0.1:8001>* is the address of the Kubernetes API server - the way *kubectl* but also the Apache Spark native Kubernetes scheduler interacts with the Kubernetes cluster
*   *--name spark-pi* provides a name for the job and the subsequent Pods created by the Apache Spark native Kubernetes scheduler are prefixed with that name
*   *--class org.apache.spark.examples.SparkPi* provides the canonical name for the Spark application to run (Java package and class name)
*   *--conf spark.executor.instances=1* tells the Apache Spark native Kubernetes scheduler how many Pods it has to create to parallelize the application. Note that on this single node development Kubernetes cluster increasing this number doesn't make any sense (besides adding overhead for parallelization)
*   *--conf spark.kubernetes.container.image=romeokienzler/spark-py:3.1.2* tells the Apache Spark native Kubernetes scheduler which container image it should use for creating the driver and executor Pods. This image can be custom build using the provided Dockerfiles in *kubernetes/dockerfiles/spark/* and *bin/docker-image-tool.sh* in the Apache Spark distribution
*   *--conf spark.kubernetes.executor.limit.cores=1* tells the Apache Spark native Kubernetes scheduler to set the CPU core limit to only use one core per executor Pod
*   *local:///opt/spark/examples/jars/spark-examples\_2.12-3.1.2.jar* indicates the *jar* file the application is contained in. Note that the *local://* prefix addresses a path within the container images provided by the *spark.kubernetes.container.image* option. Since we're using a *jar* provided by the Apache Spark distribution this is not a problem, otherwise the *spark.kubernetes.file.upload.path* option has to be set and an appropriate storage subsystem has to be configured, as described in the [documentation](https://spark.apache.org/docs/latest/running-on-kubernetes.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMBD0225ENSkillsNetwork25716109-2022-01-01#running-spark-on-kubernetes)
*   *10* tells the application to run for *10* iterations, then output the computed value of *Pi*

Please see the [documentation](https://spark.apache.org/docs/latest/running-on-kubernetes.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMBD0225ENSkillsNetwork25716109-2022-01-01#configuration) for a full list of available parameters.

# Monitor the Spark application in a parallel terminal

Once this command runs you can *open a second terminal window* within Theia and issue the following command:

> **Note:** To see at least one executor, run the below-mentioned command while the other terminal is still executing spark-submit command

```
kubectl get po -n default
```

{: codeblock}

This will show you the additional Pods being created by the Apache Spark native Kubernetes scheduler - one driver and at least one executor (with an exception if there is only one executor, it runs within the driver Pod). Here an example when using three executors (exact IDs replaced by X and Y for readability):

```
NAME              READY STATUS    RESTARTS AGE
spark             2/2   Running   0        28m
spark-pi-X-exec-1 1/1   Running   0        33s
spark-pi-X-exec-2 1/1   Running   0        33s
spark-pi-X-exec-3 1/1   Running   0        33s
spark-pi-X-driver 1/1   Running   0        44s
spark-pi-Y-driver 0/1   Completed 0        12m
```

You can see that Pod *spark-pi-Y-driver* is in status *Completed*, from a single executor run twelve minutes ago and that there are one driver and three executors actually running for job *spark-pi-X- ..*.

To check the job's elapsed time just execute (you need to replace the Pod name of course with the one on your system):

<span style="color:red">Please make sure you run the following code in the newly created terminal window which allows you to execute commands within the Spark driver running in a POD</span>.

> **Note:** Replace the ID in the Spark-pi-ID-driver with the one which is created by you. For example: if your pod is spark-pi-6f62d17a800beb3e-driver then replace ID with 6f62d17a800beb3e

```
kubectl logs -n default spark-pi-6f62d17a800beb3e-driver |grep "Job 0 finished:"
```

{: codeblock}

You should get something like:

```
Job 0 finished: reduce at SparkPi.scala:38, took 8.446024 s
```

If you are interested in knowing what value for *Pi* the application came up with just issue:

> **Note:** Replace the ID in the Spark-pi-ID-driver with the one which is created by you. For example: if your pod is spark-pi-6f62d17a800beb3e-driver then replace ID with 6f62d17a800beb3e

```
kubectl logs -n default spark-pi-6f62d17a800beb3e-driver |grep "Pi is roughly "
```

{: codeblock}

And you'll see something like:

```
Pi is roughly 3.1416551416551415
```

# Experiment yourself

Now you can play around with values for *spark.executor.instances*, *spark.kubernetes.executor.limit.cores=1* (0.1 is also a valid number) and number of iterations and see how it affects runtime and precision of the outcome.

This concludes this lab.

# Summary

In this lab you've learned how to setup an experimental Kubernetes cluster on top of Docker using KIND (Kubernetes in Docker). You've learned how to create an Apache Spark client POD within that cluster to submit jobs. Then, you've used the spark-submit command to create a job running inside this Kubernetes cluster. You are now able to scale your Apache Spark jobs on any Kubernetes cluster running in the cloud or in your data center to thousands of nodes, CPUs and GB of main memory.

## Changelog

| Date        | Version | Changed by     | Change Description       |
| ----------- | ------- | -------------- | ------------------------ |
| July 2021   | 1.0     | Romeo Kienzler | Initial version created  |
| August 2021 | 1.1     | Romeo Kienzler | Production ready version |
| April 2022  | 1.2     | Samaah Sarang  | Instructions updated     |

## Credits

Thanks a lot to Aije Egwaikhide for testing and her feedback to improve the lab.

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
