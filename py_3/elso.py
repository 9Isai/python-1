szam = int(input("Kérek egy számot: "))

if szam % 2 == 0:
    print(f"Az eredmény: {szam / 2}")
    print("Ez a szám páros!")

else:
    print(f"Az eredmény: {szam / 2:. 2f}")
    print(f"maradék: {szam % 2}")
    print("Ez a szám páratlan")