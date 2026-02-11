"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

labdarugok = []
with open('beolvasando_adatok/labdarugok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        labdarugo = {
            'nev': adatok[0],
            'csapat': adatok[1],
            'golszam': int(adatok[2]),
            'merkozesek_szama': int(adatok[3])
        }
        labdarugok.append(labdarugo)

print(f'{labdarugok=}')

jatekosok_szama = len(labdarugok)

legkevesebb = labdarugok[0]
for labdarugo in labdarugok:
    if labdarugo['golszam'] < legkevesebb['golszam']:
        legkevesebb = labdarugo

legtobb = labdarugok[0]
for labdarugo in labdarugok:
    if labdarugo['golszam'] > legtobb['golszam']:
        legtobb = labdarugo

legtobb_merkozes = labdarugok[0]
for labdarugo in labdarugok:
    if labdarugo['merkozesek_szama'] > legtobb_merkozes['merkozesek_szama']:
        legtobb_merkozes = labdarugo

osszes_gol = 0
for labdarugo in labdarugok:
    osszes_gol += labdarugo['golszam']

atlag = osszes_gol / len(labdarugok)


print(f"A beolvasott fájlban összesen {jatekosok_szama} játékos szerepel.")
print(f"A legkevesebb gólt szerző játékos: {legkevesebb['nev']} ({legkevesebb['golszam']} gól)")
print(f"A legtöbb gólt szerző játékos: {legtobb['nev']} ({legtobb['golszam']} gól)")
print(f"A legtöbb mérkőzést játszó játékos: {legtobb_merkozes['nev']} ({legtobb_merkozes['merkozesek_szama']} meccs)")
print(f"Az átlagos gólszám: {atlag}")
print(f"A legtöbb gólt szerző csapat:____")