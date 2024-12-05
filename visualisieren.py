import matplotlib.pyplot as plt

# Ausgangssituation
produkt_standard = 7.99 * 160
produkt_standard_advanced = produkt_standard + 9.99 * 130
produkt_standard_advanced_premium = produkt_standard_advanced + 12.99 * 110
kosten = 2000

# Nachfragewerte
nachfrage_standard = 160
nachfrage_standard_advanced = 160 + 130
nachfrage_standard_advanced_premium = nachfrage_standard_advanced + 110

# X-Achse: Nachfrage
nachfrage = [nachfrage_standard, nachfrage_standard_advanced, nachfrage_standard_advanced_premium]
# Y-Achse: Umsatz
umsatz = [produkt_standard, produkt_standard_advanced, produkt_standard_advanced_premium]




#Szenario:Eine weitere Version anbieten
#produkt_standard = 7.99 * 160
#produkt_standard_advanced = produkt_standard + 9.99 * 130
#produkt_standard_advanced_premium = produkt_standard_advanced + 12.99 * 110
#produkt_standard_advanced_premium_superpremium = produkt_standard_advanced_premium + 15.99*45
#kosten = 2250

# Nachfragewerte
#nachfrage_standard = 160
#nachfrage_standard_advanced = 160 + 130
#nachfrage_standard_advanced_premium = nachfrage_standard_advanced + 110
#nachfrage_standard_advanced_premium_superpremium = nachfrage_standard_advanced_premium + 45
# X-Achse: Nachfrage
#nachfrage = [nachfrage_standard, nachfrage_standard_advanced, nachfrage_standard_advanced_premium, nachfrage_standard_advanced_premium_superpremium]
# Y-Achse: Umsatz
#umsatz = [produkt_standard, produkt_standard_advanced, produkt_standard_advanced_premium, produkt_standard_advanced_premium_superpremium]




#Szenario:Freemium
#produkt_standard = 7.99 * 176
#produkt_standard_advanced = produkt_standard + 9.99 * 143
#produkt_standard_advanced_premium = produkt_standard_advanced + 12.99 * 121
#produkt_standard_advanced_premium_freemium = produkt_standard_advanced_premium + 0*500
#kosten = 2100

# Nachfragewerte
#nachfrage_standard = 160
#nachfrage_standard_advanced = nachfrage_standard + 130
#nachfrage_standard_advanced_premium = nachfrage_standard_advanced + 110
#nachfrage_standard_advanced_premium_freemium = nachfrage_standard_advanced_premium + 500
# X-Achse: Nachfrage
#nachfrage = [nachfrage_standard, nachfrage_standard_advanced, nachfrage_standard_advanced_premium, nachfrage_standard_advanced_premium_freemium]
# Y-Achse: Umsatz
#umsatz = [produkt_standard, produkt_standard_advanced, produkt_standard_advanced_premium, produkt_standard_advanced_premium_freemium]





#Szenario: Kombination aller drei Szenarien
#produkt_standard = 7.99 * 176
#produkt_standard_advanced = produkt_standard + 9.99 * 143
#produkt_standard_advanced_premium = produkt_standard_advanced + 12.99 * 121
#produkt_standard_advanced_premium_superpremium = produkt_standard_advanced_premium + 15.99* 45
#produkt_standard_advanced_premium_superpremium_freemium = produkt_standard_advanced_premium_superpremium + 0*500
#kosten = 2350

# Nachfragewerte
#nachfrage_standard = 160
#nachfrage_standard_advanced = nachfrage_standard + 130
#nachfrage_standard_advanced_premium = nachfrage_standard_advanced + 110
#nachfrage_standard_advanced_premium_superpremium = nachfrage_standard_advanced_premium + 45
#nachfrage_standard_advanced_premium_superpremium_freemium = nachfrage_standard_advanced_premium_superpremium + 500
# X-Achse: Nachfrage
#nachfrage = [nachfrage_standard, nachfrage_standard_advanced, nachfrage_standard_advanced_premium,nachfrage_standard_advanced_premium_superpremium, nachfrage_standard_advanced_premium_superpremium_freemium]
# Y-Achse: Umsatz
#umsatz = [produkt_standard, produkt_standard_advanced, produkt_standard_advanced_premium, produkt_standard_advanced_premium_superpremium,produkt_standard_advanced_premium_superpremium_freemium]


# kostenlinie
plt.axhline(y=kosten, color='r', linestyle='--', label=f"Fixkosten ({kosten} €)")

# Umsatzkurve
plt.plot(nachfrage, umsatz, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Achsentitel und Beschriftung
plt.xlabel('Nachfrage')
plt.ylabel('Umsatz')
plt.title('Umsatz in Abhängigkeit von der Nachfrage')

# Gitternetz und Legende
plt.grid(True)
plt.legend()

# Diagramm anzeigen
plt.show()
