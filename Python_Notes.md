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

## Intro
Type öğrenme fonskyonu: **type()**

### Typecasting 

    float(1) : 1.0
    int(3.99) : 3  (asagi yuvarliyor fix)
    int('1') : 1

### Booleans 

Booleanların başı uppercase

**True / False**

    bool(0) = False

### Divisions

**/** = float division

**//** = integer division.

25 / 5 : 5.0

### Kullandigim metodlar:

    Print('string')

    sys.version (import sys lazim)

*#Comments*

sys.float_info  : float hakkinda teknik bilgiler

## Lists

Listelerde negative indexing var.
Son elemana 

    List[-1] // diyerek ulasabilirsin

Listelerde ayni type aranmaz.
Farkli type nesneler ayni listede durabilir

Tuple'lar: ('A', 2) mesela.
Listeye bunlar bile girebiliyor, nested listler de girebiliyor.

    liste[4:9] // dersen indexi 4 9 arasi degerleri slice eder (ilk dahil ikinci degil)

    .extend() // listeye eleman ekleme fonksyonu. 
    list.extend(  [ 1 , 'C' ]  )  : 2 eleman ekledik

O sondaki listeyi tek bi eleman olarak eklemek istiyorsan da:

    append  metodunu kullanacaksin. append( [array] ) yapaceksin.

Eleman degistirme:

    a[0] = 'Hoppp yeni deger';

Eleman silme:

    del(a[1])

## Strings

    string.split() // bize stringi KELIME KELIME split eder

Delimeter de alabilir tabi. split(,) dersin, virgule gore split eder

Referanslar javadaki gibi.
Ayni degeri gosteren referanslardan birini degistirirsen,
Diger referansin degeri de ayni seyi gosterdigi icin degisecek.

O yuzden, listeleri referanslarla degistirmek yerine klonlayabiliriz.

    B = A[:] diyorsun, hoppaa

Listeleri concat etmek (yazdirirken filan) icin + operatoru

    A = [ asdasd ]
    B = [ Ikincil Degerler ]
    A + B : [ adsasd, Ikincil Degerler ]

Tek tırnak veya cıft tırnak
Stringler array gibi kullanilabiliyor.

    String[0] = stringin ilk karakteri
    String[-1] = stringin son harfi. Dogal olarak, negatif index de gecerli 

    Array[::2] demek, her 2nin modu eleman demek.
    
    string = "Bir String" olsun
    string[::2} = [BrSrn] donecek

Sayi yazmadan : koymak = 0 yazmak.
**string[0:5:2]** olsaydi **= [BrS]**

**string[5:6]** dersen!!!
5\. indexe git, 6. indexe kadar al demek (sadece 5)

**6 uzunlukta bisey al degil!** *(Tekrar baktim ve onayliyorum)*

    len(string) // uzunlugu verir

Concat, arraylardeki gibi **( + )** operatoru ile yapilir.

Stringleri Carpip Multiple edebiliriz.
    
    String * 3 = "Bir StringBir StringBir String" olurdu

Stringler immutable, java gibi.

    String[0] = "C" // diyemezsin

Onun yerine referansi yeni bi stringe point et

Escape Character: **\\**

- \n = new line
- \t = tab
- \\\ = backslash

    text = r"\nayir \nolamaz"    
    print(text) : "\nayir \nolamaz"

Bu bastaki **r**, escape'leri onluyor

### Bazi string metodlari:

    string.upper() = uppercase halini dondurur
    string.replace("Degisecek kelime", "yeni kelime");
    string.find("sub") = stringin icinde "sub" kelimesi kacinci indexte basliyor. 
                        Yoksa -1

## Tuples:

Sirali dizilerdir.
*(1,5,4,6,10,9)* boyle olur mesela. Sayilarin sirali olmasi sart degil

Bi tuple'da farkli typelar olabilir.
Ama tuple'in kendi type'i var **(tuple)**

Yine indexlerle erisim.

    Tuple[0] = ilk eleman. Negatif index de var yine

Concat yine **+** ile.
Slice yine var **tuple[1:3]** gibi.
**len()** de var
append ve extend **yok**!

    sorted(tuple) ile sortlayabiliriz

Stringdeki find() yerine burada **.index( item )** var

**TUPLE'LAR IMMUTABLE**.
Listler degil.
Degistirilemedigi icin,
Ayni seyi gosteren iki referanstan biri degisirse,
Digeri **degismiyor**.
String de boyle immutabledir.

    bisey = sorted( tuple ) ile sortlayabiliriz

Ama dondurulen type List olur! 
**[1,2,3]** olur elinde.

## List 

anam babam array.
Koseli parantez reis:

    [0:5]

**+** operatoru liste concat eder.

Listeler **mutable** olduğundan ilk elemanı son elemanı vs. Değiştirebiliriz.

    del(index) yaparak silebiliriz listeden.

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

    { "key1":"value1", "key2":2, "key3":[3,3,3], ("Ouuu", "Bu bi touple keyi"):("Touple valuesu") }
    Dict1[ "key1" ]  cagirirsan "value1" donecek.

{ } Sunlarla olusturduk

    Dict1 = {  biseyler:biseyler }

Eklemek icin olmayan bi degeri set et direkt.

    Dict1["za"] = "xd"

    del( Dict1[ "silinenKey" ] ) // ile degeri sildik

    "Aranan Deger" in Dict1 // ile arama yaptik. 
    // False donecek olmadigi icin, bool donuyor.

    Dict1.keys( ) // cagirirsan keyler donecek, liste olarak
    Dict1.values( ) // ile valuelari getirdik liste olarak

Ayni keyi iki kere kullanirsan:

    dic1 = { "key1":"a", "key1":"b" }
    "key1":"b"  dondurur

## Sets

**Sirasiz, unique** elementler koleksyonu / KUMELER 

    Set1 = { "element" , "BaskaElement", 4 }

    set( list ) seklinde bi typeCast metodu da var.
    Liste alip set cikariyor

    Set1.add ( "element" ) ile ekleme
    Set1.remove ( "element" ) ile silme
    "Aranan Deger" in Set1  ==  False donecek, in var yine Dict. gibi

Kumelerin kesisen degerini cekmek icin filan hep operatorler var.

- & Kesisen degerleri getirir. Set1 & Set2 yaparak ortak olan elementleri cektin.
- Kesisim icin ayrica Set1.intersection( Set2 ) de diyebilirdik
- Set1.union( Set2 ) diyerek de union yaptik, tum elemanlar geldi.
- Set1.difference( Set2 ) diyerek 1'de olup 2'de olmayanlari gorduk
- Set3.issubset( Set1 ) demek, Set3, Set1'in Subset'i mi diye bakiyor, bool return.
- Set3.issuperset( Set1 ) diyerek de, tam tersi iliskiyi kontrol.

Variable olusturmaya da gerek yok tabi, pratik iki ornek:

    set({ "A", "b" }).issubset( Set1 )
    Set1.issuperset({ "Back in Black", "AC/DC" })

## Conditioning

Bool donen operatorlerimiz var.

    == equals'i kontrol eder
    >   buyuktur   |||   >=  buyuk esittir
    <   kucuktur   |||   <=   kucuk esittir

Char ve stringlerde ascii degere gore comparison var.

    'B' > 'A'  dir mesela.
    'BA' > 'AB'  dir ayrica, ilkin onceligi var.
(Ascii kodlari case sensitive)

    !=  esit degil

    if (  condition  ) :
        Statement
    elif (  other condition  ) :
        Other Statement
    else :
        Otherest Statement
    Continues

if indent'leri genelde 4 space (compiler based)

## Logic Operators

Bool alip bool donerler

    not( someBool )  returns Bool'un Tersi

**or** 

    if( biseyler ) or ( baska seyler ):
    	Bambaska seyler

**and**

    if( biseyler ) and ( baska seyler):
    	Super seyler
	
Parantez sart degil.

    if biseyler or baskaSeyler or bambaskaSeyler:
        Statementz

## Loops

**range ( N )** metodu, (N pozitifse),
	0'dan N'e kadar **range objesi** donuyor.

    range(3) = [0,1,2]

range( S, E ) Start S, End E arasi sequence

    range(10,13) = [10,11,12]

    for i in range( 0, 5 ) :
    	array[i] = bisey
! Indent'e dikkat

loop'a range fonksyonu haricinde direkt List filan da verebilirsin

    for square in squares:
    	Statements

Hem itemleri hem de indexlerini tutarak loop edebilirsin,

    for i, item in  enumerate ( squares ):
    	print( i +"th element is: " + item )
	
**while** icin:

    i = 0
    while ( array[i] > 5 and i<len(array) ):
	    array.append(biseyler)
	    i = i + 1   // i += 1 de olur
	
While'a **i < len(a)** ekledik, eklemezsek array out of bounds olana kadar dolasabilir

## Functions

