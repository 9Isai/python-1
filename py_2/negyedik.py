import math

a = int(input("Kérek egy számot: "))
b = int(input("Kérem a második számot: "))

hatvany = math.pow(a, b)
print(f"hatvány: {hatvany:.2f}")

gyok = math.sqrt(a)
print(f"gyok: {gyok}")
print(f"gyok kerekítve: {math.ceil (gyok)}")

print(f"Az (a) szám tipusa: {type:a}")
print(f"Az (b) szám tipusa: {type:b}")
print(f"Az hatvany tipusa: {type: hatvany}")
print(f"A gyok tipusa: {type: gyok}")








