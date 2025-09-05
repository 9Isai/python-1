elso_szam = int(input("Kérek egy számot"))
masodik_szam = int(input("Kérem a második számot: "))
harmadik_szam = int(input("Kérek egy harmadik számot: "))

egyenlet = elso_szam *masodik_szam / (harmadik_szam + elso_szam) - elso_szam / 45

print(f"Az egyenlet eredménye: {egyenlet:.2f}")