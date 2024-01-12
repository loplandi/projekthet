from ipari_forradalom import IpariForradalom

# Quiz létrehozása
def ipari_forradalom_quiz(forradalom):
    print("Ipari Forradalom Quiz")
    print("---------------------")
    print("Kérdés:")
    print(f"Mikor kezdődött az {forradalom.evszam} ipari forradalom?")
    print("A) 1600-as évek\nB) 1700-as évek\nC) 1800-as évek\nD) 1900-as évek")
    valasz = input("Válasz (A/B/C/D): ")

    if valasz.upper() == "C":
        print("Helyes válasz! Gratulálok!")
    else:
        print(f"Sajnálom, rossz válasz. Az ipari forradalom {forradalom.evszam}-től kezdődött.")

    print()
    print("További információk:")
    forradalom.bemutatkozas()

# További kérdések
def tovabbi_kerdesek(forradalom):
    print("\nTovábbi kérdések:")
    print("1. Mi volt az ipari forradalom fő oka?")
    print("A) Földművelés fejlődése\nB) Tudomány és technológia előrelépése\nC) Politikai változások\nD) Vallási események")
    valasz = input("Válasz (A/B/C/D): ")
    print("Helyes válasz! Az ipari forradalom fő oka a tudomány és technológia előrelépése volt.")

    print("\n2. Melyik ipari forradalom hozta el az összeszerelősorokat?")
    print("A) Első ipari forradalom\nB) Második ipari forradalom\nC) Harmadik ipari forradalom\nD) Negyedik ipari forradalom")
    valasz = input("Válasz (A/B/C/D): ")
    print("Helyes válasz! A második ipari forradalom hozta el az összeszerelősorokat.")

    print("\n3. Ki volt az ipari forradalom során a gőzgép feltalálója?")
    print("A) Thomas Edison\nB) James Watt\nC) Nikola Tesla\nD) Alexander Graham Bell")
    valasz = input("Válasz (A/B/C/D): ")
    print("Helyes válasz! James Watt volt a gőzgép feltalálója.")

    print("\n4. Mely ipari forradalom volt az elektromosság térhódításának ideje?")
    print("A) Első ipari forradalom\nB) Második ipari forradalom\nC) Harmadik ipari forradalom\nD) Negyedik ipari forradalom")
    valasz = input("Válasz (A/B/C/D): ")
    print("Helyes válasz! A második ipari forradalom idején terjedt el az elektromosság.")

    print("\n5. Melyik város volt az egyik központja az ipari forradalomnak?")
    print("A) Manchester\nB) Birmingham\nC) London\nD) Liverpool")
    valasz = input("Válasz (A/B/C/D): ")
    if valasz.upper() == "B":
        print(f"Helyes válasz! {forradalom.varos} az ipari forradalom egyik központja volt.")
    else:
        print(f"Sajnálom, rossz válasz. Az ipari forradalom egyik központja volt {forradalom.varos}.")


