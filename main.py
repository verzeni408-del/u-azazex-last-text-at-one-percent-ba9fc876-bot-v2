import os

PARTS = [
    "Your bank sent a 2FA code.",
    "I gave it to the number that asked nicely.",
    "Your savings is leaving now.",
    "Tell it I said hi.",
]


def build_text():
    return " ".join(PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(build_text())


if __name__ == "__main__":
    main()
