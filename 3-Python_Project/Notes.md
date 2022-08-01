# Notes

## ETL

**glob** kutuphanesi sayesinde dizinde bulunan **.csv** dosyalarinin isim listesini cekebiliriz.
**.json** icin de yapabiliriz aynisini.
Pandas'da **.read_csv

```py
glob.glob('*.json') # dizindeki .json dosyalarin isimleri,
                    # liste olarak doner.
```

**Extract** asamasi icin pandas'in **read_json(\*)** gibi metodlarini kullanip, DataFrame'lere veri aktarabiliriz.
DataFrame'e **append(\*)** ile datalari ekledik.

**Transform** icin mesela, data standardization yapalim. Height bilgisini inch'ten cm'e ceviriyor. Pandas sayesinde tum kolonu tek satirda guncelleyebiliriz:

```py
df['Height'] = round(df.height * 0.0254, 2)
```

**Load** icin de dataFrame'i bi dosyaya aktaricaz. 
Pandas'in built-in **to_csv(\*)** metodunu kullanabiliriz. 

ETL bitti diye sevinme. **LOG** ekle log!

```py
from datetime import datetime

def log(message):
    timestamp_format = '%Y-%h-%d-%H-%M-%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open('logfile.txt', 'a') as logFile:
        logFile.write( timestamp + ',' + message + '\n' )
```

Lab'da excercise kismina geldim kaldim.
Onceki ornekte Transform kisminda takildim, labda calisti bende calismadi.
Tum column'a round(...) atamadim hata aliyor.

