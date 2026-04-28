def hlavni_menu():
    ukoly = []  # seznam úkolů
    # hlavní smyčka programu - běží dokud uživatel nezvolí konec
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            while True:
                nazev = input("\nZadejte název úkolu: ").strip()
                if not nazev:
                    print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
                    continue
                break
            while True:
                popis = input("Zadejte popis úkolu: ").strip()
                if not popis:
                    print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
                    continue
                break
            ukoly = pridat_ukol(ukoly, nazev, popis)
        elif volba == "2":
            ukoly = zobrazit_ukoly(ukoly)
        elif volba == "3":
            if not ukoly:
                print("\nSeznam úkolů je prázdný, není co odstranit.")
            else:
                zobrazit_ukoly(ukoly)
                while True:
                    vstup = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()
                    try:
                        cislo = int(vstup)
                    except ValueError:
                        print("Neplatný vstup. Zadejte celé číslo.")
                        continue
                    if 1 <= cislo <= len(ukoly):
                        ukoly = odstranit_ukol(ukoly, cislo)
                        break
                    else:
                        print(f"Neplatné číslo. Zadejte číslo od 1 do {len(ukoly)}.")
        elif volba == "4":
            print("\nKonec programu.")
            break  # ukončí hlavní smyčku a program skončí
        else:
            print("\nNeplatná volba. Zadejte číslo od 1 do 4.")


def pridat_ukol(ukoly, nazev, popis):
    ukoly.append({"nazev": nazev, "popis": popis})  # přidej úkol do seznamu
    print(f"Úkol '{nazev}' byl přidán.")
    return ukoly


def zobrazit_ukoly(ukoly):
    if not ukoly:  # seznam je prázdný
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):  # číslování od 1
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    print()
    return ukoly


def odstranit_ukol(ukoly, cislo):
    odstranen = ukoly.pop(cislo - 1)  # odstraň úkol (index je o 1 menší)
    print(f"Úkol '{odstranen['nazev']}' byl odstraněn.")
    return ukoly


if __name__ == "__main__":
    hlavni_menu()  # spustí program pouze při přímém spuštění souboru
