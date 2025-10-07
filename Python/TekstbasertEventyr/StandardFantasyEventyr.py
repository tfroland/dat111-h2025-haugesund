#********************
# Karakteroppretting*
#********************
karakternavn = input("Hva skal karakteren hete? ")
gull = 100

ferdighet1 = "ingenting"
ferdighet1verdi = 0
ferdighet2 = "ingenting"
ferdighet2verdi = 0
ferdighet3 = "ingenting"
ferdighet3verdi = 0

#********
# Butikk*
#********
print("Du kommer nå inn i en lurvete butikk og får følgende tilbud fra en småshady butikkeier:")
strength = 60
speed = 40
stamina = 40
reactions = 20

valg1 = input("Ønsker du å kjøpe strength for 60 gull? (j/n) ")
if (valg1 == "j" and strength <= gull):
    ferdighet1 = "strength"
    ferdighet1verdi = strength
    gull -= 60
elif(valg1 == "j" and strength > gull):
    print("Du har ikke råd til denne ferdigheten.")
else:
    print("Du kjøpte ikke varen.")

valg2 = input("Ønsker du å kjøpe speed for 40 gull? (j/n) ")
if (valg2 == "j" and speed <= gull):
    ferdighet2 = "speed"
    ferdighet2verdi = speed
    gull -= 40
elif(valg2 == "j" and speed > gull):
    print("Du har ikke råd til denne ferdigheten.")
else:
    print("Du kjøpte ikke varen.")

print("Navnet på karakteren er", karakternavn)
print(karakternavn + " har " + str(gull) + " gull.")
print("Første ferdighet er", ferdighet1, "som har verdi", ferdighet1verdi)
print("Andre ferdighet er", ferdighet2, "som har verdi", ferdighet2verdi)