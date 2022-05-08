# Python Notes
(in Turkish, mostly)

## Table of Contents

1. [Intro](#intro)
2. [Lists](#lists)
3. [Strings](#strings)
4. [Tuples](#tuples)
5. [Lists](#list)
6. [Sets](#sets)
7. [Conditioning](#conditioning)
8. [Logic Operators](#logic-operators)
9. [Loops](#loops)
10. [Functions](#functions)

## Intro
Type öğrenme fonskyonu: **type()**

### Typecasting 

```py
    float(1) : 1.0
    int(3.99) : 3  (asagi yuvarliyor fix)
    int('1') : 1
```

### Booleans 

Booleanların başı uppercase

**True / False**

```py
    bool(0) = False
```

### Divisions

**/** = float division

**//** = integer division.

25 / 5 : 5.0

### Kullandigim metodlar:

```py
Print('string')

sys.version (import sys lazim)
```

*#Comments*

sys.float_info  : float hakkinda teknik bilgiler

## Lists

Listelerde negative indexing var.
Son elemana 

```py
List[-1] diyerek ulasabilirsin
```

Listelerde ayni type aranmaz.
Farkli type nesneler ayni listede durabilir

Tuple'lar: ('A', 2) mesela.
Listeye bunlar bile girebiliyor, nested listler de girebiliyor.

```py
liste[4:9] // dersen indexi 4 9 arasi degerleri slice eder (ilk dahil ikinci degil)

.extend() // listeye eleman ekleme fonksyonu. 
list.extend(  [ 1 , 'C' ]  )  : 2 eleman ekledik
```

O sondaki listeyi tek bi eleman olarak eklemek istiyorsan da:

    
```py
append metodunu kullanacaksin. append( [array] ) yapaceksin.
```

Eleman degistirme:

```py
a[0] = 'Hoppp yeni deger';
```

Eleman silme:

```py
del(a[1])
```

## Strings

```py
string.split() # bize stringi KELIME KELIME split eder
```

Delimeter de alabilir tabi. split(,) dersin, virgule gore split eder

Referanslar javadaki gibi.
Ayni degeri gosteren referanslardan birini degistirirsen,
Diger referansin degeri de ayni seyi gosterdigi icin degisecek.

O yuzden, listeleri referanslarla degistirmek yerine klonlayabiliriz.

```py
B = A[:] diyorsun, hoppaa
```

Listeleri concat etmek (yazdirirken filan) icin + operatoru

```py
A = [ asdasd ]
B = [ Ikincil Degerler ]
A + B : [ adsasd, Ikincil Degerler ]
```

Tek tırnak veya cıft tırnak
Stringler array gibi kullanilabiliyor.

```py
String[0]   = stringin ilk karakteri
String[-1]  = stringin son harfi. Dogal olarak, negatif index de gecerli 
```

```py
Array[::2] demek, her 2nin modu eleman demek.
    
    string = "Bir String" olsun
    string[::2} = [BrSrn] donecek
```

Sayi yazmadan : koymak = 0 yazmak.
**string[0:5:2]** olsaydi **= [BrS]**

**string[5:6]** dersen!!!
5\. indexe git, 6. indexe kadar al demek (sadece 5)

**6 uzunlukta bisey al degil!** *(Tekrar baktim ve onayliyorum)*

```py
len(string) # uzunlugu verir
```

Concat, arraylardeki gibi **( + )** operatoru ile yapilir.

Stringleri Carpip Multiple edebiliriz.
    
```py
String * 3 = "Bir StringBir StringBir String" olurdu
```

Stringler immutable, java gibi.

```py
String[0] = "C"  diyemezsin
```

Onun yerine referansi yeni bi stringe point et

Escape Character: **\\**

- \n = new line
- \t = tab
- \\\ = backslash

    text = r"\nayir \nolamaz"    
    print(text) : "\nayir \nolamaz"

Bu bastaki **r**, escape'leri onluyor

### Bazi string metodlari:

```py
string.upper() = uppercase halini dondurur
string.replace("Degisecek kelime", "yeni kelime");
string.find("sub") = stringin icinde "sub" kelimesi kacinci indexte basliyor. 
                    Yoksa -1
```

## Tuples:

Sirali dizilerdir.
*(1,5,4,6,10,9)* boyle olur mesela. Sayilarin sirali olmasi sart degil

Bi tuple'da farkli typelar olabilir.
Ama tuple'in kendi type'i var **(tuple)**

Yine indexlerle erisim.

```py
Tuple[0] = ilk eleman. Negatif index de var yine
```

Concat yine **+** ile.
Slice yine var **tuple[1:3]** gibi.
**len()** de var
append ve extend **yok**!

```py
sorted(tuple) ile sortlayabiliriz
```

Stringdeki find() yerine burada **.index( item )** var

**TUPLE'LAR IMMUTABLE**.
Listler degil.
Degistirilemedigi icin,
Ayni seyi gosteren iki referanstan biri degisirse,
Digeri **degismiyor**.
String de boyle immutabledir.

```py
bisey = sorted( tuple ) ile sortlayabiliriz
```
Ama dondurulen type List olur! 
**[1,2,3]** olur elinde.

## List 

anam babam array.
Koseli parantez reis:

```py
[0:5]
```

**+** operatoru liste concat eder.

Listeler **mutable** olduğundan ilk elemanı son elemanı vs. Değiştirebiliriz.

```py
del(index) yaparak silebiliriz listeden.
```

String'deki **split()**, liste donduruyordu.
Delimeter de verebilirsin icine, ona gore boler

Mutable oldugu icin,
Ayni objeyi refere eden iki referanstan birini degistirirsen,
**Digeri de degisir!**

Listede degismesin istiyosan, ayni objeyi refer ettirmeyeceksin de,
**Klonlayacaksin** arrayi. B = A [ : ] Şeklinde

Tuple ile List concat edilemiyor lol denedim.

## Dictionaries

Map yahu

**Key ve Value**'ler var.
Key'ler **Immutable** olmali. **Unique** de olacak.
Her keyin yanina  **( : )**  ile value eklenir.
Yani keylerin tipi ayni olmak zorunda degil ama Immut. ve Uniq. Olmasi yeterli.

Touple bi keyle beraber string keyler kullanabiliriz, mesela:

```py
{ "key1":"value1", "key2":2, "key3":[3,3,3], ("Ouuu", "Bu bi touple keyi"):("Touple valuesu") }
Dict1[ "key1" ]  cagirirsan "value1" donecek.
```

{ } Sunlarla olusturduk

```py
Dict1 = {  biseyler:biseyler }
```

Eklemek icin olmayan bi degeri set et direkt.

```py
Dict1["za"] = "xd"
```

```py
del( Dict1[ "silinenKey" ] ) # ile degeri sildik

"Aranan Deger" in Dict1      # ile arama yaptik. 
# False donecek olmadigi icin, bool donuyor.

Dict1.keys( )   # cagirirsan keyler donecek, liste olarak
Dict1.values( ) # ile valuelari getirdik liste olarak
```

Ayni keyi iki kere kullanirsan:

```py
dic1 = { "key1":"a", "key1":"b" }
"key1":"b" # dondurur
```

## Sets

**Sirasiz, unique** elementler koleksyonu / KUMELER 

```py
Set1 = { "element" , "BaskaElement", 4 }
```

```py
set( list ) seklinde bi typeCast metodu da var.
List alip set cikariyor
```

```py
Set1.add ( "element" ) ile ekleme
Set1.remove ( "element" ) ile silme
"Aranan Deger" in Set1  ==  False donecek, in var yine Dict. gibi
```

Kumelerin kesisen degerini cekmek icin filan hep operatorler var.

- & Kesisen degerleri getirir. Set1 & Set2 yaparak ortak olan elementleri cektin.
- Kesisim icin ayrica Set1.intersection( Set2 ) de diyebilirdik
- Set1.union( Set2 ) diyerek de union yaptik, tum elemanlar geldi.
- Set1.difference( Set2 ) diyerek 1'de olup 2'de olmayanlari gorduk
- Set3.issubset( Set1 ) demek, Set3, Set1'in Subset'i mi diye bakiyor, bool return.
- Set3.issuperset( Set1 ) diyerek de, tam tersi iliskiyi kontrol.

Variable olusturmaya da gerek yok tabi, pratik iki ornek:

```py
set({ "A", "b" }).issubset( Set1 )
Set1.issuperset({ "Back in Black", "AC/DC" })
```

## Conditioning

Bool donen operatorlerimiz var.

```py
== equals kontrol eder
>   buyuktur   |||   >=  buyuk esittir
<   kucuktur   |||   <=   kucuk esittir
```

Char ve stringlerde ascii degere gore comparison var.

```py
'B' > 'A'  dir mesela.
'BA' > 'AB'  dir ayrica, ilkin onceligi var.
# (Ascii kodlari case sensitive)
```

```py
!=  esit degil

if (  condition  ) :
    Statement
elif (  other condition  ) :
    Other Statement
else :
    Otherest Statement
Continues
```

if indent'leri genelde 4 space (compiler based)

## Logic Operators

Bool alip bool donerler

```py
not( someBool ) # returns Bool'un Tersi
```

**or** 

```py
if( biseyler ) or ( baska seyler ):
    Bambaska seyler
```

**and**

```py
if( biseyler ) and ( baska seyler):
    Super seyler
```

Parantez sart degil.

```py
if biseyler or baskaSeyler or bambaskaSeyler:
    Statementz
```

## Loops

**range ( N )** metodu, (N pozitifse),
0'dan N'e kadar **range objesi** donuyor.

```py
range(3) = [0,1,2]
```

range( S, E ) Start S, End E arasi sequence

```py
range(10,13) = [10,11,12]
```

```py
for i in range( 0, 5 ) :
    array[i] = bisey
```

! Indent'e dikkat

loop'a range fonksyonu haricinde direkt List filan da verebilirsin

```py
for square in squares:
    Statements
```

Hem itemleri hem de indexlerini tutarak loop edebilirsin,

```py
for i, item in  enumerate ( squares ):
    print( i +"th element is: " + item )
```

**while** icin:

```py
i = 0
while ( array[i] > 5 and i<len(array) ):
    array.append(biseyler)
    i = i + 1  # i += 1 de olur
```

While'a **i < len(a)** ekledik, eklemezsek array out of bounds olana kadar dolasabilir

## Functions

Input alip output veren unsurlardir.

```py
def functionName(inputs):
    """ Documentation """
    # someTasks;
    return value;
```

Bazi tanimli fonksyonlar

```py
len(x)      ## x'in uzunlugunu getirir
sum(x)      ## iterable bir x'in degerlerini toplar
sorted(x)   ## Listeyi veya tuple'in sirali versiyonunu doner. 
            ## Orijinale bisey olmuyor.
sort(x)     ## mevcut listeyi siralar, degistirir
help(func)  ## func metodunun documentationunu getirir
```

Su referanstan bakilabilir bazi onemli olanlara:
[Python Onemli Metotlar](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%203/Python_reference_sheet.pdf?utm_term=10006555)

Type belirtilmedigi icin, overloada gerek olmuyor.

```py
def func(x,y):
    c = x * y
    return c

func(2,"string ")   : "string string "
func(3,5.6)         : 16.8
func(2,3)           : 6
```
**pass** keywordu metodlari return value olmadan gecebilmeni saglar. Aslinda **None** objesi donuyor.

```py
def func():
    pass

print(func()) : None
```

**Collecting Arguments**

Inputa kac sayida arguman gelecegini kestiremiyorsun, **\*** atiyosun basa. Metod onlari tuple'a ekliyor.

```py
def func(*names):
    for name in names:
        print(name)
```

Cift yildiz atarak, Tuple yerine **Dictionary** icine de toplayabiliriz. Ornekte inputun nasil verildigine dikkat!

```py
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
# OUTPUT:
# Country : Canada
# Province : Ontario
# City : Toronto
```

Key:Value seklinde ( **:** ) isaretiyle verince calismiyor.

**Scope** 

Scope isleri gecerli halen. Metodda tanimladigin degeri baska yerde cagiramazsin.

Metodun disinda tanimladigin degeri metodda cagirabilirsin! Static gibi. Ama ayni isimde baska bisey tanimlamayacaksin local variable olarak.

Local variable'larin baslarina **global** yazarak, metodlarin disindan da erisilebilir olmalarini saglayabiliriz.

```py
def func()
    global z
    z = "deger"
    return z

func()      # Cagirdik ki o bloga girip olustursun
print(z)    # func'u cagirmasaydik gormezdi. 
```

**Default Arguements**

```py
def func(x=5):
    return x*x

print(func()) # returns 25
```

Tanimli referansi silmek icin

```py
del referans
```

Metoda input olarak gelen objeyi **dogrudan degistirebiliriz**. Ekstra anotasyonlara gerek olmuyor.