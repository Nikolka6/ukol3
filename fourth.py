def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    radek, sloupec = cilova_pozice
    aktualni_radek, aktualni_sloupec = aktualni_pozice

    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    rozdil_radku = abs(radek - aktualni_radek)
    rozdil_sloupcu = abs(sloupec - aktualni_sloupec)

    if typ == "král":
        return (rozdil_radku <= 1
            and rozdil_sloupcu <= 1
            and (rozdil_radku != 0 or rozdil_sloupcu != 0))

    elif typ == "jezdec":
        return ((rozdil_radku == 2 and rozdil_sloupcu == 1)
            or (rozdil_radku == 1 and rozdil_sloupcu == 2))

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))

    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice))