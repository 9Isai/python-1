import random

kocsi_1 = random.randint(0, 200)
kocsi_2 = random.randint(0, 170)

print(f"Az első kocsi sebessége: {kocsi_1}")
print(f"A második kocsi sebessége: {kocsi_2}")

if kocsi_1 > kocsi_2:
    print("Az első kocsi nyert!")
elif kocsi_1 < kocsi_2:
    print("A második kocsi nyert!")
elif kocsi_1 ==  kocsi_2:
    print("Döntetlenül értek be!")