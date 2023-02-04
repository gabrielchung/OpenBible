import json

proverbs_book_id = 19

with open(f'./books/{proverbs_book_id}.json', 'r') as f:
    proverbs = json.load(f)

def text_search(keyword):
    for c_id, chapter in enumerate(proverbs):
        for v_id, verse in enumerate(chapter):
            if keyword in verse:
                print(f'{c_id+1:02}:{v_id+1:02} {verse}')


while(True):
    keyword = input('Please insert the keyword for a Book of Proverbs search: ')
    if keyword == '':
        continue
    if keyword == 'exit()':
        break
    print(f'============================')
    print(f'Your search is : "{keyword}"')
    print(f'============================')
    print()
    print('Results:')
    text_search(keyword)