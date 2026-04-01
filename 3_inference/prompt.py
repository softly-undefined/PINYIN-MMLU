# imported logic from https://github.com/softly-undefined/NLP_final/blob/main/2_order_bias/order_bias.py
import re


# === PROMPT TEMPLATES (one per language) ===

QUERY_TEMPLATE_EN = """
Answer the following multiple choice question. The last line of your response should be of the following format: 'Answer: $LETTER' (without quotes) where LETTER is one of ABCD. Think step by step before answering.

{Question}

A) {A}
B) {B}
C) {C}
D) {D}
""".strip()

QUERY_TEMPLATE_ZH = """
回答以下选择题。你的回答的最后一行应采用以下格式：'Answer: $LETTER'（不含引号），其中 LETTER 是 ABCD 之一。请在回答之前逐步思考。

{Question}

A) {A}
B) {B}
C) {C}
D) {D}
""".strip()

QUERY_TEMPLATE_PY = """
hui da yi xia xuan ze ti 。 ni de hui da de zui hou yi hang ying cai yong yi xia ge shi ： 'Answer: $LETTER' （ bu han yin hao ）， qi zhong LETTER shi ABCD zhi yi 。 qing zai hui da zhi qian zhu bu si kao 。

{Question}

A) {A}
B) {B}
C) {C}
D) {D}
""".strip()

PROMPT_TEMPLATES = {
    "en": QUERY_TEMPLATE_EN,
    "zh": QUERY_TEMPLATE_ZH,
    "py": QUERY_TEMPLATE_PY,
}

# Keep backward compat alias
QUERY_TEMPLATE = QUERY_TEMPLATE_EN


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
