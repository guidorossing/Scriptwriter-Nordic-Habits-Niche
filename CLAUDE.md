# Nordic Channels — projectinstructies

Dit bestand wordt automatisch geladen bij elke Claude Code-sessie in deze map.
Het is het equivalent van de project-instructies in claude.ai.

## Wat dit project is

Een portfolio van faceless Nordic-lifestyle YouTube-kanalen, gedreven door één
AI-avatar-persona. Het werk in deze map bestaat uit: keyword- en titelresearch,
scripts schrijven, scripts reviewen, en kanaalteksten (descriptions, about).

**Kanalen**

| Kanaal | Positionering | Kernkeywords |
|---|---|---|
| NordicLifestyle | Hoofdkanaal | nordic habits, nordic minimalism, scandinavian lifestyle |
| The Nordic Way | Gedifferentieerde framing — <!-- INVULLEN: hoe precies --> | <!-- INVULLEN --> |
| Nordic Wisdom | <!-- INVULLEN --> | <!-- INVULLEN --> |

## Werktaal

- **Overleg met mij (Guido): Nederlands.**
- **Alle output voor het kanaal — scripts, titels, descriptions, VO: Engels (US).**
- Feedback voor externe medewerkers: eenvoudig Engels.

## Vaste regels (gelden altijd, ook als ik ze niet noem)

1. **Keyword-basis.** "nordic habits" is de dominante term. "Hygge" en
   landspecifieke termen (swedish/danish/norwegian ...) presteren slecht —
   gebruik ze niet als hoofdkeyword.
2. **Videolengte:** 14–16 minuten. Als de word-count-cap per item botst met die
   lengte, wint de lengte — de cap mag gebroken worden.
3. **Format:** countdown/listicle met een terugkerende refrain die de items
   verbindt.
4. **Intro:** herhaalt letterlijk (deels) de videotitel — niet parafraseren.
   Moet de kijker direct binnentrekken. Generieke openingen worden afgekeurd.
5. **Ik-vorm.** Het hele script staat in de eerste persoon, want het kanaal
   gebruikt een AI-avatar die spreekt. Referentiekanaal voor deze toon:
   FrankMillerCuts.
6. **Avatar-schermtijd:** ± 3 minuten per video, om kosten te drukken. Markeer
   in elk script welke passages avatar-on-screen zijn (intro + kernzinnen).
7. **Geen outsider-framing.** De verteller is een geboren Scandinaviër die over
   zijn eigen cultuur praat — nooit "ik verhuisde naar Zweden en ontdekte ...".

## De persona

**Magnus Aalberg** — geboren Scandinaviër, eind 30.

- Uiterlijk: volle rossige baard, rode gebreide muts, grijze wollen trui,
  achtergrond van een Noords meer met dennenbos en mistige bergen.
- Stem: native Scandinaviër die vloeiend Engels spreekt, met Nordic accent.
- Hij spreekt vanuit binnen de cultuur, met eigen ervaring en familie-
  anekdotes — niet als onderzoeker of buitenstaander.

De VO en avatar maak ik zelf; de video-editor krijgt ze aangeleverd en
integreert ze. Zie `.claude/skills/nordic-persona/SKILL.md`.

## Referentiemateriaal

- **Structuur:** Japan Genius (opbouw van scripts)
- **Toon en avatar-inzet:** FrankMillerCuts
- **Onderwerpbron voor remakes:** Inside Japan Living

## Output en opslag

- Scripts worden geleverd als `.docx` en daarnaast opgeslagen als Google Doc in
  de Drive-map **Scripts**.
- Werkbestanden in deze map: zie `knowledge/` voor bronmateriaal en
  `scripts/` voor lopende scripts.

## Werkwijze in dit project

- Wees direct en beknopt. Geen samenvattingen van wat je net gedaan hebt.
- Lever liever een concrete v1 op die ik aanscherp dan een vraag vooraf.
- Denk mee: als je een betere titelhoek, pillar of structuur ziet, zeg het.
- Verzin geen cijfers. Als research nodig is, doe research (NexLev) of zeg dat
  het cijfer ontbreekt.

## Vaardigheden in deze map

Deze laden automatisch wanneer relevant:

- `nordic-script` — het scriptplaybook (structuur, intro's, refrain,
  word counts, avatar-markering)
- `nordic-research` — keyword- en titelresearch volgens de pillar-methode
- `script-qa` — scripts van medewerkers nakijken en feedback opstellen
- `nordic-persona` — Magnus Aalberg: consistentie in stem, look en VO-pipeline

## Slash-commands

- `/nieuw-script` — nieuw script van titel tot afgewerkt .docx
- `/titel-research` — pillars en titels genereren en toetsen
- `/script-review` — script van een medewerker beoordelen
