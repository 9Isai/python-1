import random

véletlenszám = random.randint(-300, 300)
print(f"A sorsolt szám: {véletlenszám}")

if véletlenszám % 3 == 0: 
    print(f"A szám osztható 3-mal!\n"
          f"Eredmény: {véletlenszám / 3}")