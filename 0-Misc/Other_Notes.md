# Other Topics & Notes

1. [Data Normalization](#data-normalization)

## Data Normalization

6-7 adımlı bir process. Sıralı gitmen gerekiyor ki diğer adımları uygulayabil.

Database'i büyük masraflı değişikliklerden koruyacak şekilde datayı düzenleme metodlarıdır.
Relational dbler için geçerli.

4NF (4'th normal form)'den sonraki adımlar akademik problemleri çözüp, günlük hayatta az rastlanırmış.

### DB Gereksinimi

Primary key ile uniqueness sağla.

### 1NF 

Her sütun, tek değer içermeli. Küme değerler veya nested değerleri yallah başka tabloya.
Başka tablonun içine de bi foreign key attık ohh.

### 2NF 

Diyelim tüm bilgileri aynı 2 kitap var, ama sadece Basılı / E-kitap bilgisinin olduğu kolon farklı. Ona göre fiyat kolonu da değişsin. Composite Key olan tablolarda bunu da ayırmak normalizationun 2NF'ini oluşturuyor. Duplicate olan ve değişmeyen tüm değerleri "kitap ismi" kolonuna bağlayıp bi tabloda tuttuk, Format-Price tablosunu oluşturup kitap ismi / format / price bilgilerini de oraya bağladık. Kitap ismi, yeni tablonun "candidate key"i oldu.

### 3NF

Diyelim tabloda "Author" ve "Author Nationality" diye iki kolon var. Nationality olan, Author'a bağımlı bi kolon. O değişse bu da değişecek vs. vs. Hoppp, bunlara da kendi tablolarını açtık. Book'ta sadece Author'u tuttuk.

### 4NF 

Diyelim bi tablon var, non-key kolon yok. 3 kolon olsun, üçü bir aradayken uniqueness sağlasın.
Tamam üçü birden uniqueness sağlıyor ama,
Diyelim ki bi kolon, aslında diğer kolondaki tüm değerler için mevcut. Yani bakınca, "ulan zaten tüm C kolonu değerleri için B'deki tüm değerler mevcut" dedirtiyor. O zaman hopp tabloları ayırıyorsun.
(Karışık biraz, wikipediadaki örneklerden buldum. 4NF'in sayfasına ve Database Normalization'daki akıcı örneğe bak.)
O her koşulda tekrar eden (B) kolonla her koşulu sağlayan (C) kolonu ayrı ayrı iki tabloya ayırıyorsun, A kolonu sabit kalıyor ikisinde de mevcut oluyor.
Aslında, B de C de ayrı ayrı A'ya bağımlı oluyor sanırım.

**AMAA DİPNOT:** 

Eğer tüm B değerleri C'lerin hepsinde yoksa!!! O zaman tabloların birleşik hali 4NF'i sağlıyor kendiliğinden.

### ETNF (Essential Tuple Normal Form) 

Diyelim üç kolonlu bi tablo. Ama A kolonundaki değerler spesifik B kolonu değerlerini karşılıyor. B'deki değerler C'deki spesifik değerlerle eşleşiyor. C'deki değerler de spesifik A değerleri ile sadece mevcut. Unique belirten key hiyerarşisi düşün, üç ilişkinin de birbirine üstünlüğü yok ama üçü de bi uniqueness sağlıyor. Önemli bilgiler yani.
4NF'i sağlıyor bu hali ama ETNF için decompose edeceğiz.
Meksika açmazını açıyoruz. Üç ilişki için üç tablo. Evet...

A-B relations, B-C relations, C-A relations diye 3 tablo.

### 5NF 

Bu da birazcık karışık. Bir tablo, daha fazla parçalanamayacak konumda olmalı. Nasıl yani?
Diyelim kolon ilişkilerine göre bi tık daha parçaladın. Ama tabloları natural join yaptığın zaman asıl datanı koruyamıyorsun, data sayısı artıyo mesela. No no no. Demek ki, tablonun o ilk hali, kolon ilişkilerine göre daha da parçalanamayacak haldeymiş. 5NF'i sağlıyormuş.
4NF'i daha da parçalayabiliyorsun bazen, 5NF'i daha da parçalayamıyorsun.

### DKNF (Domain Key Normal Form) 

Diyelim Sayfa sayısı diye bi kolon var, bi de "Kalınlık" diye bi kolon var kitaplar için. Bu ikisi birbiriyle ilişkili ama ne domain constraint ne de key constraint imiş.

Bu durumda, "Kalın" ı kalın yapan sayfa sayısı bilgisiyle, "ince" yi ince yapan sayfa sayısı bilgisini bi Constants tablosu gibi tabloda tutuyorsun. DKNF'yi sağlıyor. 

### 6NF 

Tabloda sadece Primary key ve MAX TEK BİR DİĞER KOLON olmalı.
Yani row'un her bilgisini ayrı tabloda tutuuyorsun. OLTP işlerinde fazla tablo maliyetinden ötürü tercih edilmemeli :) 