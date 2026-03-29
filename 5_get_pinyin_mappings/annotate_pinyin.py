import csv
import re
from pathlib import Path
from tempfile import NamedTemporaryFile


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "mmlu_ZH-PY.csv"
MAPPINGS_FILE = BASE_DIR / "pinyin_mappings.csv"
TEXT_COLUMNS = [
    "Question_ZH-PY",
    "A_ZH-PY",
    "B_ZH-PY",
    "C_ZH-PY",
    "D_ZH-PY",
]
TOKEN_PATTERN = re.compile(r"(?<![A-Za-z])[a-z]+(?![A-Za-z])")
LATEX_PATTERN = re.compile(r"\$.*?\$", re.DOTALL)


def load_complexity_map(path: Path):
    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return {row["pinyin"]: int(row["num_characters"]) for row in reader}


def iter_scored_tokens(text: str):
    cleaned_text = LATEX_PATTERN.sub(" ", text)
    for match in TOKEN_PATTERN.finditer(cleaned_text):
        yield match.group(0)


def score_row(row, complexity_map):
    values = []

    for column in TEXT_COLUMNS:
        for token in iter_scored_tokens(row.get(column, "")):
            complexity = complexity_map.get(token)
            if complexity is None:
                continue
            values.append(complexity)

    pcs = sum(values)
    pcm = pcs / len(values) if values else 0.0
    return pcs, pcm


def annotate_csv():
    complexity_map = load_complexity_map(MAPPINGS_FILE)

    with INPUT_FILE.open(encoding="utf-8", newline="") as input_csv:
        reader = csv.DictReader(input_csv)
        fieldnames = list(reader.fieldnames or [])

        for new_field in ["PCS", "PCM"]:
            if new_field not in fieldnames:
                fieldnames.append(new_field)

        with NamedTemporaryFile(
            "w",
            delete=False,
            dir=BASE_DIR,
            newline="",
            encoding="utf-8",
            suffix=".csv",
        ) as temp_csv:
            writer = csv.DictWriter(temp_csv, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                pcs, pcm = score_row(row, complexity_map)
                row["PCS"] = pcs
                row["PCM"] = f"{pcm:.6f}"
                writer.writerow(row)

            temp_path = Path(temp_csv.name)

    temp_path.replace(INPUT_FILE)


def main():
    annotate_csv()
    print(f"Annotated {INPUT_FILE.name} with PCS and PCM")


if __name__ == "__main__":
    main()
