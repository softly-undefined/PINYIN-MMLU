import csv
import json
from collections import defaultdict
from pathlib import Path

from pypinyin import lazy_pinyin
from pypinyin.constants import PINYIN_DICT


OUTPUT_FILE = Path(__file__).with_name("pinyin_mappings.csv")


def build_pinyin_mapping():
    mapping = defaultdict(list)

    for codepoint in sorted(PINYIN_DICT):
        char = chr(codepoint)
        pinyin_values = lazy_pinyin(char, errors="ignore")
        if len(pinyin_values) != 1 or not pinyin_values[0]:
            continue
        mapping[pinyin_values[0]].append(char)

    return mapping


def write_csv(mapping, output_file: Path):
    with output_file.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=["pinyin", "characters", "num_characters"],
        )
        writer.writeheader()

        for pinyin in sorted(mapping):
            characters = mapping[pinyin]
            writer.writerow(
                {
                    "pinyin": pinyin,
                    "characters": json.dumps(characters, ensure_ascii=False),
                    "num_characters": len(characters),
                }
            )


def main():
    mapping = build_pinyin_mapping()
    write_csv(mapping, OUTPUT_FILE)
    print(f"Wrote {len(mapping)} pinyin rows to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
