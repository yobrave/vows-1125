"""vows-1125: robot wedding vow, one line, gate at 160 chars."""

import json
import os

TERMS = {"source": "entry.txt", "ceiling": 160, "output": "entry.txt"}


def read_vow(folder):
    vow = None
    with open(os.path.join(folder, TERMS["source"]), encoding="utf-8") as reader:
        for row in reader:
            if row.strip():
                vow = row.strip()
    if vow is None:
        raise SystemExit("empty vow book")
    return vow


def bless(text):
    if len(text) > TERMS["ceiling"]:
        raise SystemExit("vow too long for the altar: %d chars" % len(text))
    return True


def deliver(folder, text):
    chapel = os.environ.get("MAKEFUN_OUTPUT_DIR") or folder
    os.makedirs(chapel, exist_ok=True)
    altar = os.path.join(chapel, TERMS["output"])
    with open(altar, "w", encoding="utf-8", newline="\n") as keeper:
        keeper.write(text + "\n")
    return altar


folder = os.path.dirname(os.path.abspath(__file__))
vow = read_vow(folder)
bless(vow)
print(json.dumps({"ring": vow[:42], "chars": len(vow), "uptake": "till reboot do us part", "altar": deliver(folder, vow)}))
