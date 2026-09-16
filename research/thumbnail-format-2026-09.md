# Thumbnail-teardown — celebrity-clips niche

**Onderzocht:** [@Knanuel / Papa Ruzz](https://www.youtube.com/@Knanuel), [@celebsgoat / Celebs Goat](https://www.youtube.com/@celebsgoat), [@Belmorra](https://www.youtube.com/@Belmorra)
**Datum:** 16 september 2026 · **Steekproef:** 47 thumbnails (35 recente uploads + 12 extremen)
**Interactief rapport:** https://claude.ai/artifact/RpCHk9cF1wwGuPv4eTVaB2

---

## Kern

Alle drie de kanalen verkopen hetzelfde plaatje: **een beroemdheid die stoïcijns blijft
terwijl iemand naast hem instort van het lachen.** Wat verschilt is hoe ze eraan komen.

| Kanaal | Methode | Abo's | Kenmerk |
|---|---|---|---|
| Papa Ruzz | knipt uit bestaand beeldmateriaal | 156K | enige kanaal dat soms tekst gebruikt |
| Celebs Goat | plakt composieten in Photoshop | 77,3K | spit-take in bijna elke thumbnail |
| Belmorra | genereert volledig met AI | 10,4K | 10 van de 11 video's is een AI-scène |

## Vijf archetypes

| # | Archetype | Omschrijving | PR | CG | BM |
|---|---|---|---|---|---|
| A | Ruwe still | onbewerkte screenshot, geen tekst | 11/17 | 1/19 | 0/11 |
| B | Still + markering | rode cirkel of 3–4-woordscitaat in wit vet | 3/17 | 0/19 | 0/11 |
| C | Spit-take composiet | 2–3 uitsnedes, één spuugt water uit | 0/17 | 13/19 | 1/11 |
| D | Gag-composiet | 2–3 uitsnedes, visuele grap i.p.v. spit-take | 0/17 | 3/19 | 0/11 |
| E | AI-scène | gefabriceerd tafereel, "reactie-sandwich" | 3/17 | 2/19 | 10/11 |

## Compositieregels (gelden in alle 47)

- **2 of 3 personen** — nooit één, nooit vier of meer op de voorgrond
- **Precies één anker** met neutraal/onbewogen gezicht; bij drie personen in het midden, bij twee links
- **De reactie is extreem** — open mond, dubbelklappen, spugen. Nooit een glimlach (leest niet op 200px)
- **Hoofden in de bovenste helft** van het frame
- **Geen rand, geen logo, geen kanaalhandtekening**
- **94% bevat geen enkele tekst** (44 van 47)

## Gedeelde asset-bibliotheek — de belangrijkste vondst

De drie kanalen concurreren niet, ze **delen een productiepijplijn**:

1. **Awards-publiek-template**, 4× over 3 kanalen — identiek camerastandpunt, zaalverlichting,
   microfoon en compositie; alleen de hoofdpersoon en zijn kostuum wisselen:
   - Papa Ruzz / Dolly Parton (`kwDxpeEV1WY`) — 435K
   - Celebs Goat / Emilia Clarke (`JHLxIQgD8A4`) — 1,0M
   - Celebs Goat / Matt Damon (`aj_kMULpKUw`) — 818K
   - Belmorra / Joe Pesci (`loHAsIVYFTA`) — 672K
2. **Italiaans restaurantdecor** (roodgeruite tafelkleden), 3× over 2 kanalen:
   `z1DeAUU04vk`, `r2opRhXBuAQ` (Celebs Goat) en `cnOZPmnZYdA` (Belmorra).
   Pixelgewijze RGB-afstand van de centrale achtergrondstrook: 13–22,
   tegen 37–85 voor niet-verwante thumbnails.
3. **Ballon-rekwisiet**: `xFGZQK2HQUw` (Papa Ruzz, rood) en `COjtFtfDpkQ` (Celebs Goat, geel).

> Een losse thumbnail namaken is daarom het verkeerde doel. Bouw hún apparaat:
> een bibliotheek van herbruikbare achtergronden en reactie-poses waar je wekelijks
> een nieuwe hoofdpersoon in schuift.

## Prestatie per archetype

Mediane weergaven, alle drie de kanalen samen, video's jonger dan een week weggelaten.

| Archetype | Mediaan | n | Spreiding |
|---|---|---|---|
| D — gag-composiet | 1,0M | 3 | 26K – 2,4M |
| E — AI-scène | 677K | 14 | 2,4K – 2,5M |
| A — ruwe still | 226K | 12 | 4,5K – 1,5M |
| C — spit-take composiet | 205K | 14 | 8,8K – 2,5M |
| B — still + markering | — | 2 | 40K & 1,3M (te weinig data) |

**Lees de spreidingen, niet de medianen.** Elk archetype spant drie ordes van grootte.
Het format bepaalt de uitkomst dus niet — het legt een bodem.

De awards-template is de meest consistente: de zwakste van de vier (435K) verslaat
de mediaan van elk ander archetype. De drie zwakste AI-scènes (Dick Van Dyke 2,4K,
een onherkenbare Conan-scène 4K, Willem Dafoe 17K) falen niet op format maar op
hoofdpersoon.

> **Format zet de bodem, de celebrity zet het plafond.**

## Meetbare huisstijl

Ondanks drie verschillende productiemethodes komen de kanalen op vrijwel dezelfde
kleurwaarden uit — er zit één gedeelde grading achter.

| Meting | Papa Ruzz | Celebs Goat | Belmorra |
|---|---|---|---|
| Warme pixels (fractie) | 0,60 | 0,60 | 0,60 |
| Verzadiging (0–255) | 117 | 114 | 112 |
| Helderheid (0–255) | 107 | 122 | 117 |
| Contrast (std.dev.) | 55 | 48 | 62 |
| Resolutie | 1280×720 | 1280×720 | 1280×720 |

## Toepassing

1. Bouw een bibliotheek van 5–8 achtergronden die "dit is echt gebeurd" zeggen
   (talkshowbank, press-junketkamer, restaurant, awardshow-publiek, sitcomwoonkamer)
2. Bouw een bibliotheek van reactie-poses (spit-take, dubbelklapper, hand-voor-de-mond)
3. Leg één grading vast: warm, verzadiging ~115, helderheid ~115
4. **Kies de beroemdheid vóór het beeld** — dit is waar de zwakke video's stukliepen
5. Zet het deadpan-anker in het midden, de instorting links en rechts
6. Laat tekst weg; als je het toch doet, één citaat van 3–4 woorden tussen aanhalingstekens

## Voorbehoud

- **Weergaven zijn geen CTR.** Van buitenaf is een zwakke thumbnail met een sterke titel
  niet te onderscheiden van een echte winnaar.
- **Kleine, scheve steekproef.** Archetype E komt grotendeels van Belmorra, dat zo klein
  is dat één uitschieter de mediaan verschuift.
- **Niet genormaliseerd op leeftijd.** Video's jonger dan een week zijn weggelaten,
  de rest niet gecorrigeerd.
- **De AI-classificatie is een beoordeling, geen detectie** — gebaseerd op onmogelijke
  combinaties van personen, afwijkende handen en gezichtsranden, en taferelen die
  aantoonbaar nooit hebben plaatsgevonden.

Losse observatie: de nieuwste Papa Ruzz-video serveert zijn thumbnail als
`hq720_custom_1.jpg` in plaats van `hq720.jpg`, wat erop wijst dat de thumbnail na
publicatie is vervangen of in een test loopt. Van buitenaf niet te bevestigen —
maar het is het overwegen waard of zij A/B-testen.

## Methode

47 thumbnails opgehaald op maxres-resolutie (1280×720) van `i.ytimg.com` en stuk voor
stuk visueel beoordeeld: 35 recente uploads plus 12 extra video's gekozen op extreme
prestaties, om te controleren of winnaars en verliezers een ander format volgen.
Kleur, contrast en luminantieverdeling gemeten met Pillow; achtergronden vergeleken via
pixelgewijze RGB-afstand over de centrale beeldstrook. Kanaal- en weergavecijfers via
de NexLev YouTube-API.
