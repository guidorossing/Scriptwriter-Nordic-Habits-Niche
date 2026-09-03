---
name: nordic-persona
description: Magnus Aalberg — de AI-avatar persona van de Nordic-kanalen — met stem, uiterlijk, framing-regels en de VO/avatar-productiepijplijn. Gebruik bij het schrijven van avatar-tekst, het genereren of nabestellen van avatar-beelden, prompts voor VO of avatar-tools, of afstemming met de video-editor.
---

# Magnus Aalberg — persona en productie

## Wie hij is

Een **geboren Scandinaviër**, eind 30. Hij praat over zijn eigen cultuur van
binnenuit: eigen jeugd, eigen familie, eigen winters. Nooit als iemand die
naar Scandinavië verhuisde en het ontdekte — die framing is expliciet
afgekeurd.

**Look (vast, moet consistent blijven over alle video's)**

- Man, eind 30
- Volle rossige/rode baard
- Rode gebreide muts
- Grijze wollen trui
- Achtergrond: Noords meer, dennenbos, mistige bergen

**Stem**

- Native Scandinaviër die vloeiend Engels (US-doelgroep) spreekt, met een
  hoorbaar Nordic accent
- Rustig tempo, geen YouTube-hypertoon
- Ik-vorm, altijd
- **Gekozen VO-stem (ElevenLabs): "Test 5", voice ID `jm40tll7b9kW0hSUxaKx`**
  (vastgelegd 27-08-2026 in het Drive-doc "Magnus Aalberg Voices"; Tests 1–4
  afgevallen)

## Canon en continuïteit

Magnus' biografische feiten en terugkerende personages (6 jaar Phoenix, 11 jaar
terug, buurvrouw Kari, grootvader in Røros, enz.) staan in
`knowledge/magnus-canon.md`. Elk nieuw script moet daarmee consistent zijn;
nieuwe feiten die een script introduceert worden aan dat bestand toegevoegd.

## Schrijfregels voor zijn tekst

- Eerste persoon, verleden en heden door elkaar: observatie + anekdote
- Concrete details boven algemeenheden ("my grandmother's kitchen", niet
  "Nordic homes")
- Geen begroetingen, geen kanaalpromotie in de hook
- Hij oordeelt niet over de kijker; hij vertelt wat bij hem normaal is en laat
  het contrast het werk doen

## Productiepijplijn

Ik (als Content Creator) maak de VO en de avatar zelf en lever ze aan de
video-editor. Het genereren van de avatar valt contractueel expliciet onder
mijn verantwoordelijkheid, niet die van de editor. De editor monteert en
integreert avatarbeeld, VO en overige assets.

- **Kanaaltaal:** Engels (US)
- **Custom persona**, gebouwd vanaf een gegenereerde portretfoto — geen
  stock-avatar uit een bibliotheek. Zelfde gezicht in elke video.
- **Budget:** VO + avatar-tooling samen zo laag mogelijk, richtlijn
  **€ 30–50 per maand**.
- **Schermtijd:** ± 3 minuten per video (kostenbeheersing).

- **VO-tool: ElevenLabs** — stem "Test 5" (`jm40tll7b9kW0hSUxaKx`). Elk script
  bevat onderaan het volledige script zonder 【AVATAR】-markers, voor één paste:
  de VO wordt in één keer voor de hele video gegenereerd. De markers bovenin
  zijn voor de editor, die daar het avatarbeeld op monteert.

<!-- INVULLEN: avatar-tool (beeld/video) en maandprijzen van de accounts -->

## Aanleveren aan de editor

<!-- INVULLEN: bestandsformaten, resolutie, mapstructuur, deadline-afspraken -->

## Beeldprompt (basis)

Gebruik deze als vertrekpunt bij het nagenereren van portretten of stills, en
houd hem woordelijk gelijk om drift te voorkomen:

```
Photorealistic portrait of a Scandinavian man in his late thirties, full red
ginger beard, red knitted beanie, grey wool sweater, standing by a Nordic lake
with pine forest and misty mountains behind him, overcast natural light,
shallow depth of field, documentary photography style.
```
