gelir = float(input("yıllık geliri girin: "))

if gelir <= 85528:
    vergi = gelir * 0.18 - 556.02
else:
    vergi = 14839.02 + 0.32 * (gelir - 85528)

if vergi < 0:
    vergi = 0.0

vergi = round(vergi, 0)
print("verginiz:", vergi, "thalerdir")
