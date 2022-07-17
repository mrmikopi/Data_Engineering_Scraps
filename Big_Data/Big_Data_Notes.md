# Big Data with Spark & Hadoop

Notes from videos/labs. Mostly in Turkish.

## Content

1. [Week 1 - Introduction](#week-1---introduction)
2. [Week 2 - Hadoop](#week-2---hadoop)

## Week 1 - Introduction

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

**Primary Node:** aka. Name Node. File access'i duzenler. Secondary node'un tasklarini yonetir. Her CLUSTER'da 1 tane.

**Secondary Node:** aka. Data Node. Read Write requestlerini gerceklestirir. Cokca olabilir.

Primary node, is ustlendigi zaman kendisine en yakin rack'leri onceliklendirir. Maximizing efficiency.

*Rack: 40 veya 50 adet, ayni networku kullanan node toplulugu*

Rack awareness calisiyor Hadoop. Onceliklendirme yaptigi gibi, ayrica replikasyon yapilan rack'leri de farkli tutuyor ki fault proof devam.

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