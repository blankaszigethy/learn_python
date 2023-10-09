# Cocktail Maker

- Hozz létre egy cocktailmaker.py fájlt a git repository-d gyökrébe. Ebbe a fájlba fogunk dolgozni.
- Hozz létre egy COCKAILS konstanst (úgy kell, mint a változót, csak csupa nagybetű a neve) melynek értéke egy tömb (list)
- Töltsd fel a tömböt objektumokkal (dictionary), minimum 5 darabbal. Minden dictionary-nek a következő kulcsai legyenek meg:
    - name (a koktél neve, string)
    - components (hozzávalók, az értéke egy tömb, melyben stringekkén szerepelnek a hozzávalók)
    - contains_alcohol (logikai érték, amely megmondja, alkoholos koktél-e)
- Írj függvényt header néven, melynek nincsenek bemeneti argumentumai a visszatérési értéke pedig egy string, mely egy üdvözlő üzenetet tartalmaz: "Python Coctail Maker"
- Hozz létre egy main nevű függvényt, mely meghívja a header függvényt és a visszatérési értékét beletölti egy header_text változóba, majd ezt a változót ki-print-eli.
- hozz létre egy print_coctails nevű függvényt, mely egy while ciklussal végighalad a COCTAILS tömb elemein és kiírja a koktélok adatlapját a következő példa szerint:


```
Name: Sex on the Beach
Components:
- vodka
- peach liqueur
- orange juice
- cranberry juice
Alcoholic: Yes
```

- Az egyes sorok legyenek küldön print-ek, string interpolációval behelyezve a COCTAILS i-edik elemének adott kulcsaihoz tartozó értékeket.
- Az Alcoholic kiírásához egy if-re lesz szükséged, ami a COCTAILS i-edik elemének alcoholic kulcsának értéke szerint írja ki, van-e alkohol tartalma az italnak, vagy sem.
- Hívd meg a main függvényben a print_coctails függvényt.
- GIT-eld el a coctailmaker.py-t "add coctailmaker.py" commit message-dzsel és push-old fel a github-ra.