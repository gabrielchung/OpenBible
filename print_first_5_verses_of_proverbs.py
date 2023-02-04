import json

proverbs_book_id = 19

with open(f'./books/{proverbs_book_id}.json', 'r') as f:
    proverbs = json.load(f)

for i in range(5):
    print(proverbs[0][i])