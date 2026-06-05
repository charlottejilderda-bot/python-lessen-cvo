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
totaal = bedrag + btw_bedrag