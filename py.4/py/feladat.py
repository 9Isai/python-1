import random

játékos_1_dsz = random.randint(1, 6)
játékos_2_dsz = random.randint(1, 6)
    
print(f"Első játékos által dobott szám: {játékos_1_dsz}")
print(f"Második játékos által dobott szám: {játékos_2_dsz}")

if játékos_1_dsz > játékos_2_dsz:
    print("Első játékos nyert!")
elif játékos_1_dsz < játékos_2_dsz:
    print("Második játékos nyert!")
elif játékos_1_dsz == játékos_2_dsz:
    print("Döntetlen!")