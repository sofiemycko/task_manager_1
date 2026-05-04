from typing import List, Dict # pro verze Pythonu starší než 3.9

### Hlavní funkce - zpracování hlavního menu a volby uživatele
def hlavni_menu() -> None:
    """Spustí hlavní smyčku programu a zpracovává volby uživatele."""
    
    # Seznamu úkolů - každý úkol je reprezentován jako slovník s klíči "nazev" a "popis"
    ukoly: List[Dict[str, str]] = []  # seznam úkolů

    # hlavní smyčka programu - běží dokud uživatel nezvolí konec
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            ukoly = nacti_nazev_a_popis(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            ukoly = nacti_cislo_ukolu(ukoly)
        elif volba == "4":
            print("\nKonec programu.")
            break  # ukončí hlavní smyčku a program skončí
        else:
            print("\nNeplatná volba. Zadejte číslo od 1 do 4.")


### I/O funkce - načítání a zpracování vstupů od uživatele, zobrazování výstupů
def nacti_nazev_a_popis(ukoly: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Načte od uživatele název a popis úkolu, přidá úkol do seznamu a vrátí ho.

    Args:
        ukoly (list): Aktuální seznam úkolů.

    Returns:
        list: Aktualizovaný seznam úkolů.
    """
    # načítání názvu úkolu s kontrolou, že nejsou prázdné
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        break
    
    # načítání popisu úkolu s kontrolou, že nejsou prázdné
    while True:
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue
        break

    # přidání úkolu do seznamu
    return pridat_ukol(ukoly, nazev, popis)


def nacti_cislo_ukolu(ukoly: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Zobrazí seznam úkolů, načte od uživatele platné číslo úkolu a odstraní ho.

    Args:
        ukoly (list): Aktuální seznam úkolů.

    Returns:
        list: Aktualizovaný seznam úkolů.
    """
    # prazdný seznam - není co odstranit ani zobrazit
    if not ukoly:
        print("\nSeznam úkolů je prázdný, není co odstranit.")
        return ukoly
    
    # seznam není prázdný - zobrazí úkoly a načte číslo pro odstranění
    zobrazit_ukoly(ukoly)
    while True:
        vstup = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()
        
        # kontrola, že vstup není prázdný
        if not vstup:
            print("Vstup nesmí být prázdný. Zadejte celé číslo.")
            continue

        # kontrola, že vstup je celé číslo (bez desetinné části a bez písmen)
        try:
            cislo = int(vstup)
        except ValueError:
            print("Neplatný vstup. Zadejte celé číslo (bez desetinné části).")
            continue
        
        # kontrola, že číslo je kladné
        if cislo <= 0: 
            print("Číslo musí být kladné celé číslo.")
            continue
        
        # kontrola, že číslo odpovídá existujícímu úkolu
        if cislo > len(ukoly):
            print(f"Neplatné číslo. Zadejte číslo od 1 do {len(ukoly)}.")
            continue
        
        # všechny kontroly jsou v pořádku - můžeme odstranit úkol
        return odstranit_ukol(ukoly, cislo)

### Logické funkce - zpracování dat, přidávání, zobrazování a odstraňování úkolů
def pridat_ukol(ukoly: List[Dict[str, str]], nazev: str, popis: str) -> List[Dict[str, str]]:
    """Přidá nový úkol do seznamu úkolů.

    Args:
        ukoly (list): Aktuální seznam úkolů.
        nazev (str): Název úkolu.
        popis (str): Popis úkolu.

    Returns:
        list: Aktualizovaný seznam úkolů.
    """

    # kontrola, zda úkol s tímto názvem a popisem již existuje
    if any(u["nazev"] == nazev and u["popis"] == popis for u in ukoly):
        print(" ! POZOR: Úkol s tímto názvem a popisem již existuje.")
        # return ukoly  # pokud nechceme přidat duplicitní úkol, můžeme odkomentovat tuto řádku
    
    # přidání úkolu do seznamu
    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")
    return ukoly


def zobrazit_ukoly(ukoly: List[Dict[str, str]]) -> None:
    """Zobrazí seznam úkolů.
    Args:
        ukoly (list): Seznam úkolů k zobrazení.
    """
    if not ukoly:  # seznam je prázdný
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):  # číslování od 1
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    print()


def odstranit_ukol(ukoly: List[Dict[str, str]], cislo: int) -> List[Dict[str, str]]:
    """Odstraní úkol ze seznamu podle zadaného čísla.
    Args:
        ukoly (list): Aktuální seznam úkolů.
        cislo (int): Číslo úkolu k odstranění (číslování od 1).
    Returns:
        list: Aktualizovaný seznam úkolů.
    """
    odstranen = ukoly.pop(cislo - 1)  # odstraň úkol (index je o 1 menší)
    print(f"Úkol '{odstranen['nazev']}' byl odstraněn.")
    return ukoly


if __name__ == "__main__":
    hlavni_menu()  # spustí program pouze při přímém spuštění souboru
