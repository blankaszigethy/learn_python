# Coctail Components

## I. Terminal feladatok
- Hozz létre egy coctail mappát a lokális repository-nkon belül (mkdir)
- Helyezd át a coctailmaker.py -t ebbe a mappába (mv)
- GIT-eld el a változtatásokat (git add, git commit, git pudh)

## II. Tömb iterációs feladatok

### Fájl létrehozása
- Hozz lére egy components.py fájlt az előző feladatban létrehozott coctail mappánkba (touch) (ebbe a fájlba fogunk dolgozni)

### COMPONENTS konstans
- Írj egy COMPONENTS konstanst, amelynek értéke egy tömb, amely string-eket tárol. A tárolt string-ek a következők legyenek:
  - wines
  - gins
  - soft_drinks

### Borok
- Hozz létre egy WINES konstans, amelynek értéke egy tömb, amely string-eket tárol. A tárolt stringek borok legyenek.
- Írj függvényt print_wines néven, amely egy while ciklus segítségével végigiterál (végighalad) a WINES tömb elemein és kiírja őket

### Ginek
- Hozz létre egy GINS konstans, amelynek értéke egy tömb, amely string-eket tárol. A tárolt stringek gin-ek legyenek.
- Írj függvényt print_gins néven, amely egy while ciklus segítségével végigiterál (végighalad) a GINS tömb elemein és kiírja őket
 
### Üdítők
- Hozz létre egy soft_drinks konstans, amelynek értéke egy tömb, amely string-eket tárol. A tárolt stringek üdítők legyenek.
- Írj függvényt print_soft_drinks néven, amely egy while ciklus segítségével végigiterál (végighalad) a SOFTDRNKS tömb elemein és kiírja őket

### Ellenörzés!
- Hívd meg mindhárom függvényt és próbáld ki, hívd meg!

## III. Alkomponens kiiratás
- Írj egy print_subcomponents függvényt, amelynek van egy bemeneti argumentuma, type néven
- A függvényt úgy írd meg, hogy ha azt az értéket kapja a type bemeneti argumentum-ban (string-ként), hogy
  - wines: akkor meghívja a print_wines függvényt
  - gins: akkor meghívja a print_gins függvényt
  - soft_drinks: akkor meghívja a print_soft_drinks függvényt
- Ez a gyakorlatban 3db if statement, melyeknek igaz kódblokkjaiban a fent írt függvényhívások állnak
  kondícióikban pedig a három string-et hasonlítjuk össze a type bemeneti argumentummal.
- Ha ezektől független értéket kap, ne csináljon semmit.

### Ellenörzés!
- A függvényt próbáld ki, hívd meg!

## IV. Összes komponens kiírása
- Írj egy print_all függvényt, mely a végigiterál (végighalad) a COMPONENTS tömb elemein egy while ciklus segítségével
- A ciklusmagjában két dolgot csináljon:
  - írja ki a tömb "i-edik" elemét, 2x3 egyenlőségjel között (példa: "=== Gins ===") (string interpolációt kell használni)
  - hívja meg a print_subcomponents függvényt és bemeneti argumentumáénak a tömb "i-edik" elemét adja meg.
- Az erdedmény egy lista kell hogy legyen, ahol mindhárom komponens típus listázódik és az "al-listék"
- elején egyenlőségjelek áéltal kijemelve láétszónak az allisták nevei is.
  - A függvényt próbáld ki, hívd meg!
 
## V. Zárás
- GIT-eld el a components.py-odat!
- Ha hosszabb időre otthagyod a feladatot, mindig GIT-elj!
