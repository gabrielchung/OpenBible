import json
import unicodedata

with open('kjv.json', 'r', encoding='utf-8') as f:
    kjv = json.load(f)

# genesis = kjv['content'][0]

# print(genesis)
result = {}
content_result = []

for book in kjv['content']:
    curr_book = []
    for chapter in book:
        curr_chapter = []
        for verse in chapter:
            curr_verse = verse.replace(u'\u2019', "'")
            # if not curr_verse.isascii():
            #     print(curr_verse)
            curr_chapter.append(curr_verse)
        curr_book.append(curr_chapter)
    content_result.append(curr_book)

result['books'] = kjv['books']
result['content'] = content_result

# for chapter in kjv:
#     for verse in chapter:
#         curr_verse = verse.replace(u'\u2019', "'")
#         if not curr_verse.isascii():
#             print(curr_verse)

with open('kjv_ascii.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)