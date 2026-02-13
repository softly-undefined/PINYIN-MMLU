# Evaluating LLM Performance on PINYIN

## 1_data_cleaning
Cleaning process to get final data. NOTE: not totally sure if human translated or MT (I believe human translated?), more details on where I found it are in 1_data_cleaning/cleaning.ipynb

Cleaned for faulty multilingual data, and distributed equally across relevant subjects as follows (TOTAL = 500 rows):

Subcategory_ZH-PY
biology             50
history             50
physics             50
philosophy          50
math                50
health              50
business            50
economics           50
computer science    50
psychology          50

## 2_pinyin_conversion

I used pypyin to make conversions using their "lazy_pinyin" setting.
This setting doesn't include any tone markings, which reflects how many type pinyin in real-world use cases. 

Final converted data is found in 2_pinyin_conversion/mmlu_ZH-PY.csv

### NEXT STEPS

1. run inference on X models over 2_pinyin_conversion/mmlu_ZH-PY.csv
    - what models? Chinese + English centric?
        - Qwen, Llama? Gpt? Claude? Gemini?
        - we should probably compare performance on Chinese characters vs. Chinese PINYIN, Chinese non-pinyin data can be found in 2_pinyin_conversion/mmlu_EN-US_ZH-CN_ZH-PY.csv

        - (it would be really cool to use a reasoning model with a prompt to first translate to characters and then answer but probably out of scope) 

2. Evaluate Results, create graphs
    - 

3. Writeup + Present!
    - 