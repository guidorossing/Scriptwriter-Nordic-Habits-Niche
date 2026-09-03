# Geleverde scripts

Drive is de bron van de definitieve tekst; dit is de index. Volledige tekst
ophalen kan via de Drive-connector met het doc-ID.

| # | Titel | Woorden | Lengte | Avatar | Drive doc-ID | Geleverd |
|---|---|---|---|---|---|---|
| 01 | 5 Nordic Habits That Melt Belly Fat - Start Right Now! | 2.169 | ~14:58 | 419 w / 22 seg | `12KDK9SWie0kWk8mbLvB_FWIc6ePv0RZtpBe9VMXRtpA` | 27-08-2026 |
| 02 | 7 American Hygiene Habits That Disgust Nordic People - You Need To Stop Now! | 2.426 | ~16:44 | 435 w / 22 seg | `1c7Tg64ymQLQEReWm-q_hG07UHV4ioOrLCvEgEV7r77g` | 27-08-2026 |
| 03 | 11 Nordic Habits That INSTANTLY Make Life Better - Try Today! | 2.402 | ~16:34 | 414 w / 24 seg | `1vrsJHAFfet3nLVIgowKgS8_B2_PPtnIb7oizu2Oml7Q` | 27-08-2026 |
| 04 | 12 Things Nordic People Avoid In Their Houses - You Should Copy Today! | 2.410 | ~16:37 | 418 w / 27 seg | `1t9RYtXby8QtiYVU1saV1bPUKxEVcoYBQMqMSRINJP7Q` | 27-08-2026 |
| 05 | 8 Nordic Secrets To Sleep LESS And Wake Up FRESH - You Should Start Tonight! | 2.277 | ~15:42 | 432 w / 22 seg | `1IFplRZmnbvYzieEH6vopQ2KVAjGR0SVXy5FJkBFoxqU` | 27-08-2026 |

Bronvideo's per titel: `knowledge/titel-bronnen.md`.
Volgende scripts nummeren door vanaf 06.

## Geschreven 03-09-2026 — als Google Doc in de Drive-map "Titles 6 - 11"

Batch 06–11 uit het Drive-doc "Titles 6 - 11". Nieuw t.o.v. 01–05: doellengte
**16–18 min**, Phoenix (niet London) als canon, en de refrain is weer verplicht.
Zowel `.md` als `.docx` staan in `scripts/`; de Google Docs staan in Drive-map
`127qMMVsFsiEdcgZkzFLQQHiCmWvyWznX`.

| # | Titel | Woorden | Lengte | Avatar | Drive doc-ID |
|---|---|---|---|---|---|
| 06 | 9 Struggles Nordic People Refuse To Accept In A Simpler Life! | 2.383 | ~16:26 | 418 w / 20 seg | `1OBw-pY4URh9dZkdo8TEmHJ1IPwMtQCQhV8AvsOsHTTE` |
| 07 | 7 Things Nordic People Do Every Morning Before 8 AM And Make Life Easier! | 2.391 | ~16:29 | 431 w / 20 seg | `1oqcPFshrNrziIAbPTJ5uoKrJNT8kE1LYX0FZiN_QL3Y` |
| 08 | 11 Things Nordic People Quit Doing After 40 To Live A Simpler Life! | 2.394 | ~16:31 | 436 w / 19 seg | `1rY2ztOvzgI6RA_YlwK3CenSb-QNPDRe1h8spiEqbiqc` |
| 09 | 12 Scandinavian Cleaning Habits That Keep Homes Spotless And You Should Start Today! | 2.339 | ~16:08 | 447 w / 19 seg | `1sO7XpLMLsO_CB2zrVlWK5hhFB26lPAuli6_DVmKVwUQ` |
| 10 | 9 Nordic Home Ideas That Save Space And Calm Your Mind | 2.385 | ~16:27 | 441 w / 19 seg | `1Vzrd9U_9xjVIAqrZdbq3QtiG9ILQpbFKxF49Pu7An1k` |
| 11 | 13 Things You'll Never Find In A Nordic Home (And Why They're Happier)! | 2.397 | ~16:32 | 431 w / 20 seg | `1jJkU01gOzrXYIUlR7pgp7tfVC28dOnjwY2vzdcsvByw` |

Tellingen worden gegenereerd met `python3 tools/scriptmeta.py scripts/<bestand>.md`;
de `.docx` met `python3 tools/md2docx.py scripts/<bestand>.md`.
