---
name: nordic-research
description: Keyword-, titel- en nicheresearch voor de Nordic-kanalen volgens de pillar-broadening methode, met NexLev-patronen voor benchmarking en outlierdetectie. Gebruik bij het zoeken van nieuwe videotitels, het toetsen van vraag versus aanbod, het benchmarken van concurrentiekanalen of het opzetten van een uploadrotatie.
---

# Nordic research

## De vaste methode (pillar broadening)

Pas deze standaard toe, ook als er niet expliciet om gevraagd wordt.

1. **Isoleer het winnende titel-skelet** — getal + autoriteit + onderwerp +
   uitkomstbelofte. Haal het uit een bewezen outlier, niet uit een gemiddelde
   video.
2. **Bouw 8–10 pillars** — inhoudelijke onderwerpen die bij het kanaal passen
   (bijv. slaap, geld, huis, eten, ochtendroutine, sociale codes, winter,
   opvoeding, werk, gezondheid).
3. **Plug elke pillar in het skelet** — levert 8–10 kandidaat-titels.
4. **Toets vraag versus aanbod** per titel: bestaat de vraag aantoonbaar, is
   het aanbod dun?
5. **Rangschik op overlap-potentieel** — hoeveel deelt de titel met wat het
   kanaal al doet (algoritme-consistentie).
6. **Bouw een rotatieschema** — 2–3 hoofdpillars + 3–4 secundaire pillars.
7. **Test klein, verdubbel op winnaars.**

## NexLev-patronen

Werk met de NexLev-tools; verzin nooit cijfers.

- **Kanaal opzoeken:** `channel_resolver` → channel ID →
  `youtube_channel_videos` met sortering op populair, voor benchmarking.
- **Outlierresearch:** `minOutlierScore: 3` met `isExactMatch: true`.
- **Async tools:** `get_similar_channels` en `get_niche_overview` geven een
  `jobId` terug — pollen tot het resultaat er is.
- **Transcripten:** `get_bulk_video_transcripts` geeft geneste JSON die op twee
  niveaus geparsed moet worden.
- **Puur numeriek filteren** in de niche finder: `query: "*"` met de numerieke
  filters, in plaats van een semantische zoekterm.

## Vaste kanaalkennis

- Dominante term: **"nordic habits"**.
- Onderpresteerders: "hygge", landspecifieke termen (swedish/danish/norwegian
  lifestyle). Niet als hoofdkeyword gebruiken; hooguit als secundaire term in
  de description.
- Benchmarkkanalen: **Japan Genius** (structuur), **Inside Japan Living**
  (onderwerpbron voor remakes), **FrankMillerCuts** (avatar-inzet).

## Wat een research-oplevering bevat

1. De 8–10 pillars, met per pillar één zin waarom hij bij dit kanaal past
2. De kandidaat-titels in het skelet
3. Per titel: bewijs voor vraag (concrete kanalen/video's met cijfers) en een
   inschatting van aanbod
4. Ranking met korte motivering
5. Voorgestelde rotatie: 2–3 hoofd + 3–4 secundair
6. De drie titels waarmee ik zou beginnen, en waarom

Beknopt, in het Nederlands, cijfers in een tabel.
