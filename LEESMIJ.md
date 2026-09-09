# Zo gebruik je deze repo

## Installeren

1. Clone deze repo naar de plek waar je aan de Nordic-kanalen werkt, of open
   hem direct in Claude Code (lokaal of via claude.ai/code).
2. Open een terminal in de map en start `claude`.
3. Claude Code laadt `CLAUDE.md` automatisch — dat zijn je project-instructies.

Geen installatie nodig voor de skills en commands; die worden gevonden zodra ze
in `.claude/` staan.

## Wat waar staat

```
CLAUDE.md                        projectinstructies — altijd geladen
.claude/skills/                  kennis die alleen laadt als hij relevant is
  nordic-script/SKILL.md         het scriptplaybook
  nordic-research/SKILL.md       keyword- en titelresearch
  script-qa/SKILL.md             scripts van medewerkers nakijken
  nordic-persona/SKILL.md        Magnus Aalberg + VO/avatar-pipeline
.claude/commands/                slash-commands
  nieuw-script.md                → /nieuw-script
  titel-research.md              → /titel-research
  script-review.md               → /script-review
knowledge/                       jouw eigen bronbestanden
scripts/                         opgeleverde scripts
```

## Het verschil tussen CLAUDE.md en een skill

`CLAUDE.md` zit in élke sessie in het geheugen. Zet er dus alleen in wat altijd
geldt — regels, kanalen, persona in het kort. Alles wat maar soms nodig is
(een volledig playbook, een QA-checklist) hoort in een skill. De `description`
bovenaan een skill bepaalt wanneer hij afgaat, dus die moet de woorden bevatten
die jij zou gebruiken als je erom vraagt.

## Nog invullen

Doorzoek de map op `INVULLEN` — daar heb ik iets gelaten wat ik niet zeker
weet:

- `CLAUDE.md` — positionering en keywords van The Nordic Way en Nordic Wisdom
- `nordic-script/SKILL.md` — je exacte word-count-tabel (mijn getallen zijn
  afgeleid van 14–16 min bij ~150 woorden per minuut)
- `script-qa/SKILL.md` — overige schrijvers naast Ufuoma
- `nordic-persona/SKILL.md` — gekozen VO- en avatar-tools, en de
  aanleverafspraken met je editor

## Bestaande knowledge files meenemen

Download ze uit het claude.ai-project en zet ze in `knowledge/`. Kleine,
altijd-relevante bestanden noem je in `CLAUDE.md`; grote of situatie-specifieke
bestanden hang je onder de bijbehorende skill in dezelfde map als de
`SKILL.md`, met een verwijzing ernaar in de skilltekst.

## MCP-servers

Je NexLev- en Google Drive-connectors zitten niet in deze zip — die stel je in
Claude Code apart in met `claude mcp add`. Zonder NexLev werkt
`/titel-research` niet volledig.
