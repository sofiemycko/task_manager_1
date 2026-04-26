ukoly = []  # globální seznam pro ukládání úkolů


def hlavni_menu():
    # hlavní smyčka programu - běží dokud uživatel nezvolí konec
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.")
            break  # ukončí hlavní smyčku a program skončí
        else:
            print("\nNeplatná volba. Zadejte číslo od 1 do 4.")


def pridat_ukol():
    # opakuj dokud uživatel nezadá neprázdný název
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        break

    # opakuj dokud uživatel nezadá neprázdný popis
    while True:
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        break

    ukoly.append({"nazev": nazev, "popis": popis})  # přidej úkol do seznamu
    print(f"Úkol '{nazev}' byl přidán.")


def zobrazit_ukoly():
    if not ukoly:  # seznam je prázdný
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):  # číslování od 1
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    print()


def odstranit_ukol():
    if not ukoly:  # nelze odstranit z prázdného seznamu
        print("\nSeznam úkolů je prázdný, není co odstranit.")
        return

    zobrazit_ukoly()  # zobraz úkoly, aby uživatel věděl jaké číslo zadat

    # opakuj dokud uživatel nezadá platné číslo úkolu
    while True:
        vstup = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()
        try:
            cislo = int(vstup)  # převeď vstup na celé číslo
        except ValueError:
            print("Neplatný vstup. Zadejte celé číslo.")
            continue

        if 1 <= cislo <= len(ukoly):  # číslo je v platném rozsahu
            odstranen = ukoly.pop(cislo - 1)  # odstraň úkol (index je o 1 menší)
            print(f"Úkol '{odstranen['nazev']}' byl odstraněn.")
            break
        else:
            print(f"Neplatné číslo. Zadejte číslo od 1 do {len(ukoly)}.")


if __name__ == "__main__":
    hlavni_menu()  # spustí program pouze při přímém spuštění souboru
