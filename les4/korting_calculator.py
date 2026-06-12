#korting_calculator.py - gemaakt door Charlotte

print("=" * 45)
print("Korting Checker - PrimabouwBV")
print("=" * 45)
totaalbedrag = float(input("Voer het totale orderbedrag in (€):"))

if totaalbedrag > 1000: 
    print("Hoera! Deze klant heeft recht op volumekorting.")
else:
    print("Status: Standaard tarief van toepassing (geen korting).")