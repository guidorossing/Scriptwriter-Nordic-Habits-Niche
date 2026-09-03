#!/usr/bin/env python3
"""Vult het kopblok van een script en genereert het ElevenLabs-blok onderaan.

Gebruik:  python3 tools/scriptmeta.py scripts/06-*.md

Het script leest alles onder de ────-lijn als de body, telt de woorden,
verzamelt alle 【AVATAR】…【/AVATAR】-segmenten, en schrijft het bestand
opnieuw met correcte tellingen en een compleet AVATAR SCRIPT-blok.
Idempotent: een bestaand AVATAR SCRIPT-blok wordt vervangen.
"""
import re
import sys

WPM = 145
RULE = "──────────────────────────────"
FOOT = "AVATAR SCRIPT — copy everything below this line in one paste into ElevenLabs."


def mmss(words):
    total = round(words / WPM * 60)
    return f"{total // 60}:{total % 60:02d}"


def process(path):
    text = open(path, encoding="utf-8").read()
    head, _, rest = text.partition(RULE)

    # gooi een eerder gegenereerd ElevenLabs-blok weg
    body = rest.split(FOOT)[0].rstrip("\n ─\n")
    body = body.rstrip()

    segments = re.findall(r"【AVATAR】(.*?)【/AVATAR】", body, flags=re.S)
    segments = [" ".join(s.split()) for s in segments]

    plain = body.replace("【AVATAR】", "").replace("【/AVATAR】", "")
    total_words = len(plain.split())
    avatar_words = sum(len(s.split()) for s in segments)

    head = re.sub(r"Total words: .*", "", head)
    head = re.sub(r"Avatar words: .*", "", head)
    head = re.sub(r"\n{3,}", "\n\n", head)

    stats = (
        f"Total words: {total_words:,}  |  "
        f"Estimated length: ~{mmss(total_words)} min (at {WPM} wpm)\n"
        f"Avatar words: {avatar_words} in {len(segments)} segments  |  "
        f"Avatar screen time: ~{mmss(avatar_words)} min"
    )
    lines = head.split("\n")
    lines.insert(2, stats + "\n")
    head = "\n".join(lines)

    tail = (
        f"\n\n{RULE}\n\n{FOOT}\n"
        "These are all avatar segments in order of appearance. Keep the blank lines:\n"
        "they mark where each on-screen clip ends, so the audio can be cut per segment.\n"
        f"\n{RULE}\n\n" + "\n\n".join(segments) + "\n"
    )

    open(path, "w", encoding="utf-8").write(
        head + RULE + "\n\n" + body.lstrip("\n") + tail)
    print(f"{path}: {total_words} words / ~{mmss(total_words)} | "
          f"avatar {avatar_words} w in {len(segments)} seg / ~{mmss(avatar_words)}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        process(p)
