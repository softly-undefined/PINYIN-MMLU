# Evaluating LLM Performance on PINYIN

## 1_data_cleaning
Cleaning process to get final data. NOTE: not totally sure if human translated or MT (leaning human translated), more details on where I found it are in 1_data_cleaning/cleaning.ipynb

Cleaned for faulty multilingual data, and distributed equally across relevant subjects as follows (TOTAL = 850 rows):

Subcategory_ZH-PY
biology             50
history             50
politics            50
physics             50
philosophy          50
other               50
math                50
law                 50
health              50
business            50
geography           50
engineering         50
economics           50
culture             50
computer science    50
chemistry           50
psychology          50

## 2_pinyin_conversion

I used pypyin to make conversions using their "lazy_pinyin" setting.
This setting doesn't include any tone markings, which reflects how many type pinyin in real-world use cases. 

Final converted data is found in 2_pinyin_conversion/mmlu_ZH-PY.csv

### NEXT STEPS

1. run inference on X models over 2_pinyin_conversion/mmlu_ZH-PY.csv
    - is this too many examples (850)?
    - what models? Chinese + English centric?

2. Evaluate Results, create graphs, writeup
3. Present!