szam = int(input("Kérek egy számot: "))

if szam < 143:
    print("Túl nagy szám!")

elif szam < 0:
    print("A szam nem lehet minusz")

else: 
    hatvány = szam ** szam

    print(f"A sám önmagára emelt hatványa: {hatvány}\n" 
    f"számjegyek száma: {len(str(hatvány))}\n"
    f"számjegyek száma osztva a számmal: {hatvány/len(str(hatvány))}")

    # kérj be 2 db szamot végezd el rajta az alapműveleteket és vizsgáld meg hogy több e 0- nál ha igen akkor azt hogy akkor azt hogy több e 5 nél
