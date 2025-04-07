# Darbas su „DataFrame“ (2–3 dienos)
import pandas as pd

df = pd.read_csv("duomenys.csv")

# Užduotis 1: Rask visus žmones, kurių amžius > 30
age = df[df["Amzius"] > 30]

# 2: Rask visas moteris, kurios gyvena Kaune
women = df[(df["Lytis"] == "M") & (df["Miestas"] == "Kaunas")]

# Užduotis 3: Rask žmones, kurių vardas baigiasi „a“
names_with_a = df[df["Vardas"].str.endswith("a")]

# Užduotis 4: Rask vyrus iš Vilniaus arba Šiaulių
men_city = df[(df["Lytis"] == "V") & (df["Miestas"].isin(["Vilnius", "Šiauliai"]))]

#  Rodo rezultata, kurie NERA Vilnius ir Siauliai
women_not_live_in_city = df[(df["Lytis"] == "M") & (~df["Miestas"].isin(["Vilnius", "Siauliai"]))]
#print(women_not_live_in_city)

# loc[], iloc[] taisykles
df = pd.DataFrame({
    "Name": ["Anna", "Jonas", "Tomas"],
    "Age": [28, 34, 22]
}, index=["a", "b", "c"])

df.loc["b", "Age"]  # Rezultatas: 34
df.iloc[1, 1]  # Rezultatas: 34. Tai reiškia: paimk antrą eilutę (pozicija 1) ir antrą stulpelį (pozicija 1).

df = pd.DataFrame({
    "Name": ["Anna", "Jonas", "Tomas", "Laura"],
    "Age": [28, 34, 22, 45],
    "City": ["Vilnius", "Kaunas", "Klaipėda", "Šiauliai"]
})

#Pasirink ir atspausdink antrą eilutę naudodamas iloc.
df.iloc[1]

#Pasirink ir atspausdink vardą iš pirmos eilutės naudodamas loc.
dp = df.loc[0, "Name"]

#Pasirink visus žmones iš Kauno.
#dp = df.loc[df["City"] == "Kaunas"]

# Atspausdink visus žmones, kurių amžius didesnis nei 30. 5. Visų, kurių miestas yra Vilnius, stulpelį „City“ pakeisk į "Sostinė". 6. Pakeisk „Tomas“ amžių į 25
dp = df.loc[df["Age"] > 30, "Name"]
pp = df.loc[df["City"] == "Vilnius", "City"] = "Sositne"
cc = df.loc[df["Name"] == "Tomas", "Age"] = 25

#  Atspausdink pirmas 2 eilutes ir tik stulpelius „Name“ ir „Age“. 8. Atspausdink paskutinio žmogaus duomenis naudodamas iloc.
ka = df.loc[0:1, ["Name", "Age"]]
s = df.iloc[-1]

# Atrink žmones, kurių vardas yra Jonas, Inga arba Eglė
names = df[df["Vardas"].isin(["Jonas", "Inga", "Eglė"])]
#print(names)

# prideti eilute Naudojant pd.concat()
new_row = pd.DataFrame([{"Vardas": "Andrius", "Amžius": 36, "Miestas": "Vilnius"}])
df = pd.concat([df, new_row], ignore_index = True)

# Duomenų rūšiavimas (sort_values())
df.sort_values(by="Amžius")
df.sort_values(by=['Miestas', 'Amžius'], ascending=[True, False])
df.groupby('Miestas')['Amžius'].mean()

import pandas as pd
data = {
    'Vardas': ['Jonas', 'Asta', 'Mantas', 'Rūta', 'Tomas'],
    'Miestas': ['Vilnius', 'Kaunas', 'Vilnius', 'Kaunas', 'Klaipėda'],
    'Amžius': [25, 30, 22, 30, 28],
    'Lytis': ['Vyras', 'Moteris', 'Vyras', 'Moteris', 'Vyras']
}

df = pd.DataFrame(data)
print(df.groupby('Miestas')['Amžius'].mean())

# Uzduotis su groupby()
import pandas as pd
data = {
    'Vardas': ['Jonas', 'Asta', 'Mantas', 'Rūta', 'Tomas', 'Laura', 'Jurgis'],
    'Skyrius': ['IT', 'Personalas', 'IT', 'Marketingas', 'IT', 'Marketingas', 'Personalas'],
    'Lytis': ['Vyras', 'Moteris', 'Vyras', 'Moteris', 'Vyras', 'Moteris', 'Vyras'],
    'Atlyginimas': [2500, 2200, 2700, 2100, 2600, 2300, 2400]
}

df = pd.DataFrame(data)

# Grupuok darbuotojus pagal skyrių ir suskaičiuok:
# kiek žmonių dirba kiekviename skyriuje (count)
print(df.groupby("Skyrius")["Vardas"].count())

# kiek vidutiniškai moka kiekvienam skyriui (mean atlyginimas)
print(df.groupby("Skyrius")["Atlyginimas"].mean())

# Grupuok pagal skyrių ir lytį, parodyk:
# vidutinį atlyginimą kiekviename skyriuje vyrams ir moterims
print(df.groupby(["Skyrius", "Lytis"])["Atlyginimas"].mean().unstack())

