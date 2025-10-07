samling = ["en ting", "ting to", 50]
print(samling)
print(samling[0])
samling.append(20)
print(samling)
print(samling[3])

tupleIListe = [("strength", 60), ("speed", 40)]
print("Første ferdighet er ", tupleIListe[1][1], "\n\n")


navneliste = ["Gandalf", ["Legolas", "Elrond"], "Gimli"]
for n in navneliste:
    print(n[1])

print(navneliste[1][1])


print("\n\n\n")

ferdigheterTilSalgs = [
    ["strength", 60], 
    ["speed", 40], 
    ["stamina", 40],
    ["reactions", 20]
]

for element in ferdigheterTilSalgs:
    print(element[0][1][0][0][0][0][0][0][0])

print("\n\n\n")

navn = "Frode"
print(navn[0][0])



print("\n\n\n")

enOrdbok = {
    "stein": 5,
    "kappe": 5,
    "stav": 786
}
print(enOrdbok.values())

for element in enOrdbok:
    print(enOrdbok[element])