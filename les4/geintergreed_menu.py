#geintegreed_menu.py - gemaakt door Charlotte

while True: 

    print("\n"+"=" * 45)
    print("HOOFDMENU ERPM-SYSTEEM PRIMABOUW")
    print("=" * 45)
    print("1)BTW_Calculator(Les 3)")
    print("2)BTW_Calculator(Les 4)")
    print("3)BTW_Calculator(Les 4)")
    print("4)Applicatie afsluiten")
    print("=" * 45)

    keuze = input("Maak uw keuze(1-4):")
    if keuze == "1":
        print("\n---[OPSTARTEN BTW_CALCULATOR]---")
        # btw_calculator.py - gemaakt door Charlotte Jilderda

        print("=" * 45)
        print(" BTW-Calculator -PrimaBouw BV")
        print("=" * 45)
        gebruiker = input("Jouw naam:")
        print("Welkom, " + gebruiker + "!")
        bedrag_str = input("Voer het bedrag in (excl. BTW, in €):")
        bedrag = float(bedrag_str)
        tarief_str = input("Welk BTW-tarief?(6, 12 of 21):")
        tarief = int(tarief_str)

        btw_bedrag = bedrag * (tarief/100)
        totaal = bedrag + btw_bedrag #242.00

        print("-" * 45)
        print(f"Bedrag excl. BTW: €{bedrag:.4f}")
        print(f"BTW ({tarief}%)   :€{btw_bedrag:.2f}")
        print(f"Totaal incl. BTW: €{totaal:.2f}")
        print("=" * 45)

        btw_pct_van_totaal = (btw_bedrag / totaal) * 100
        print(f"BTW als % van totaal: {btw_pct_van_totaal:.1f}%") #17.4%

        nog_een = input("\nWil je nog een berekening? (ja/nee):")
        if nog_een.lower() =="ja":
                print("Start het script opnieuw om een nieuwe berekening te doen.")
        else:
                print("Tot de volgende keer, " + gebruiker + "!")
        
    elif keuze == "2":
        print("\n---[OPSTARTEN KORTINGS_CALCULATOR]---")
        import korting_calculator.py    
    elif keuze == "3":
        print("\n---[OPSTARTEN WERF-VEILIGHEID]---")
        import werf_veiligheid.py   
    elif keuze == "4":
        print("\nBedankt voor het gebruiken van het PrimaBouw systeem. Tot ziens!")
        break #Dit breekt de 'while True' lus en stopt het programma 
    else:
        print("ongeldige keuze! Voer een cijfer van 1 tot en met 4 in.")