# imported logic from https://github.com/softly-undefined/NLP_final/blob/main/2_order_bias/order_bias.py

# === PROMPT TEMPLATE ===
QUERY_TEMPLATE = """
Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.

{Question}

A) {A}
B) {B}
C) {C}
D) {D}
""".strip()

# === EXTRACT ANSWER ===
ANSWER_PATTERN = r"(?i)Answer[ \t]*:[ \t]*\$?([A-D])\$?"

def extract_answer_from_output(text):
    if not isinstance(text, str):
        return "Error"

    # Try regex
    match = re.search(ANSWER_PATTERN, text)
    if match:
        return match.group(1).upper()

    # Fallback: check last few lines for single-letter answer
    lines = text.strip().splitlines()
    for line in reversed(lines[-5:]):
        if line.strip().upper() in ['A', 'B', 'C', 'D']:
            return line.strip().upper()

    return "Invalid"