# latihan konvensi satuan temprature

# program konvensi celcius ke satuan lain
print("\nPROGRAM KONVENSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah ",celcius, "celcius")

# reamur (4/5)C
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit ",fahrenheit, "fahrenhait")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin",kelvin, "kelvin")
