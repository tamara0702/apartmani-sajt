# Etikete „Bagremov med“ – Pčelinji dom

| Fajl | Gotova veličina | Sa viškom (3 mm) | Piksela (300 dpi) |
|---|---|---|---|
| `bagremov-1kg` | 86 × 152,8 mm | 92 × 158,8 mm | 1087 × 1876 |
| `bagremov-500ml` | 85 × 116 mm | 91 × 122 mm | 1075 × 1441 |

Za štampu: `.pdf` (vektorski, tačne dimenzije) ili `.png` (300 dpi). `*-pregled.png` ima
ružičastu liniju sečenja i plavu sigurnu zonu (3 mm unutra) – nije za štampu.

## Pre štampe obavezno
1. **Logo**: koristi se `../logo.svg` (Dedin med organic). Natpis „ORGANIC“ na logu se automatski izostavlja dok `ORGANSKI = False`.
2. **Podaci** u `podaci.py`: naziv i adresa proizvođača (sada su mesta za upis), broj registracije (`REG_BROJ`).
3. **Organski**: reč se ne štampa; `ORGANSKI = True` samo uz važeći sertifikat.
4. Neto masa za teglu 500 ml je 700 g – proveriti vaganjem.
5. Datum („Najbolje upotrebiti do“) i LOT su linije za štampač/pečat/ručni upis.

Ponovno generisanje: `python3 build_etikete.py && node render.js`
(Playwright + Chromium; fontovi Liberation Serif i DejaVu Serif).
