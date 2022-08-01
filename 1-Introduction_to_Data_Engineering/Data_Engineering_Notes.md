# Introduction to Data Engineering

Notes are from an old OneNote note, seperated by date added.

1. [February 15](#15-february)
2. [February 17](#17-february)
3. [February 22](#22-february)
4. [March 1](#1-march)

## 15 February

ETL - extract transform load
Kafka - stream processing

ELT de var
Unstructured için ideal, data lake için ideal.
Cloudda filan var bunlar.
Data daha hızlı hazır
Big datada filan da bunlar var. yeni işler yani.

Data pipeline da datanın kullanıma hazır edilme yoluna verilen diğer bir isim. Etl elt ile değiştirilebilir ama daha genel ve kapsamlı bir tabir diye anladım.

Hadoop storage / process big data
Hive: warehouse built on top of hadoop
Spark: data analytics in real time

Hive: Read based late query times. Çükü arşiv gibi galiba. SQL ile daha rahat erişirmişsin hive içinde. Analize filan iyiymiş

Spark kendi clustering teknolojisiyle de çalışabiliyormuş, hadoop ile de.

## 17 February

### Data architecture

**Data Ingestion/Collection:**
Data toplar. Streamlerden batchlerden.
Bağlantı kurar, transfer data.
Maintain info about data collected in metadata repository.
Kafka da collection için kullanılabilir

**Storage and integration:**
Store
Transform and merge
Make available for stream/batch.
Rdbms'ler böyle. Clouud based de olabilir (db as a service)
NoSql de olabilir. Bunlar storage idi. Integration da başka toollar içeriyor.
Integration platform as a service de var cloud hali. iPaaS

**Data Processing:**
Read data from storage and apply transformation
Query ve prog language'e izin verecek.
Transformationdan kasıt structuring olabilir. Form veya schema değiştirilebilir.
Normalization olabilir: cleaning database of unused data
Denormalization: combine from multiple table to singular.
Data clearing: fix irregular data

**Analysis user interface:**
Data consumerler burada, analistler, business stakeholderlar burada. Scientist analists burada. Diğer appler burada. Qyery ve prog lange izin verecek burası.

**Data Pipeline:**
İmplement and maintane flowing data pipeline.

--------------------

Db'ler için Normalization var. Trx based db için baya iyi ama analytic based için kötü

--------------------

**Cia**
Confidentiality: kim erişiyo
Integrity: kaynaklar güvenilir
Availability: kaynaklar available

Cia 4 yerde geçerli olmalı:
- **Physical infrastructure:** 
    - access / surveilance / power feeds / heating cooling mech / environmental threats
- **Network:** 
    -firewall / access control / segmentation-local area networks / protocols / intruer detection-preventation
- **Application Security:** 
    -Threat modeling / Secure Design / Secure Coding / Security Testing
- **Data Security:** Monitoring filan olmalı.
	- Data at rest için: Authentication systemleri / encryption
	- Data in transit için: encryption methodlar https filan. 

## 22 February

**Data çekme metodları:**
- SQL
- API'ler
- Web scrape
- Sensor data
- Data Exchange
- RSS?
- Diğer-Third party kaynaklar? Vs vs

**Data Wrangling nedir?**
Datayı raw datadan kullanılabiblir dataya çevirme işlemi

**Data Transformation:**
Data structure bozma (union / join)

**Normalizing/Denormalizing:**
	Nor: Kullanılmayan data silinmesi
	Deno: multiple datayı tek yerde birleştirme
	Böylece query fasten
	
**Cleaning: fix ireegularities**
	1-Detect issues errors
	2-Validate
	3-Profiling
	4-Visualization
	
### Sorunlar: 
- **Missing values**
	- Filtreleyebilirsin
	- Imputate edebilirsin, ortalama değer kaçsa onu verebilirsin.
- **Duplicate data** - silinmeli
- **Irrelevant data** - temizleee
- **Data type düzeltmeleri yapılmalı**
- **Standardize et** (date formats, string case'leri)
- **Syntax errorları** (white spaceler typolar formatlar)
- **Outlier'**ları incele ve karar ver ne yapılması gerektiğine

## 1 March

Data incelemek için sql komutlarını inceledik
**Stddev** standard deviation
Min max like where
Group by

Performans metrikleri
Failures
Resource utilization
Trafik
Latency

Monitoring konusunda monitor edebileceğimiz çokça metrik var.
Onları saydı

Data governance
GDPR regulastionu var EU icin.
USA icin her state kendisi.

