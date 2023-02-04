import json
import unicodedata

with open('kjv_ascii.json', 'r') as f:
    kjv = json.load(f)

books = kjv['books']
# print(books)

for i in range(66):
    print(f'{i} - {books[i]}')

    book_content = kjv['content'][i]

    result = []

    for chapter in book_content:
        curr_chapter = []
        for verse in chapter:
            curr_chapter.append(verse)
        result.append(curr_chapter)

    # with open(f'./books/{i:02}_kjv_{books[i]}.json', 'w') as f:
    with open(f'./books/{i:02}.json', 'w') as f:
        json.dump(result, f, indent=4)