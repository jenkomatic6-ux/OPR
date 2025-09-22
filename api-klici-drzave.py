import requests
import pprint

url = "https://restcountries.com/v3.1/all?fields=name,borders,languages,population,continents"
odgovor = requests.get(url)
drzave = odgovor.json()

# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
max_sosedi=0
drzava_z_najvec_sosedi=""

for d in drzave:
    borders= d.get("borders", [])
    if len(borders) > max_sosedi:
        max_sosedi = len(borders)
        drzava_z_najvec_sosedi = d["name"]["common"]

print(f"Drzava z najvec sosedi je: {drzava_z_najvec_sosedi} ter ima {max_sosedi} sosedov.")

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
max_jezikov=0
drzava_z_najvec_jeziki=""

for d in drzave:
    languages= d.get("languages",[])
    if len(languages) > max_jezikov:
        max_jezikov = len(languages)
        drzava_z_najvec_jeziki = d["name"]["common"]
print("Država z največ jezikov:", drzava_z_najvec_jeziki, "število jezikov:", max_jezikov)

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0
celine={}
st_drzav={}

for d in drzave:
    pop= d.get("population",0)
    cont= d.get("continent", ["Unknown"])[0]

    celine[cont]= celine.get(cont,0) + pop
    st_drzav[cont] = st_drzav.get(cont,0) + 1

    for cont in celine:
        print(cont,"povprečna populacija: ", celine[cont] / st_drzav[cont])



# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.
