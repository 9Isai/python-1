# szükséges modulok meghívása
import random

# szereplők életereje konstansként eltárolva változóban
hős_hp = 100
ellenség_hp = 75

# ki mekkorát üt az adott körben, ehhez sorsolunk véletlen számot
hős_hit = random.randint(0, 200)
ellenség_hit = random.randint(0, 120)

# dobókockával dobunk és ezzel döntjük el ki üt
ütés = random.randint(1, 6)

if ütés == 1 or ütés == 3 or ütés == 5 or ütés == 6:
    print(f"Hős üt!\n"
          f"sebzés: {hős_hit}\n"
          f"ellenség életereje: {ellenség_hp - hős_hit}")
else:
    print(f"Ellenség üt!\n"
          f"sebzés: {ellenség_hit}\n"
          f"hős életereje: {hős_hp - ellenség_hit}")
    
if hős_hp > 0 and ellenség_hp < 0 and (ellenség_hp - hős_hit) <= 0 : 
    print(f"A hős még él!"
          f"A hős halott!")
else: 
    print(f"ellenség")

