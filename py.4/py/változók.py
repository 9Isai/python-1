változó = int(input("Kérek egy adatot: "))

print(f"A változó tipusa: {type(változó)}")

if type(változó) == int or type(változó) == float:
    print("Ez egy egész szám!")
    print(f"Hatványra emelve: {változó ** 2}")
elif type(változó) == str:
    print("A művelet nem végezhető el!")