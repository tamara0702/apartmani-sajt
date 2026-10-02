# Podaci koji idu na etiketu. Izmenite ovde i pokrenite: python3 build_etikete.py
PROIZVODJAC = "[naziv proizvođača]"    # <-- UPISATI po registraciji (ne mora biti isto što i brend na logu)
ADRESA      = "[ulica i broj, mesto, Srbija]"   # <-- UPISATI tačnu adresu
REG_BROJ    = None                       # npr. "RS-12-345"; None = red se ne štampa
ORGANSKI    = False                      # True SAMO uz važeći sertifikat

# naziv fajla, širina, visina (mm, gotova veličina), neto masa, opis
ETIKETE = [
    ("bagremov-1kg",   86.0, 152.8, "1000 g", "tegla 1 kg"),
    ("bagremov-500ml", 85.0, 116.0, "700 g",  "tegla 500 ml"),
]
BLEED = 3.0      # mm viška sa svake strane
DPI = 300
