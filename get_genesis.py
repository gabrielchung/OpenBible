import json
import unicodedata

with open('kjv_ascii.json', 'r') as f:
    kjv = json.load(f)

genesis = kjv['content'][0]

result = []

for chapter in genesis:
    curr_chapter = []
    for verse in chapter:
        curr_chapter.append(verse)
    result.append(curr_chapter)

with open('kjv_genesis.json', 'w') as f:
    json.dump(result, f, indent=4)