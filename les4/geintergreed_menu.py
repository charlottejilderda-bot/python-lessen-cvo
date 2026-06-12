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
        import btw_calculator.py         
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