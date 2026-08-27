---
name: nordic-script
description: Het scriptplaybook voor de Nordic-lifestyle kanalen — structuur, intro-regels, terugkerende beats, word counts en avatar-markering. Gebruik bij het schrijven, herschrijven of uitbreiden van een videoscript, VO-tekst of hook voor NordicLifestyle, The Nordic Way of Nordic Wisdom.
---

# Nordic script playbook

Alle output in dit playbook is **Engels (US)**, in de **ik-vorm**, uitgesproken
door Magnus Aalberg (zie de `nordic-persona` skill en
`knowledge/magnus-canon.md` — de canonfeiten daar zijn bindend).

Het maatgevende voorbeeldmateriaal: de vijf geleverde scripts in `scripts/`
(27-08-2026). Nieuw werk volgt dat format exact.

## 1. De titel-skeletten

Een werkende titel bevat: **getal + autoriteit + onderwerp + belofte/uitkomst
+ actie-suffix**.

```
{getal} Nordic Habits That {uitkomst} - {actie}!            → "…That Melt Belly Fat - Start Right Now!"
{getal} Things Nordic People Avoid {context} - {actie}!     → "…In Their Houses - You Should Copy Today!"
{getal} Nordic Secrets To {uitkomst} - {actie}!             → "…Sleep LESS And Wake Up FRESH - You Should Start Tonight!"
{getal} American {onderwerp} Habits That Disgust Nordic People - {actie}!
```

Bronmapping van de eerste vijf titels (remakes): `knowledge/titel-bronnen.md`.

## 2. Documentformat (exact zo opleveren)

Elk script begint met dit kopblok:

```
TITLE: <volledige videotitel>

Total words: X,XXX  |  Estimated length: ~MM:SS min (at 145 wpm)
Avatar words: XXX in NN segments  |  Avatar screen time: ~M:SS min

LEGEND: Text between 【AVATAR】 and 【/AVATAR】 is spoken by Magnus (the AI
avatar) visibly on camera. All other text is voice-over with B-roll or stock
footage. At the very bottom of this document all avatar segments are collected
in one block for a single paste into ElevenLabs.
```

En eindigt met het ElevenLabs-blok:

```
──────────────────────────────

AVATAR SCRIPT — copy everything below this line in one paste into ElevenLabs.
These are all avatar segments in order of appearance. Keep the blank lines:
they mark where each on-screen clip ends, so the audio can be cut per segment.

──────────────────────────────

<alle avatar-segmenten, in volgorde, gescheiden door lege regels>
```

## 3. Scriptstructuur

```
[COLD OPEN]      avatar — herhaalt titel letterlijk, directe aanspreking,
                 tease van een hoog item ("And number one is …"),
                 telrichting ("Five, weakest first") en een startcommando
[ITEM #N → #1]   VO over b-roll, met korte avatar-interjecties
  ├─ claim / scène
  ├─ onderzoek of hard feit (nooit verzonnen; bron benoemen in de tekst)
  ├─ honesty beat waar nodig ("Now, I owe you the truth … I will not oversell you")
  ├─ persoonlijke anekdote (London, Kari, grootvader in Røros — zie canon)
  ├─ het mechanisme (waarom het werkt)
  └─ concrete instructie ("Try one tomorrow …", "Swap the bulbs tonight …")
[BRUG halverwege] één zin die de resterende items als zwaarder aankondigt
                 ("The last two are the ones people find hardest to accept …")
[ITEM #1]        het sterkste item; bindt de hele lijst tot één idee
[OUTRO]          avatar — concrete startopdracht ("Start with the cheapest
                 three …") + slotformule:
                 "You were never X. You were only/simply Y. Subscribe. More next week."
```

Countdown loopt **aftellend** naar #1; het beste item staat op #1 en item #1
formuleert het overkoepelende principe ("The house has been sealed against the
place it stands in").

## 4. Intro-regels — hier wordt het meest op afgekeurd

- De eerste zin **herhaalt letterlijk (een deel van) de videotitel** en maakt
  hem persoonlijk: "Seven American hygiene habits disgust Nordic people, and I
  watched a guest do four of them in my hallway before his coat was off."
- Directe aanspreking van de kijker binnen twee zinnen ("Look down at your
  stomach right now." / "You are sitting under the first one right now.").
- Tease van een hoog genummerd item: "And number one/two is …".
- Sluit af met telrichting + startcommando: "Five, weakest first. Start
  tonight."
- Verboden: "Have you ever wondered …", "In today's video …", "Welcome back",
  elke begroeting, elke parafrase van de titel.

## 5. Terugkerende beats (i.p.v. een letterlijke refrain)

De geleverde scripts gebruiken geen woordelijk herhaalde refrainzin, maar
vaste beats die hetzelfde werk doen:

1. **Honesty beat** — minstens 1× per video zwakt Magnus zijn eigen bewijs
   eerlijk af ("That was eight men. … I am not going to inflate eight people
   into a promise."). Dit is het merk van het kanaal; nooit overslaan.
2. **Avatar-vragen als scharnier** — korte on-screen vragen ("So what does
   that buy a country?") die de VO beantwoordt.
3. **Rode draad in item #1** — het slotitem benoemt expliciet wat alle items
   gemeen hadden.
4. **Outro-formule** — "You were never X. You were only/simply Y. Subscribe.
   More next week."
5. **Canon-anekdotes** — London (6 jaar), Kari (74, grijs wollen vest),
   grootvader in Røros. Zie `knowledge/magnus-canon.md`.

Het kernkeyword van de video staat in de titel, de eerste 30 seconden en
terugkerend in de itemteksten.

## 6. Word counts

Gebaseerd op de vijf geleverde scripts; reken met **145 wpm**.

| Onderdeel | Richtlijn | Geleverd ( referentie) |
|---|---|---|
| Totale video | 14–16 min ≈ **2.030–2.320 woorden** | 2.169–2.426 |
| Cold open | 60–80 woorden | ±70 |
| Per item | geen harde cap; sterkste items langst | 150–350 |
| Outro | 60–100 woorden (avatar) | ±80 |

Lengte wint van elke cap. Kom je onder 14 minuten, verleng dan de sterkste
items in plaats van items toe te voegen. Boven ±2.400 woorden (>16:30) juist
inkorten bij de zwakkere items.

## 7. Avatar-markering

Inline markeren met **【AVATAR】 … 【/AVATAR】**; alles daarbuiten is VO over
b-roll (geen aparte VO-tag). Doel: **±420–435 avatar-woorden in 20–27 korte
segmenten** ≈ 2:50–3:00 schermtijd.

- Segmenten zijn kort: één zin tot drie zinnen; veel zijn vragen of
  kernuitspraken. Geen lange avatar-monologen buiten de cold open.
- Vaste avatar-momenten: de volledige cold open, de honesty beats, de
  scharniervragen, de persoonlijke canon-uitspraken ("There is no radiator in
  the room where I sleep …"), de slotinstructie en de outro-formule.
- Onderaan het document komen alle segmenten nogmaals in het ElevenLabs-blok
  (zie §2), gescheiden door lege regels als knippunten.

Referentie voor hoe de verdeling voelt: FrankMillerCuts.

## 8. Checklist vóór oplevering

- [ ] Kopblok met TITLE, woordtelling, lengte bij 145 wpm, avatar-telling
- [ ] Intro herhaalt de titel letterlijk + tease + telrichting + startcommando
- [ ] Volledig in de ik-vorm, geen outsider-framing
- [ ] Minstens één honesty beat; cijfers en studies kloppen (niets verzonnen)
- [ ] Canonfeiten consistent met `knowledge/magnus-canon.md`
- [ ] Totale woordtelling 2.030–2.320 (max ±2.400)
- [ ] 【AVATAR】-segmenten: ±420–435 woorden, 20–27 segmenten
- [ ] Outro-formule aanwezig, eindigend op "Subscribe. More next week."
- [ ] Kernkeyword in titel en eerste 30 seconden; geen "hygge", geen
      landspecifieke term als hoofdterm
- [ ] ElevenLabs-blok onderaan compleet en identiek aan de inline segmenten
- [ ] Geleverd als `.docx`

## 9. Oplevering

Schrijf het script naar `scripts/NN-<slug>.md` (doornummeren op de bestaande
reeks), converteer daarna naar `.docx`. Guido zet hem zelf in de Drive-map
(of vraag of je hem via de Drive-connector mag plaatsen).
