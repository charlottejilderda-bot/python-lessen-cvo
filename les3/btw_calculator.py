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

print("-" * 45)
print(f"Bedrag excl. BTW: €{bedrag:.4f}")
print(f"BTW ({tarief}%)   :€{btw_bedrag:.2f}")
print(f"Totaal incl. BTW: €{totaal:.2f}")
print("=" * 45)
