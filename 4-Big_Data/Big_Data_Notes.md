# Big Data with Spark & Hadoop

Notes from videos/labs. Mostly in Turkish.

## Content

1. [Week 1 - Introduction](#week-1---introduction)
2. [Week 2 - Hadoop](#week-2---hadoop)
3. [Week 3 - Spark](#week-3---spark)
4. [Week 4 - DataFrames & SparkSQL](#week-4---dataframes--sparksql)
5. [Week 5 - Spark Architecture](#week-5---spark-architecture)

## Week 1 - Introduction

1. [What is Big Data](#big-data-nedir)
2. [5V of Big Data](#5-v-of-big-data)
3. [Impact of Big Data](#impact-of-big-data)
4. [Parallel Processiong & Scalability](#parallel-processing--scalability)
5. [Tools and Ecosystem](#tools-and-ecosystem)
6. [Open Source and Big Data](#beyond-the-hype)
7. [Beyond the Hype](#beyond-the-hype)

### Big Data Nedir

* Veri buyuklugu normal verilere gore buyuk. 
* Structured, semi-structured veya unstuctured olabilir.
* Inceleyebilmek icin process edilmesi gerekli.
* Farkli kaynaklardan surekli olarak akis halinde gelir.
* Videolar, ses, resim gibi turlerde de olabilir.
* Daginik sistemlerde islenirler.

Su akisa gore ilerlenir:

1. Data Collection (Hadoop Hdfs)
2. Data Modelling (Hadoop Yarn / MapReduce)
3. Data Processing (Spark, Hive)
4. Data Visualization

### 5 V of Big Data

* Velocity: Hizli islenme, durmadan islenme. Batch, gercek zamana yakin ve streaming olarak islenebilir.
* Volume: Datanin miktari. Surekli artiyor.
* Variety: Veri makinalardan, insanlardan ve islemlerden gelebilir. Structured, semi str. veya unstr. olabilir.
* Veracity: Veri kalitesi, kaynagi ve tutarliligiyla ilgilidir. Insanlardan ve islemlerden gelen veriyle ilgilidir.
* Value: Hepsinden alinabilecek value.

### Impact of Big Data

Alisveris sitelerinde, kisisel asistanlarda sikca kullanilir. Amazon, Siri, Google Now gibi gibi.

IoT cok data uretiyor bu konuda.

### Parallel Processing & Scalability

Parallel processing:
Veri buyuk oldugu icin klasik bilgisayar metodu kullanilamiyor. Veriyi diskten al, memory'e, isle, geri yukle yapamiyorsun boyuttan oturu.

Veriyle yapilacak tum islemleri farkli konumlarda cozmeye calisiyorsun, boylece hata durumunda ayni node icinde o islem tekrar yapiliyor. 

Data Scaling nedir?

Verinin boyutuna gore memory'i veya bilgisayari buyuttugunu dusun. OKey ama Big Data icin no no.

Onun yerine Horizontal Scale yapiyosun, embarrasingly parallel yapacaksin. Bisuru node veya cluster olacak veriyi paylastirabilecek.

Bunda da soyle durumlar oluyor: Veriyi siralayacaksin mesela buyukten kucuge. Node'lar birbiriyle iletisime gece gece tek makina gibi hareket etmek zorunda kalacak.

O yuzden, boyle toplu islemleri yapmak icin bi node'un olacak. Verinin ilgili kisimlarini burada tutacaksin tek parca. Verinin kopyalarini da node'lara dagitacaksin.

### Tools and Ecosystem

- [Data Tech](#data-tech)
- [Analytics and Visualization](#analytics-and-visualization)
- [Business Intelligence](#business-intelligence)
- [Cloud Providers](#cloud)
- [NoSql Dbs](#nosql-databases)
- [Programming Tools](#programming-tools)

#### Data Tech

- Hadoop
- HDFS
- Spark
- MapReduce
- Cloudera
- DataBricks

#### Analytics and Visualization

- Tableau
- Palantir
- SAS
- Pentaho
- Teradata

#### Business Intelligence

Raw Data'yi kullanilabilir hale getirir, analize uygun hale getirir. Istatistik gibi alanlari kullanabilir.

- Cognos
- Oracle
- Power BI
- Business Objects
- Hyperion

#### Cloud

- AWS
- IBM
- Google Cloud
- Oracle

#### NoSQL Databases

- MongoDB
- CouchDB
- Cassandra
- Redis

#### Programming Tools

- R
- Python
- SQL
- Scala
- Julia

### Open Source and Big Data

Projelerin gelistirilmesi ve surdurulmesi icin kacinilmaz. 

Commiter: Kodu dogrudan degistirebilenler.
Contributer: Degisiklikleri review icin gonderen destekciler.
User: Kullanicilar.

Hadoop kritik bi Big Data teknolojisi. Hadoop'taki su projeler mesela onemli open source:

- MapReduce, Spark'in muadili
- Hadoop File System, Dataset manager gibi
- Yet Another Resource Negatioator (YARN), Resource Manager. Kubernetes gibi muadilleri var.

Hive ve Spark, ETL islerini filan destekliyor hep.

### Beyond the Hype

Big Data Kaynaklari:

- Social Data
- Machine Data (IoT vs.)
- Transactional Data

**Structured Data:**

Organized, labeled ve tablo seklinde formati var.

Sql direkt bir ornek.

**Unstructured data:**

Image'lar, sensor datasi, text data vs. vs.

Sosyal medya icerikleri filan buralardaymis. Videolar vs.

**Semi Structured**

E postalar mesela. Hem structured alanlar var hem de karisik alanlar.

Xml veya Json dosyalari da buraya giriyor

Cloud computing'in ilerlemesi de big datayi hizlandirmis.

### Use Cases

Finans, teknoloji ve telekomunikasyon'da cok kullanim var. Retail, government ve healthcare devam ediyor.

**Retail'de** mesela:

- Price Analytics
- Sentiment Analystics: Urunler hakkindaki yorumlardan cikarim yapar

 **Insurance:**

- Fraud Analytics
- Risk Assessment: user history'e gore modelleme yapilabilir.

**Telecommunications:**

- Network Security
- Location Bases Promotions
- Real time network analytics
- Pricing promotions

**Manufacturing:**

- Predictive Maintenance
- Production Optimization

**Automative:**

- Predictive Support: bunun arabasi bozulacak arayalim bi
- Connected self-driven cars

**Finance:**

- CUstomer Segmentation
- Algoritmic Trading

## Week 2 - Hadoop

1. [Introduction](#hadoop-introduction)
2. [MapReduce](#mapreduce)
3. [Hadoop Ecosystem](#hadoop-ecosystem)
4. [HDFS](#hdfs)
5. [HIVE](#hive)
6. [HBase](#hbase)
7. [Hadoop and MapReduce Lab Example](#hadoop--mapreduce-lab-example)
8. [Hadoop Cluster Lab Example](#hadoop-cluster-example-lab)

### Hadoop Introduction

Big data teknolojisi.
Buyuk miktarda data, farkli farkli kaynaklardan gelen data ve structured & unstr. data icin ideal. Cluster'larda paralel calisabilir.

Bir DB Degil, data isleme ortami gibi.

* HDFS : Storage module. 
* MapReduce: Processing unit.
* YARN: Resource manager.

Kotu yanlari:

- Transaction processing
- Parallel degil de lineer isler
- Datada dependency varsa
- Low latency data access
- Cok sayida kucuk dosya varsa (MapReduce'un bazi ozellikleri bunun icin gelistirildi)
- Little data uzerinde Intensive calculations (Hive daha iyi)

### MapReduce

Big Data isleyicisi. Hadoop'un kalbi. Distrubuted computing saglar. Map ve Reduce tasklarindan olusur (tabi ki).

Map: Input file alir (hdfs'ten mesela), bilgileri key-value listesi olarak map halinde saklar. Bikac islem daha yapar.

Reducer'a iletilir. Reduce de paralel sekilde derliyor topluyor isliyor.

**Isleyisi:**

'isimler' datasinda kac tane ozgun isim oldugunu bulan akis:

![MapReduce_Diagram](resource/MapReduce_Diagram_1.png)

**Neden MapReduce Kullanalim?**

- Parallel Computing saglar node'lar arasinda. Name ve Data Node'lari olur Hadoop'ta
- Splitting and running tasks in parallel

**Use Case'ler**

- Sosyal medya uygulamalari
- Recommendations data
- Financial Industries
- Advertisements (cok severiz malum)

### Hadoop Ecosystem

Hadoop Common - Common utilities and other modules. Orn:

- HDFS
- MapReduce
- YARN

![Hadoop Ecosystem](resource/Hadoop_Ecosystem_1.png)

**Ingesting:**

- Flume: Big Data toplar ve iletir. Basit ve esnek bir mimarisi vardir
- Sqoop: Relational Db datasi toplar ve hadoop'a iletir. Ayrica ilgili MapReduce kodlarini da olusturup uretiyormus. Hdfs islerini de hallediyor sanirim(?). Db accessi oldugu icin schema'lari anliyor.

**Store data:**

- HBase: Column based sekilde non-relational databasedir. Hdfs uzerinde calisir. Datayi hashmapler, yani indexler, halinde saklayip random access-faster access saglar.
- Cassandra: Bir NoSQL db'dir.

**Analyzing data:**

- Pig: Large data analyzer. Prosedurel data flow language'i var.
- Hive: Report creating. Server side calisir. Kullanici erismek istedigi datayi secer: declerative'dir.

**Access data:**

- Impala: Non-tech userlarin kullanimini saglar.
- Hue: Hadoop User Experience'in kisaltmasi. Data upload, browse ve query islemleri saglar. Pig islerini ve akislarini calistirabilir. Hive ve MySql icin SQL query destegi saglar.

### HDFS

Buyuk datayi bloklar halinde replike ederek saklar. Fault tolerant da oluyormus boylece. Scale etmesi de kolay ve ucuz.

Streaming data access'i sunuyormus.

Ayrica bir CLI sunuyormus interaksiyon icin.

**Blocklar** calisiyor. 64 mb veya 128 mb chunklar halinde tutuyor blocklari. Daha az kalirsa bi bloga, daha az olabilir tabi.

Block is a minumum size of a file (dolmayabilir)

**Nodes**

Calisan her bi makina gibi dusunelim. Primary ve Secondary Node'lar var.

- **Primary Node:** aka. Name Node. File access'i duzenler. Secondary node'un tasklarini yonetir. Her CLUSTER'da 1 tane.

- **Secondary Node:** aka. Data Node. Read Write requestlerini gerceklestirir. Cokca olabilir.

Primary node, is ustlendigi zaman kendisine en yakin rack'leri onceliklendirir. Maximizing efficiency.

**Racks**

Rack: 40 veya 50 adet, ayni networku kullanan node toplulugu

Rack awareness calisiyor Hadoop. Onceliklendirme yaptigi gibi, ayrica replikasyon yapilan rack'leri de farkli tutuyor ki fault proof devam.

**Boyuta gore siralama:**

Blocks -> Nodes -> Racks -> Cluster

**Replication demisken:**

Backup amaclidir. Replication factor: Bir block'un kac kere replike edilecegi.

#### Write once, read many times

HDFS'in dosya konsepti. Editing updatingden ziyade append usulu.

**Read** icin: Client datanin oldugu node'u bulmak icin istek atar. Read requestini ilgili node'a atar(?). Close connection.

**Write** icin: Yazdirilmak istenen file var mi diye bakilir. Varsa IO Exception. Yoksa yetkilendirilir. Yazma islemi, replikalarin yazilmasiyla sonlanir.

### HIVE

Structured/Tabular data icin **warehouse software**. Read/write/manage islerini yapabiliyor. SQL gibi HiveQL'i var. Cleansing ve filtering destekliyor

**RDBMS'le kiyaslanisi:**

![Hive vs RDBMS](resource/Hive_Architecture_1.png)

**Mimarisi:**

![Hive Architecture](resource/Hive_Architecture_2.png)

- JDBC/ODBC Client: Java applerini / ODBC applerini Hive'a baglayan clientlar.

- Hive Services:
    - Hive Server: Enabling Queries
    - Driver: Recieves query statements
    - Optimizer: Tasklari boler
    - Executor: Optimizer'dan aldigi tasklari calistirir
    - Metastore: Metadata storage

### HBase

Column base non-relational **bir database.** HDFS uzerinde calisir. Real time data ve random read/write access of Big Data islerinde iyiymis.

**Features:**

- Linearly & modularly scalable
- MapReduce isleri icin bir backup support
- Consistent reads and writes
- No fixed column schema
- Kullanici erisimi icin kolay bir Java API'i
- *Cluster'lar arasi* data replikasyonu da saglar

Column diyoruz da bildigin column iste. Ama kolonlari tek tek degil, bazilarini column family olarak grupluyor. Family'lere sonradan kolon eklenebiliyor. 

HBase'in de primary node / region server olarak iki nodu cesidi var.

**HBase ve HDFS Kiyaslamasi**

HBase dinamik degisikliklere izin veriyor, burasi onemli. Sadece write/read degil.

![HBase vs HDFS](resource/HBase_Comparison_1.png)

#### HBase Mimarisi:

![HBase Architecture](resource/HBase_Architecture_1.png)

- HMaster: Master Server.
    - Region serverlari monitor eder
    - Region serverlara region atar
    - Schemalara yapilan degisiklikleri yonetir
- Region Servers:
    - Read Write requestleri alir.
    - Regionlari yonetirler
    - Client ile direkt kontakt kurabilir.
- Region:
    - En kucuk HBase cluster birimi
    - Contains multiple stores. Her column family icin bir store.
    - HFile ve MemStore diye iki componenti varmis :(
- Zookeeper:
    - Node'lar arasi baglari maintain eder (hdfs diye nodelar var)
    - Daginiklikta senkronizasyon saglar
    - Server failure'lari tespit eder, islemleri yapar.

### Hadoop & MapReduce Lab Example

*Bu ve sonraki lablarda, 
hadoop ortamini windows'ta kurmakta sorunlar yasadim.
labaratuvar uzerinden ilerledim sadece*

Indirilen dosyalari, onceden olusturulmus bir 'wordCounter' mapReduce ile calistirdik.
Sonuc olarak bize bi *_SUCCESS* dosyasi, bi de *part-r-00000* dosyasi olustu.
Part-r olanda word count vardi.

Su komut ile programi calistirdik:

```sh
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.3.jar wordcount data.txt output
```

Ornegin calisma akisi su sekilde:

![Map Reduce Akisi](resource/map_reduce_picture_rep.png)

### Hadoop Cluster Example Lab

Dockerize hadoop kullanip hadoop Cluster yaratacagiz.

Indirilen git reposunda su komutla docker calistirildi:

```sh
docker-compose up -d
```

Docker-compose, bi YAML dosyasi icindeki servisleri olusturup calistirir.
Calistirinca soyle oldu:

```
 ⠿ Network ooxwv-docker_hadoop_default                Created   0.2s
 ⠿ Volume "ooxwv-docker_hadoop_hadoop_namenode"       Created   0.0s
 ⠿ Volume "ooxwv-docker_hadoop_hadoop_datanode"       Created   0.0s
 ⠿ Volume "ooxwv-docker_hadoop_hadoop_historyserver"  Created   0.0s
 ⠿ Container namenode                                 Started   5.3s
 ⠿ Container resourcemanager                          Started   3.0s
 ⠿ Container nodemanager                              Started   4.4s
 ⠿ Container datanode                                 Started   5.3s
 ⠿ Container historyserver                            Started   3.5s
 ```

Sonra asagidaki komutla nameNode'u calistirmisiz:

```
docker exec -it namenode /bin/bash
```

Hadoop'u kullanmak icin config dosyalari editleniyor. Bu dosyalardan bazisi:

- hadoop-env.sh: Masterfile. Yarn, hdfs, mapreduce ve hadoop ayarlarini ayarlar.
- core-site.xml: Hdfs ve Hadoop core ozelliklerini ayarlar.
- hdfs-site.xml: Node metadatasinin lokasyonunu, fsimage dosyasini ve log dosyasini kontrol eder.
- mapred-site.xml: MapReduce config parametreleri
- yarn-site.xml: Yarn ayarlari. Node manager, resource manager, containerlar ve Application master ayarlari vardir.

Hdfs icinde bir **directory yarattik**:

    hdfs dfs -mkdir -p /user/root/input

Hadoop config xml dosyalarini input klasorune kopyaladik:

    hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml /user/root/input

data.txt dosyasi cektik internetten. Onu da */user/root* a kopyaladik:

    hdfs dfs -put data.txt /user/root/

*cat* ile dosya icerigine baktik, kopyaladigimizi teyit ettik:

    hdfs dfs -cat /user/root/data.txt

Bu noktada, calisan hadoop uygulamasina girecektik.
Ama kurstaki uygulama icinden calistiramadim aplikasyonu.
Gorsellere bakarak devam ediyorum.

Utilities -> Browse file system ile ilerlendiginde,
az once yarattigimiz dosyalari gorebiliyoruz.
data.txt dosyasini ve block sizelerini da goruyoruz:

![Hdfs directory browse](resource/browse_directory.png)

Dosyaya tikladigimizda, block id'sini filan da gorebiliyoruz.

**Notlar:**

- Name Node, sakladigi dosyalarin metadatasini memory'de tutar. 
Quick access icin.
- Hadoop cluster'imizda sunlar olacak:
    - Name node
    - Data node
    - Node manager
    - Resource manager
    - Hadoop History Server

## Week 3 - Spark

1. [Introduction](#introduction-to-spark)
2. [Functional Programming Basics](#functional-programming-basics)
3. [Parallel Programming Using RDD](#parallel-programming-using-rdd)
4. [Parallelism in Spark and Scaling Out](#sparkta-parallelism-ve-scaling-out)
5. [SparkSQL and DataFrames](#sparksql-ve-dataframes)
6. [Spark Lab Example](#spark-labaratuvar)
7. [Spark Highlights](#week-3-spark-highlights)

### Introduction to Spark

Onemli ozellikler:

- Open source
- In-memory
- Distributed data processing
- Iterative analysis on Massive data
- Genelde Scala'da yazilir. Scala JVM'de calisir.

**Distributed != Parallel**

- Parallel: Farkli processorler, ayni memory
- Distributed: Processorlerin kendi memoryleri olabilir, daginik memoryler olabilir.

**Distributed'in faydalari:**

- Scalability ve modular growth
- Fault tolerance and redundancy

**MapReduce'a kiyaslanisi:**

MapReduce isinde diske veya HDFS'e yapilan read'ler write'lar olurdu.

Spark bunu gerekli datayi in-memory yaparak cozuyor.
Disk IO'lari expensive ve time consuming imis.

Data Engineering icin kullanilan Spark urunleri:

- Core Spark Engine
- Clusters and executors
- Cluster Management
- SparkSQL
- Catalyst Tungsten DataFrames

### Functional Programming Basics

- Matematiksel fonksyonlari temel alir
- Declarative model izler
- 'Nasil' odakli degil de 'ne' odaklidir. Input ve output odaklidir.
- Statementlar yerine expressionlar kullanir

Ayrica tasklarimizi node node ayirip parallelization da yapabiliriz(?).
Spark, inheritly parallel.

### Parallel Programming using RDD

**RDD:** Resillient Distributed Datasets.

- Spark'in temel data abstraction metodu.
- Fault tolerant collection of elements.
- Cluster icindeki node'lara partition'lanir.
- Parallel operasyonlari calistirabilir.
- **Immutable'dir**. Olustuktan sonra degistirilemez. Degistirilmesi teklif dahi edilemez.

Spark'ta bir 'driver program' calisir. 
Kullanicinin temel islemlerini gerceklestirir.
Parallel operasyonlari da cluster'lara uygular.

RDD supports file types:

- Text
- SequenceFiles
- Avro
- Parquer
- Hadoop input formats

RDD Supports file formats:

- Local
- Cassandra
- HBase
- HDFS
- Amazon S3
- SQL and NoSql

**RDD Olusturma**

External veya local file'i, Hadoop-Supported systemlerden alip olusturabiliriz.

HDFS, Hbase, S3 veya Cassandra RDD yaratimi icin yardimci olabilir.

**VEYA**

Kodumuzdaki collection'lardan da basitce olusturabiliriz.

```scala
val data = Array(1,2,3,4,5)
val distData = sc.parallelize(data)
```

Aha da RDD olusturduk driver-programdeki listeden. Python veya java'dan da yapabilirdik.

Dosyayi RDD'lestirmek konusunda, partitioning giriyor isin icine.
Kac partition olacak? Spark her partition icin 1 task calistirir.

Her CPU'ya 4 5 partition genelde okey.
Spark cluster'a gore otomatik sayida partition olusturur.
Biz manuel de verebiliriz.

**VEYA**

Mevcut bir RDD'yi modifiye edip de yeni bir RDD olusturabiliriz (cunku immutable)

#### Parallel Programming:

Cok sayida islem gucunun es zamanli kullanilip, computational problem cozmesi. Distributed gibi.

Runs simultaneous instructions on multiple processors.

Memory shared olarak kullanilir, distributed'den farkli olarak.

Control/coordination mekanizmasi kurar.

**RDD ile iliskisi**

RDD olustururken partitioning ile bolmustuk datayi.
Her partition worker'larda memory'de tutulur. 
Spark, cluster'daki *her partition icin bir task calistirir*.

**Nasil Resillience sagliyor?**

- Immutable oluslari **always recoverable** yapiyor datayi.
- **Persist & Cache** islemleri ile memory'de iterative isleri hizlandirir ve fault-tolerance saglar. (?)

### Spark'ta parallelism ve Scaling out

Spark'in 3 temel componenti:

- Data Storage: HDFS veya baska formatlar.
- Compute Interface: API'lar: Scala/Java/Python
- Management: Distributed isleri yonetir. Clusterlari filan. Mesos, YARN, Kubernetes vs.

**Spark Core:**

Base engine'dir. Ozellikleri:

- Fault tolerant
- Large scale parallel ve distributed data processing
- Manages memory
- Schedules tasks
- Houses API's that defines RDD's
- Contains distributed collection of elements that are oarakkekized across the cluster

**Spark'in nasil scale oldugu** de soyle aciklanmis:

- Driver Node
- Executor Node

Bu iki node arasinda patron/calisan iliskisi var.

Driver node tasklari yonetip distributed olarak pay eder.
Executor'de de *Worker Node*lar bu pay edilmis isleri ustlenip sonuclari geri Driver'a iletirler. Resimli olarak:

![Spark Driver and Executor Node](resource/Spark_Driver_Executor.png)

Bu Worker Node'lari artir dur istedigin kadar. Spark is gucu olarak onlara dagitsin isleri. Bu sayede big dataya scale ediliyor.

### SparkSQL ve DataFrames


#### SparkSQL

- **Structured** data processing modulu.
- Query icin SQL veya baska DataFrame API'lari kullanabilir.
- Java, Scala, Python ve R'da kullanilabilir.
- Kullanilan programlama dilinden veya API'lardan *bagimsiz* olarak SQL querylerini import edilen data uzerinde veya RDD uzerinde calistirir.

```py
results = spark.sql(
    "SELECT * FROM people")
# people'i onceki satirlarda register etmen gerekiyormus
names = results.map(lambda p: p.name)
```

**SparkSQL Faydalari**

- Cost-based optimizer'i, columnar storage'i, code generation'u var.
Bunlar fast query times demek.
- Spark Engine ile buyuk sayilara scale ettigi icin fault-tolerance.
- DataFrame abstractionunu sunar. Ayrica distributed SQL query engine olarak da calisir.

#### DataFrames

Python DataFrame'ine benziyor ama zengin optimizasyonlusu. Aslinda RDBMS Tablolarina benziyor.

RDD API'si uzerine kurulmustur. RDD'leri relational query atabilmek icin kullanir.

Python uzerinde json -> DataFrame olusturulmasi:

```py
df = spark.red.json('people.json')
df.show()
df.printSchema()

# Register the dataframe as temp SQL view.
df.createTempView('people')
# Artik tablo gibi kullanabiliriz people'i.
```

- DF'ler epey scalable'dir.
- Cokca data formatina ve storage system'e destegi var
- Optimizasyonu ve code generation'u gucludur (SQL Catalyst optimizer)
- Big data toollari ve infrastructure'lari ile Spark sayesinde erisilebilir.
- Python, Java, Scala ve R'da API'lari mevcut.

**DataFrame kullanimiyla SparkSQL'i kiyaslayalim:**

SparkSQL:

```py
spark.sql("SELECT age, name FROM people WHERE age > 21").show()
```

DataFrame Python API

```py
df.filter(df["age"]>21).show()
```

Ikisi de tablo olarak sonuc dondurecektir.

### Spark Labaratuvar

Spark normalde Scala uzerinde yazilmis. 
Python'dan PySpark kullanabiliriz tabi, ama bu python'un JVM'e erismesi demek.
JVM'e git geller kodu yavaslatabiliyor.
Buna istisna olarak SparkSQL'i gosterebiliriz, cunku query'leri precompile ediyor. Execution planning engine'i guclu.

Bu PySpark yavasligini minimuma indirgemek icin:

- 'Out of the box' metotlari agirlikli kullanmak lazimmis. Ne demekse...
- Spark metotlarina iterative/frequent call spamlamamak lazim.

Performans isteyen Scala'ya gitsin.

---

SparkContext ve SparkSession yaratilacak.
Sonrasinda RDD olusturulacak ve temel aksiyonlar denenecek.

**SparkContext**, Spark'in giris noktasidir. RDD yaratimi icin kullanilan fonksyonlari icerir. **parallelize()** gibi.

**SparkSession**, SparkSQL ve DataFrame operasyonlari icin gereklidir.

Session'u baslattiktan sonra sira RDD'lerde.
**RDD**ler Spark'in ilkel data soyutlama bicimidir. Fonksyonel programlamadan konseptler kullanarak olusturup manipule edecegiz.

Lab'da **parallelize()** kullanarak RDD olusturuluyor.

#### Lazy Evaluation & Transformations

RDD'ler Immutable demistik. Bu yuzden RDD'lerde islem yapacaksan (map, filter gibi) yeni RDD'ler olusturarak yapiyorsun.

Spark, bu transformation'lari RDD olustururken yapmiyor. 
RDD'ye ilistiriyor bu islemleri. Sen sonuclari cagiracak oldugunda aksiyonlar aliniyor. Sonuclari Driver'a cagirip doner.
Buna **Lazy Evaluation** denir.

Transformation'u cagirmak icin **collect()** cagrilir.

#### Caching

Bi RDD'yi **.cache()** ile cache'lersen, onda yapacagi ilk islemde cache'e de aktarim yapar.
Ayni islemi tekrar cagiracak ol mesela, hopp artik kisa surede yapacak.

#### DataFrames ve SparkSQL

SparkSQL'le calisabilmek icin Spark Session gerekli. Labin basinda kontrol ettik hemen.

**read.json()** ile basitce DF'e aktarabiliriz json dosyalayini.

DataFrame'leri SQL icin temp view'lara donusturebiliriz.
Bu sayede query icinde *FROM* alanina ekleyebiliriz.

Kodda SQL queryleri ile de sonuclari cekebiliriz,
DataFrame'in kendi metotlarini da kullanabiliriz.

#### Orneklere notlar:

**Q2 -** TempView yarattim soru icin. 
Ama komutu tekrar calistiracagimda ayni tempView mevcut diye hata veriyor.

Silip tekrar yukleyebilmek icin: **spark.catalog.dropTempView(...)** metodunu cagirdim.

**Q3 -** Spark Session'u kapatmamizi istemis.

Spark Session'larini hep kapatmak lazim best practice icin.
Resource paylastirma isleri icin lazim genelde.

Pekiii, **context'i kapatmali miyiz?**

Gerekli  degil. Yenisini yaratacaksan kapatman lazim mevcut olani. Onun disinda kalsin.

**SparkContext ile SparkSession farklari nedir?**

Aslinda ilk SparkContext yaratiliyor. Sonra SparkSession olusturuldugunda pek cok utility buraya aliniyor.

Su an, RDD yaratimi icin **SparkContext** (variable'i genelde **sc**),

Kalan islere de **SparkSession** (variable'i genelde **spark**) kullandim gibi.

### Week 3 Spark Highlights

Spark is an open source in-memory application framework for distributed data processing and iterative analysis on massive data volumes​. Both distributed systems and Apache Spark are inherently scalable and fault tolerant. ​Apache Spark solves the problems encountered with MapReduce by keeping a substantial portion of the data required in-memory, avoiding expensive and time-consuming disk I/O.​

Functional programming follows a declarative programming model that emphasizes “what” instead of “how to” and uses expressions.​

Lambda functions or operators are anonymous functions that enable functional programming​. Spark parallelizes computations using the lambda calculus​ and all functional Spark programs are inherently parallel​.

Resilient distributed datasets, or RDDs, are Spark’s primary data abstraction​ consisting of a fault-tolerant collection of elements partitioned across the nodes of the cluster, ​capable of accepting parallel operations​.​You can create an RDD using an external or local Hadoop-supported file, from a collection, or from another RDD. RDDs are immutable and always recoverable, providing resilience in Apache Spark​ RDDs can persist or cache datasets in memory across operations, which speeds iterative operations​ in Spark.

Apache Spark architecture consists of components data, compute input, and management​. The fault-tolerant Spark Core base engine performs large-scale Big Data worthy parallel and distributed data processing jobs, manages memory, schedules tasks, and houses APIs that define RDDs​.

Spark SQL provides a programming abstraction called DataFrames and can also act as a distributed SQL query engine​. Spark DataFrames are conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations​.

## Week 4 - DataFrames & SparkSQL

1. [RDD's in Parallel Programming and Spark](#rdds-in-parallel-programming-and-spark)
2. [SparkSQL & Catalyst & Tungsten](#sparksql--catalyst--tungsten)
3. [ETL with DataFrames](#etl-with-dataframes)
4. [DataFrames Lab](#dataframes-lab)
5. [Spark SQL Real World Usage](#real-world-usage-for-spark-sql)

### RDD's in Parallel Programming and Spark

Primary Data Abstractionumuzdu. 
Node'lara partitionlanir.

#### Transformations

- Aslinda eski RDD'den yenisini olusturarak yapilir.
- Lazy evaluation vardir, action olmadikca computation olmaz.

**Actionlar**

Driver programa transformation sonuclarını donen islemlerdir.
Ornek:

```py
.reduce()
.collect()
```

RDD'lerin Transformation'lari islemesini **Directed Acyclic Graph (DAG)** semasina bagliyorlar.

**DAG:**

- Grafiksel data structure. Kenarlar ve koseler var.
- Her yeni kenar eski bi koseden olusturulur
- Koseler: RDD'leri
- Kenarlar: Operasyonlari temsil eder.
- Fault tolerance sagladigi icin kullanilir. Node'lardan biri giderse, Spark bu DAG'i replike eder ve node'u kurtarir.

**Akis semasi**

1. RDD yaratilirken Spark DAG de yaratir.
2. Spark DAG Schedular'i acar, transformation'u yapip DAG'i gunceller.
3. DAG artik yeni bir RDD'yi isaret ediyor.
4. RDD'yi transform eden pointer Spark Driver Program'a doner.
5. Action olursa, aksiyonu cagiran Driver program sadece aksiyon bittiginde DAG'i isler.

**Transformation Examples**

- **map()** her elementi verilen fonksyondan gecirip yeni bir distributed dataset olusturur.
- **filter()** selection kosuluna uyan yeni bir dataset doner
- **distinct()** Distinct elementlerden olusan yeni bir dataset doner
- **flatmap()** her input elemanini sifir veya daha fazla output elemanina map'leyebilir. icine pasladigimiz fonksyon tek bir item yerine **Seq** donmelidir.

**Action Examples**

- **reduce()** icine paslanan *func*a gore aggregate eder.
- **take()** ilk *n* elemani return eder. (n:input)
- **collect()** Tum elemanlari array olarak doner.
    - Make sure that ? will fit in driver program
- **takeOrdered()** N kadar elemani ya asc sirali doner ya da icine pasladigin fonksyona gore dondurur.

**Akis Gorseli**

![Transformations and Actions](resource/Spark_Transformation_Action.png)

### DataFrames and DataSets

#### DataSets

Spark'in data abstractionlarindan en yenisi.
Distributed data icin API saglar, RDD ve DataFrame gibi.
**Strongly typed jvm objeleri**dir.
Yani, **type-safe**dir. Olusturulurken datatype'i atanir.
Bu sebeple sadece Java ve Scala icinden API'i cagrilabilir.
Python gibi dillerin dynamic data-type(?)i var diye kullanim yapilamaz.
RDD'lerin faydalarini (lambda func., type safety) ve SQL'in faydalarini (optimization) beraber saglar.

**Ozellikleri**

- Immutable: Silinemez veya kaybedilemez. RDD gibi.
- JVM objelerini tablo gosterimine ceviren bir encoderi vardir.
- DataFrame API'ini extend eder.
    - DataFrame = Dataset[Row] # Row: generic untyped JVM object.
    - Dataset = Dataset[T]     # T: Strongly typed JVM object.

**DataFrame veya RDD'ye gore avantajlari**

- Compile-time type safety
- Compute faster than RDD's. Ozellikle aggregate queryler icin.
- SparkSQL'in ve DataFrame'lerin faydalarini beraber getirir
- Catalyst ve Tungsten'in faydalariyla query optimization saglar.
- Improved memory usage and caching.
    - Cunku data-type'a gore structure olusturup memory'de optimizasyon direkt.
- High level aggregate functions saglar:
    - Sum
    - Average
    - Join
    - Group By

**Creating a DataSet**

```scala
// Create dataset from a sequence of Primitive Datatype (string mesela)
val ds = Seq("Alpha","Beta","Gamma").toDS()

// Create dataset from a file for primitive dataType
val ds_string = spark.read.text("file.txt").as[String]

// Create a dataset from a file for a custom datatype
case class Customer(name: String, id: Int, phone: Double)
val ds_customer = spark.read.json("customer.json").as[Customer]
```

**DataSet vs DataFrame**

DataSet | DataFrame
--------|----------
Strongly typed | not typesafe
Unified Java and Scala APIs | Use APIs in Java, Scala, Python and R
Introduced Later | Introduced Earlier
Built on top of DataFrames | Built on top of RDDs

### SparkSQL & Catalyst & Tungsten

Optimizasyondan hedeflerimiz:

- Reduce Query Time
- Reduce Memory Consumption 
- Save organizations time and money

Catalyst ve Tungsten de Spark'in built-in optimizer'lari.
Catalyst rule based seyler saglarken,
Tungsten cpu optimization saglar.

#### Catalyst

- **Rule based** query optimizer for SparkSQL
- Scala'nin fonksyonel programlama yapilarini kullanir
- Yeni optimizasyon teknikleri eklemeye izin verir
- Data-source specific rule'lar tanimlamaya ve yeni data type'lara kural tanimlamaya izin verir

Query calismadan once nasil calistiracagini inceler.
Rule based optimizationa ornek:

- *Tablo indeksli mi?*
- *Query sadece bu indexli kolonlari kullaniyor mu?*

Cost based optimization olsaydi,
Query'nin alacagi **zaman** ve **memory kullanimi** goz onunde bulundurulurdu.

- *Multiple datasetler icin best path hangisidir?*

**Aciklayici ornek:**

Araban var. Lastikleri mevsime gore sectin, yakitini ozel aldin, Yuku azalttin filan.
Bunlar **Rule based** oldu. 

Yola ciktiginda sectigin yolu en kisa olacak sekilde ayarladin.
Bu da **Cost based** oldu.

Catalyst, veri yapisi olarak **Tree**leri kullanir.
Catalyst'in query calistirmasinin dort buyuk asamasi:

- Analysis
- Logical Optimization
- Physical Planning
- Code Generation

**Catalyst Akis Semasi**

![Catalyst Query Optimization Flow](resource/Catalyst_Flow_Chart.png)

- Analysis:
    - Sql query'n ve DataFrame'den bi logical plan olusturur.
    - Plan olusturma isinde katalogdan faydalanir.
- Logical Optimization:
    - Logical Plan'i alir, optimize eder.
    - Bu asama **rule based** asamasini olusturur.
- Physical Planning
    - Optimized Logical plan'lerden, veriye ve query'e maplenmis somut/fiziksel planlar olusturur.
    - Bu fiziksel planlarin costu en dusuk olanini hespalayip alir.
    - Burasi da **cost based** asamasidir.
- Code Generation
    - Secilen plan, java bytecode'una donusturulur.

#### Tungsten

**Cost based optimizer**'mis. CPU ve Memory optimization'u maximize eder.
IO Performansi yerine CPU performansi artirir.

Java orijinalde transactional applications icin tasarlanmis. 
Tungsten de, JVM'i data processing'e uygun hale getirecek metotlar kullanir.

**Features**

- Memory'i aciktan optimize eder. Objelerle veya Garbage Collector'le ugrasmaz.
- Random memory access yerine STRIDE-based memory access kullanir. Boylece **chce-friendly**
- Supports on-demand JVM byte-code generation
- Virtual Function Dispatch(?)leri olusturmaz
- Intermediate data'yi CPU registerlarinda saklar
- Loop Unrolling'i saglar.

### ETL with DataFrames

**Basic DataFrame Operations:**

- **Read** the data
    - into dataframe mesela
- **Analyze** the data
    - Examining columns, data types, no# of rows
    - Aggregated stats
    - Trend Analysis
- **Transform** data
    - Filter specific values
    - Sort data
    - Join dataset with another
- **Load** into Databse
- **Write** file back to disk

Aslinda burada **ETL** gerceklestirdik.

Peki, **ELT** icin konusalim:

- Big data ile cikti bu
- Tum data **Data Lake** icinde bulunur
    - Vast pool of raw data
    - Purpose of the data is not defined
- Each project forms individual transformation tasks.
    - ETL'de ve Data Warehouse'larda transformation her seye uygulaniyor(?) sanirim.

#### Read the Data

- Create a DataFrame
- Create DataFrame from existing DataFrame

Ornekte once pandas DataFrame'ine aktarip, sonra ondan Spark DataFrame'i olusturulacak:

```py
import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
sdf = spark.createDataFrame(mtcars)
```

#### Analyze the Data

DF'in **şemasina** bakabiliriz mesela. Data Type'lari, column adlarini gorebiliriz.

```py
sdf.printSchema()
```

Ayrica **Select** islemleri de Analyze'dir. Spesifik kolonlari analiz ederiz mantiken.

```py
sdf.select('mpg').show(5) # first 5 rows of mpg column
```

#### Transform the Data

Amac: Keep only the relevant data.

- Apply filters
- Joins
- Sources and tables
- Column operations
    - Tum kolonu bir degerle carpmak gibi
    - Converting units of column
- Grouping and aggregations

```py
# filter example
sdf.filter(sdf['mpg'] < 18).show(5)

# aggregate example
car_counts = sdf.groupby(['cyl']).agg({"wt": "count"})\ .sort('count(wt)', ascending=False).show(5)
```

#### Load or Export the Data

Final step of ETL pipeline.

- Export to Databse
- Export to disk as JSON files
- Save data to Postgres Database
- Use API to export data
    - To Postgres DB mesela

### DataFrames Lab

- Iki boyutludurlar
- Columnlar farkli data typelarda olabilir
- Farkli data inputlari alabilir, baska DataFrame'leri bile input olarak alabilir.

Labin kodlari ayri dosyada repoda tutulacak.

#### Load data to Spark DataFrame

Labda once csv dosyasi Pandas DataFrame'ine cevrilecek.
Sonra da Spark DataFrame'ine cevrilecek.

#### Basic Data Analysis and Manipulation

Once review edilecek. 
Sonra Bazi filtreler ekleyip column operasyonlari yapilacak.

Spark'ta **.head()** yerine **.show()** kullanilabilir.

DataFrame'i yeni bir kolonla gostermek icin **.withColumn(**colName, degerler **)** seklinde cagirdik.

#### Grouping and Aggregation

**.gorupby(['column'])** ve **.agg({'column': 'Func'})** kullanimi yapiyoruz.

Sorting icin de **.sort('column', order)** kullaniliyor.

### Real World Usage for Spark SQL

Spark SQL, Structured data tutan(?) ve isleyen yapimizdi.
DataFrame'ler uzerinde query atilabilir.
Java, Scala, Python ve R'da calisir.

View'lar araciligi ile SQL query'leri olusturabiliriz.

- View, temporary table gorevi gorur.
    - Gercekten temporary ise, local scope'u Session'a baglidir. Session bitince view da kalkar.
    - Global Temporary View'lar da Spark Application icinde global scope'a sahiptir.

#### Local Scope Ornegi:

```py
# Create DataFrame from file
df = spark.read.json('people.json')

# Create a temp view
df.createTempView('people')

# Run SQL Query
spark.sql('SELECT * FROM people').show()
```

#### Global Scope Ornegi

Keyword'lerdeki degisime dikkat et:

```py
# Create a global view
df.createGlobalTempView('people')

# Run SQL Query
spark.sql('SELEVT * FROM global_temp.people').show()
```

#### Aggregate Data

DataFrame'lerde **count(), avg(), max(), min()** filan vardi built-in,

SQL query'leri ile de tabi ki aggregation saglayabiliriz DF'lere ihtiyac duymadan.
TableView'lar ile de saglayabiliyormusuz.

**Aggregation Ornegi:**

```py
# Setup
import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
sdf = spark.createDataFrame(mtcars)

# DF ile aggregation hatirlatma
car_counts = sdf.groupby(['cyl'])\
    .agg({'wt':'count'})\
    .sort('count(wt)',ascending=False)\
    .show(5)

# Spark SQL Usage
sdf.createTempView('cars')
sql('SELECT cyl, COUNT(*) FROM cars GROUPBY cyl ORDER BY 2 DESC').show(5)
```

#### Data Sources

- **Parquet Files**
    - Columnar format
    - Spark SQL read/write destegi sunar.
    - Spark SQL'in dosyayi load etmesine gerek yoktur
- **JSON Datasets**
    - Spark schema'yi okuyup DataFrame'lere aktarabilir
- **Hive Tables**
    - Spark, Hive'da tutulan dataya read/write yapabilir.

### SQL Lab

CSV dosyasini Pandas DataFrame'ine aktarip, Spark DataFrame'ine cevirecegiz.

Her zamanki islemleri yapip SDF'i temp view olarak kaydedince, SQL query'lerini calistirabilir olduk.

#### Pandas UDF for Columnar Operations

**UDF:** User Defined Functions

Python'da calistirilan UDF'ler satir satir calisiyor.
Serialization ve cagirma icin overhead olusuyor.
Bu yuzden data pipeline'larda UDF'ler **Java / Scala** uzerinde olusturulup **Python** uzerinde cagrimlari yapiliyor.

**Pandas UDF**leri Apache Arrow uzerine kurulu bir sistem. Hem Python uzerinde yazilmis UDF'ler, hem de duz Python'daki kadar yuk olusturmuyor. 

Ayrica SQL ici cagrim yapabilmek icin **@pandas_udf(** return type **)** yazabiliriz.

Labdaki ornekte, Scalar Pandas UDF kullanip wt (agirlik) kolonunu emperyalden metrik sisteme cevirecegiz.

### Summary & Highlights

- RDDs are Spark's primary data abstraction partitioned across the nodes of the cluster​. Transformations leave existing RDDs intact and create new RDDs based on the transformation function​. With a variety of available options, apply functions to transformations perform operations. Next, actions return computed values to the driver program. Transformations undergo lazy evaluation, meaning they are only evaluated when the driver function calls an action.

- A dataset is a distributed collection of data that provides the combined benefits of both RDDs and SparkSQL​. Consisting of strongly typed JVM objects​, datasets make use of DataFrame typesafe capabilities and extend object-oriented API capabilities. Datasets work with both Scala and Java APIs​.  DataFrames are not typesafe. You can use APIs in Java, Scala, Python. Dataset​s are Spark's latest data abstraction.

- The primary goal of Spark SQL Optimization is to improve the run-time performance of a SQL query, by reducing the query’s time and memory consumption, saving organizations time and money. ​Catalyst is the Spark SQL built-in rule-based query optimizer.​ Catalyst  performs analysis, logical optimization, physical planning, and code generation.​ Tungsten is the Spark built-in cost-based optimizer for CPU and memory usage that enables cache-friendly computation of algorithms and data structures.

- Basic DataFrame operations are reading, analysis, transformation, loading, and writing. ​You can use a Pandas DataFrame in Python to load a dataset and apply the print schema, select function, or show function for data analysis. ​For transform tasks, keep only relevant data and apply functions such as filters, joins, column operations, grouping and aggregations, and other functions.

- Spark SQL consists of Spark modules for structured data processing that can run SQL queries on Spark DataFrames and are usable in Java, Scala, Python and R. Spark SQL supports both temporary views and global temporary views​. Use a DataFrame function or an SQL Query + Table View for data aggregation. Spark SQL supports Parquet files, JSON datasets and Hive tables​.

## Week 5 - Spark Architecture

1. [Introduction](#introduction-to-spark-architecture)
2. [Spark Cluster Modes](#spark-cluster-modes)
3. [Run Spark Application](#run-a-spark-application)
4. [Spark Lab 4](#spark-lab-4)
5. [Summary & Highlights](#week-5-summary--highlights)

### Introduction to Spark Architecture

2 Asil islem uzerinden Spark calisir:

- **Driver Process**
    - One process per application
    - Runs application's user code
    - Creates work
    - Sends work to the cluster
- **Executor Process**
    - Runs multiple threads to perform work
    - Many executors in a cluster
    = One or more executors per Node (depends on config)

---

**Spark Context**

Application ile beraber ayaga kalkar.
DataFrame'lerden ve RDD'lerden once yaratilmasi zorunludur.

Yaratilan **RDD** **ve** **DataFrame**'ler bir **Context**e baglidir.
Context, RDD ve DataFrame'lerin tum kullanimi boyunca active kalmalidir.

---

**Spark Jobs**

Driver Program kullanicinin kodlarina gore is yaratir. 
**Job** diyelim bunlara.
Job'lar, paralel calisabilir.

**Context** ise bu joblari **Task**lara boler.

![Spark Jobs](resource/Spark_Jobs_1.png)

---

**Spark Tasks**

Job'dan olusturulan Task'lar, datanin farkli farkli parcalarinda calisir.
Her biri bir **Partition**'da calisir.

Task'lar, Executor'lerde **paralel** calisir demek yani.

![Spark Tasks](resource/Spark_Tasks_1.png)

---

**Worker Nodes**

Cluster'daki nodelardir. 
Executor process'leri ve calistirir boylece tasklar calisir.

Her **Executor**e, tasklari calistirmalari icin resource (cpu core + memory) tahsis edilir.
Core basina bir task calistirabilir.

Her bir executor, kendi **data caching**inden sorumludur.

Executor sayisini ve cpu core'larini artirmak, 
cluster'daki **parallelism**i artirir.

Tum cekirdekler kullanilana kadar, tum taskler ayri thread'lerdedir.

Task bittiginde, Executor sonuclari:

- Yeni bir RDD'ye koyabilir
- Driver Program'e direkt iletebilir.

Node basina dusen core sayisini executor'un kullanacagi node sayisina gore ayarlamak lazimmis (?)

---

**Stages & Shufling**

**Stage:** Ayni partition'da yapilan tasklara stage denir.

**Shuffle:** Stage'lerin sinirlarini olusturur. 
Ayrica, baska partitionla is yapilacaksa meydana gelir.

Grafikle daha rahat:

![Spark Shuffle](resource/Spark_Shuffle_1.png)

Shuffle'lar:

- Costly'dir.
    - Data Serialization
    - Disk and Network I/O
- Operasyonlar, mevcut partition haricinde baska bir partition gerektirirse kullanilir. 
    - Ornek olarak: Group by
- Shuffle oldugunda, Spark cluster icinde dataseti tekrar dagitmis olur.

Baska bir Shuffle ornegi:

![Shuffle Example](resource/Spark_Shuffle_2.png)

1.  'a' Datasetin olsun. Partirioning ile **1a** ve **2a** var elinde.
2. Transform ediyorsun ama baska datalara ihtiyac olmadan. Columnar operation olabilir ornegin. Artik yeni datasetin 'b'. **1b** ve **2b** elinde.
3. GroupBy kullanimi yapacaksin. Partitionlar arasi bilgi lazim. Shuffle oluyor, **1c** ve **2c** seklinde 'c' Datasetin olusuyor.
4. Action oldugu zaman bu partitionlar aktariliyor. Ornegimizde Driver'a collect ediliyor.
    - **Dipnot:** Buyuk datalari driver'a cort diye collect etme. Memory'sini yer bitirir. Data buyukse, reduction uygula collection'dan once.

---

**Recap**

![Spark Architecture](resource/Spark_Architecture_1.png)

- Mimari, **Driver** ve **Executor** islemlerinden olusur.

- Cluster, **Cluster Manager** ve **Worker Node**lari icerir.

- Spark Context, **tasklari** Cluster Manager'a **schedule** eder.

- Cluster Manager, cluster'in **resourcelarini manage** eder.

---

Driver Program, Client olarak veya Cluster icinde calisabilir.

- **Client Mode** - Driver process'i Cluster disinda calistirildiginda olur.
- **Cluster Mode** - Driver process'i cluster icinde calistirilir.

Iki modda da, Driver'in Cluster'la **iletisim** kurmasi **zorunludur**.

### Spark Cluster Modes

**Spark Cluster Manager**i hatirlayalim:

- Cluster ile iletisime gecip application icin gerekli **resouce**u temin eder.
- Application'un disinda bir servis olarak calisir ve cluster type'i abstract eder

- Uygulama calisirken Spark Context, tasklari olusturup hangi resource'larin gerekli oldugunu Cluster Manager'a soyler.
- Ardindan Cluster Manager, executor core'lari ve memory resource'lari ayirir cluster icin.
- Resourcelar tahsis edilince, Tasklar Executor Process'lere aktarilir.

---

**Cluster Manager Cesitleri:**

- **Spark Standalone**: Spark ile gelir, basit clusterlar icin idealdir.
- **Hadoop** **YARN**: Hadoop'un Cluster Manager'i.
- **Apache** **Mesos**: General purpose cluster manager with some benefits.
- **Kubernetes**: Runs containerized applications.

Kullanilacak cluster-manager'i secmek su etkenlere baglidir:

- Kurulum kolayligi
- Portability
- Deployment
- Data Partitioning ihtiyaclari

---

**Spark Standalone**

- Built in geldigi icin no additional dependencies
- Fastest way to setup Spark Cluster
- Spark icin ozel tasarim, **not** general-purpose.

**Spark Standalone's Components:**

- **Workers**: Executor process'leri calistirir
- **Master**: Worker'lari cluster'a baglar.
    - Cluster Node'lardan herhangi birinde olabilir
    - Eger worker'larla beraber bulunuyorsa, tum resource'u worker'lara verme. Master da resource tuketmelidir.


**Setup Spark Standalone:**

1. Start the Master
    - Master'in URL'ini ve Port'unu verecektir.
2. URL sayesinde Worker'lari calistirabiliriz.
3. Master ve Worker'lar ayaktaysa, Spark application calistirilabilir.
    - Calistirirken arguman olarak Master URL'i veriyoruz ki baglansinlar.

---

**YARN:**

- General Purpose
- Supports many other big data ecosystem frameworks
- Kendi config ve setup'ini gerektirecek
- Dependency'leri var. Spark Standalone'a gore deploy etmesi daha zor.

**Spark'i YARN'da calistirmak:**

(Yarn ayakta diye kabul ediyoruz)

1. `spark-submit`'i `--master YARN` opsiyonu ile calistiriyoruz:

```sh
$ ./bin/spark-submit \
    --master YARN \
    <additional configuration>
```

2. Spark, default Hadoop config dosyalarina bakip, YARN'a nasil baglanacagini ayarliyor.

---

**Apache** **Mesos:**

Faydalarinin basinda **partitioning** var:

- **Dynamic Partitioning** Spark - Diger Frameworkler arasi partitioning
- **Scalable Partitioning** Spark instance'lari arasinda partitioning

Kurulumu ekstra adimlar gerektiriyormus. Link birakmislar Allah razi olsun.

[Mesos'la Setup Linki](https://spark.apache.org/docs/latest/running-on-mesos.html)

---

**Kubernetes**

Containarized applicationlari calistirir.

- Spark uygulamalari daha **portable** olur 
- **Automate** **deployment**
- Simplifies **dependency** **management**
- **Scale** the cluster

Spark, built-in native Kube scheduler kullaniyormus.

**Spark'i Kube ile calistirmak:**

```sh
$ ./bin/spark-submit \
    --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> \
    <additional configuration>
```

---

**Local Mode**

Spark'i herhangi bir cluster(/manager) olmadan local olarak calistirabiliriz.

- Cluster'a baglanmaz. Calistirmasi kolay.
- `spark-submit` ile ayni process'te calisir.
- Task'lar icin threadler kullanir.
- Test / Debug islemleri icin ideal olabilir.
- Single process icinde calistigi icin, performance limited.

**Setup Local Mode:**

User `--master local[#]`

```sh
# Launch Spark in local with 8 cores

$ ./bin/spark-submit \
    --master local[8] \
    <additional configuration>

# Launch with all available cores

$ ./bin/spark-submit \
    --master local[*] \
    <additional configuration>
```

*Not:* Girdigin tum configler local mode'da gecerli olmayabilir.

### Run a Spark Application

**Spark-Submit**

Bir script.

- Unified interface for submitting applications
- bin/ dizininde bulunur
- Tum cluster typelari icin cagrilir ve birusu config ayarlayabilir.
- **Unified** **olusu:** Localden cluster mode'una mesela tek argumanla degistirebilirsin.
- Application language veya cluster manager type'dan bagimsiz ayni sekilde calisir.
    - Python ve Java app'lerini ayni anda calistirabilir mesela.

---

**Using spark-submit**

Soyle calisacaktir:

1. Command line arguement/option'larini alir
2. `conf/spark-defaults.conf` altindaki ek ayarlari okur
3. `--master` ile belirtilen cluster manager'a baglan // local'de calis
4. Application dosyalarini (JAR veya Python) cluster'a dagiitip calistir.

---

**Common `spark-submit` Options**

![Spark Submit Options](resource/Spark_Submit_1.png)

Bunlarin sonuna `--conf` ile ek konfigurasyonlar eklenirmis.

Onlarin sonuna da `<application-path>` ve `<application-args>` gelir.

Path dedigi JAR veya PyScript adresi. 
Python icin `--py-files` diyip veriyorsun.

- Jar'lari direkt verebiliriz
- Python icin `.py`, `.egg`, `.zip` verebiliriz.

Args da programa paslanan argumanlar. `args[]` yani kurban oldugum.

---

**Spark**-**Submit** **Examples**

1. YARN ile Scala'daki `'SprakPi'` isimli programi calistiracagiz. Arguman olarak 1000 paslayacagiz.

```sh
# Launch Scala SparkPi to a YARN cluster

./bun/spark-submit \
    --class org.apache.spark.examples.SparkPi \
    --master YARN \
    /path/to/examples.jar \
    1000
```

2. Python'daki `SparkPi` cagrilacak. Spark Standalone kullanilacak.

```sh
# Launch Python SparkPi with Standalone Cluster at 207.184.161.138

./bin/spark-submit \
    --master spark://207.184.161.138:7077 \
    examples/src/main/python/pi.py \
    1000
```

---

**Application** **Dependencies:**

Dependency'leri yonetmek icin:

- Projeleri veya kutuphaneleri application ile beraber paketle. Boylece driver ve executorlere erisilebilir olur.

- Java ve Scala icin **Uber**-**JAR** olusturmak iyi olacaktir.
    - Uber Jar: Dependency ve kutuphanelerin beraber paketlendigi JAR dosyalari.
- Python icin sunlari sagla:
    - Cluster Node'lari ayni versiyondaki dependency'lere erisiyor olmali
    - Python versiyonlari ayni olmali
    - `--py-files` argumaniyla dependency'leri paslayabiliriz.
    - Virtual environment kurularak da isolated cozumler saglanabilir.

---

**Spark** **Shell**

- Spark API icin kullanisli bir yontem
- Data Analizini interaktif olarak yapmani saglar
- Local veya Cluster modda kullanilabilir. `spark-submit` ile ayni option'lari paylasir.
- Scala'da veya Python'da baslatilabilir.

Spark Shell basladiginda, **SparkContext** ve **SparkSession** da otomatik olarak baslatilir.

Action'lar Spark Shell'e girildiginde Driver'a girilmis gibi *job*lara donusur ve *task*lar olarak cluster'a aktarilir.

---

**Spark Shell'in sagladigi bilgiler**

Lokalde acildiginda sundugu bilgiler:

- Spark Load Log konumu/dosyasi
- Spark web UI address
- Variable names for SparkContext / SparkSession
- Version info for important libraries (JDK, Scala)

---

**Scala** **Shell** **Examples**

1. Launch Scala Spark Shell
2. Create distributed DataFrame with column `'id'` and 10 values (0-9)

```scala
val df = spark.range(10)
// df: org.apache.spark.sql.Dataset[Long] = [id: bigint]
```

3. Add a column that evaluates an SQL expression for modulo of 2 and show first 4 rows as result.

```scala
df.withColumn("mod", expr("id % 2")).show(4)
// Shows result as table
```

*Not:* `.show(4)` bir **Spark** **Action** olarak islev gordu.

### Spark Lab 4

- Lab icin docker ve docker-compose kurulumu yaptim.
- Git ile ilgili repoyu cektim
- `sudo dockerd` ile docker daemon'unu calistirdiktan sonra
- `docker-compose up` komutu ile docker-compose'u calistirdim.
    - **Master** ve **Worker** nodelarin calistigini teyit etmek icin `docker container ls` komutu ile calisan docker container/image'larini gordum.
- Python'da **PySpark** ile yazilan kodu calistirmak icin birkac hatayla ugrastim:
    - `JAVA_HOME` Path'ini dogru ayarlamam gerekti
    - Kullanilan JDK surumunu 18'den 17'ye aldim.
    - 17 de calismayinca JDK 11 kurulumu yapip onu kullandirdim.
- Kod icerigi:
    - Master Node URL'inden SparkContext'i aliyor
    - SparkSession'u aliyor
    - Session uzerinden kucuk bir Spark DataFrame'i olusturuyor
    - DataType'lari yazdiriyor
    - `.show()` aksiyonu cagiriyor.
- Kodu calistirabildigin zaman, Spark UI'da `Running Applications` altinda gozukuyor.
- Is bitirildiginde `Completed Applications` altina geciyor.
- UI uzerinde, executor basina ne kadar core/memory verildigi gozukuyor.

### Week 5 Summary & Highlights

- Spark Architecture has driver and executor processes, coordinated by the Spark Context in the Driver​.
- The Driver creates jobs and the Spark Context splits jobs into tasks which can be run in parallel in the executors on the cluster​. Stages are a set of tasks that are separated by a data shuffle. Shuffles are costly, as they require data serialization, disk and network I/O.​ The driver program can be run in either client Mode (connecting the driver outside the cluster) or cluster mode (running the driver in the cluster).
- Cluster managers acquire resources and run as an abstracted service outside the application. Spark can run on Spark Standalone, Apache Hadoop YARN, Apache Mesos or Kubernetes cluster managers, with specific set-up requirements.​ Choosing a cluster manager depends on your data ecosystem and factors such as ease of configuration, portability, deployment, or data partitioning needs. Spark can also run using local mode, which is useful for testing or debugging an application.
- 'spark-submit’ is a unified interface to submit the Spark application, no matter the cluster manager or application language​. Mandatory options include telling Spark which cluster manager to connect to; other options set driver deploy mode or executor resourcing. To manage dependencies, application projects or libraries must be accessible for driver and executor processes, for example by creating a Java or Scala uber-JAR​. 
- Spark Shell simplifies working with data by automatically initializing the SparkContext and SparkSession variables and providing Spark API access.













