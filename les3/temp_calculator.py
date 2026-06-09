#temp_calculator.py - gemaakt door Charlotte 


print("=" * 40)
print(" Temperatuuromrekening F -> C")
print("=" * 40)

Farenheit = float(input("Voer temperatuur in (°F):"))
Celsius = (Farenheit - 32) / 1.8
print(f"{Farenheit}°F = {Celsius:.1f}°C")


