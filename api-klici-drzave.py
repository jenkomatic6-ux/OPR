import requests
import pprint

url = "https://restcountries.com/v3.1/all?fields=name"
odgovor = requests.get(url)
drzave = odgovor.json()

# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
max_sosedi = 0
drzava_z_najvec_sosedi = None
dr=[]
for d in drzave[:5]:
    dr.append(d.get("name").get("official"))
print(dr)

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
max_jezikov = 0
drzava_z_najvec_jezikov = None
for d in drzave[:5]:
    if (stevilo_jezikov := len(d.get("languages", {}))) > max_jezikov:
        max_jezikov, drzava_z_najvec_jezikov = stevilo_jezikov, d["name"]["official"]

print(drzava_z_najvec_jezikov)
 

# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0

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
