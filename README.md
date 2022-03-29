## Programozás alapjai 2.

### 1. Zárthelyi dolgozat pótlása

A feladat egy gépjármű üzemanyagfogyasztásának elemzését segítő osztályok elkészítése a [fuelstats.py](fuelstats.py) fájlban.

A fogyasztási adatok `Trip` objektumokban legyenek tárolva:
- Konstruktorban kerül megadásra a megtett út hossza km-ben és az üzemanyagfogyasztás literben.
- Legyen egy `lit_per_100k()` metódusa, ami kiszámolja és visszaadja, hogy ez 100 km-en hány liter fogyasztással egyenértékű.
- Az adatok könnyebb rendezésének érdekében legyen összehasonlítás operátora, ami a megtett út alapján hasonlít össze két objektumot.

A `FuelStats` osztály feladata a `Trip` objektumok kezelése:
- A konstruktorának megadott pickle fájlból tudja betölteni egy korábban exportált `FuelStats` objektum adatait.
- Ha a megadott fájl nem létezik, akkor üresen legyen inicializálva az objektum.
- Az `add(Trip)` metódussal lehessen új fogyasztási adatot hozzáadni.
- A `save()` metódus végezze az adatok exportálását a konstruktorban megadott fájl elérési útra.

- Az `average()` és a `median()` metódusok adják vissza az átlagos fogyasztást, illetve a `Trip` objektumok közül a mediánnak a fogyasztását, l/100km-ben.
  - A medián a fogyasztás szerinti rendezés utáni középső elem értéke, vagy páros darabszám esetén a két középső érték számtani közepe.

A `create_chart()` metódus az alább leírt módon készítsen grafikont az utazásokból, és azt mentse el egy fájlba:

- A grafikont az aktuális könyvtár `plots` alkönyvtárába tegye, ha nincs ilyen, hozza létre.
  - A fájlok itt `0.png`, `1.png`, `2.png`, `3.png`, ... elnevezésűek legyenek.
  - Ehhez nézze meg, mi a legnagyobb "sorszámú" fájl, és annál eggyel nagyobb legyen az aktuális fájl neve.
  - A könyvtárban lehetnek olyan fájlok is, amiknek a neve nem egy szám (nem konvertálható `int`té), ezeket hagyja figyelmen kívül.

- A grafikon X tengelye az utazások hossza, az Y tengelye a fogyasztás literben, ezek legyenek is kiírva a tengelyekre, valamint a grafikon tetején legyen egy cím.
  - Az egyes utazások értékei pontokként legyenek ábrázolva, és az átlagfogyasztás pedig egy egyenes, szaggatott vonalként kerüljön feltüntetésre.
  - Tipp: A vonal y-koordinátáit minden x értékre ki kell számítani. Vagyis hogy átlagos fogyasztást feltételezve mennyi lenne a fogyasztás az egyes távolságokra.
- Példa kimenet a megadott tesztadatokra:

![expected/0.png](expected/0.png)
![expected/1.png](expected/1.png)


A ZH során használható weboldalak:
* Órai kódok repository-ja: https://github.com/Uni-Sopron/progalap2-22t
* Saját házi feladat megoldások: https://github.com/Uni-Sopron?q=progalap-22t-hf
* Python Tutor: https://pythontutor.com/visualize.html
* Hivatalos Python dokumentáció: https://docs.python.org/3/library/index.html
* W3Schools: https://www.w3schools.com/python/
* Programiz: https://www.programiz.com/python-programming
