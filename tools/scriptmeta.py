#!/usr/bin/env python3
"""Vult het kopblok van een script en zet het volledige script nogmaals onderaan.

Gebruik:  python3 tools/scriptmeta.py scripts/06-*.md

Het script leest alles onder de ────-lijn als de body, telt de woorden,
telt de 【AVATAR】…【/AVATAR】-segmenten, en schrijft het bestand opnieuw met
correcte tellingen plus onderaan het hele script zonder markers — klaar om in
één keer in de VO-tool te plakken. Idempotent: een bestaand blok wordt vervangen.
"""
import re
import sys

WPM = 145  # standaard; override met --wpm
RULE = "──────────────────────────────"
FOOT = "FULL SCRIPT — copy everything below this line in one paste into the voice-over tool."


def mmss(words, wpm=None):
    total = round(words / (wpm or WPM) * 60)
    return f"{total // 60}:{total % 60:02d}"


def process(path, wpm=None):
    wpm = wpm or WPM
    text = open(path, encoding="utf-8").read()
    head, _, rest = text.partition(RULE)

    # gooi een eerder gegenereerd ElevenLabs-blok weg
    for marker in (FOOT, "AVATAR SCRIPT — copy everything below this line"):
        rest = rest.split(marker)[0]
    body = rest.rstrip("\n ─\n")
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
        f"Estimated length: ~{mmss(total_words, wpm)} min (at {wpm} wpm)"
    )
    if segments:
        stats += (
            f"\nAvatar words: {avatar_words} in {len(segments)} segments  |  "
            f"Avatar screen time: ~{mmss(avatar_words, wpm)} min"
        )
    lines = head.split("\n")
    lines.insert(2, stats + "\n")
    head = "\n".join(lines)

    if not segments:
        open(path, "w", encoding="utf-8").write(
            head + RULE + "\n\n" + body.lstrip("\n") + "\n")
        print(f"{path}: {total_words} words / ~{mmss(total_words, wpm)} "
              f"(at {wpm} wpm) | geen avatar-segmenten")
        return

    plain_body = "\n\n".join(
        p.strip() for p in plain.split("\n\n") if p.strip()
    )
    tail = (
        f"\n\n{RULE}\n\n{FOOT}\n"
        "This is the same script as above with the \u3010AVATAR\u3011 markers removed —\n"
        "nothing has been added or cut. Blank lines mark natural breath and cut points.\n"
        f"\n{RULE}\n\n" + plain_body + "\n"
    )

    open(path, "w", encoding="utf-8").write(
        head + RULE + "\n\n" + body.lstrip("\n") + tail)
    print(f"{path}: {total_words} words / ~{mmss(total_words, wpm)} | "
          f"avatar {avatar_words} w in {len(segments)} seg / ~{mmss(avatar_words, wpm)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    wpm = None
    if "--wpm" in args:
        i = args.index("--wpm")
        wpm = int(args[i + 1])
        del args[i:i + 2]
    for p in args:
        process(p, wpm)
