#********************
# Karakteroppretting*
#********************
karakternavn = input("Hva skal karakteren hete? ")
gull = 100

ferdigheter = []

#********
# Butikk*
#********
print("Du kommer nå inn i en lurvete butikk og får følgende tilbud fra en småshady butikkeier:")
ferdigheterTilSalgs = [
    ["strength", 60], 
    ["speed", 40], 
    ["stamina", 40],
    ["reactions", 20]
]

for ferdighet in ferdigheterTilSalgs:
    valg = input("Ønsker du å kjøpe" + ferdighet[0] + "for" + 
                 str(ferdighet[1]) + " gull? (j/n) ")
    if (valg == "j" and ferdighet[1] <= gull):
        ferdigheter.append(ferdighet)
        gull -= ferdighet[1]
    elif(valg == "j" and ferdighet[1] > gull):
        print("Du har ikke råd til denne ferdigheten.")
    else:
        print("Du kjøpte ikke varen.")

print("Navnet på karakteren er", karakternavn)
print(karakternavn + " har " + str(gull) + " gull.")
for ferdighet in ferdigheter:
    print("Første ferdighet er", ferdighet[0], "som har verdi", ferdighet[1])