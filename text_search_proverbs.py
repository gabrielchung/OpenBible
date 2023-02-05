import json

proverbs_book_id = 19

with open(f'./books/{proverbs_book_id}.json', 'r') as f:
    proverbs = json.load(f)

def string_remove_all(input, remove_chars_list):
    tmp = input
    for remove_char in remove_chars_list:
        tmp = tmp.replace(remove_char, '')
    return tmp

def tokenize_verse(verse):
    punctuations_to_be_removed = ['.', ':', ',', ';']
    tmp_verse = verse
    tmp_verse = string_remove_all(tmp_verse, punctuations_to_be_removed)
    tokens = tmp_verse.split(' ')
    return tokens

def text_search(keyword):
    for c_id, chapter in enumerate(proverbs):
        for v_id, verse in enumerate(chapter):
            tokens = tokenize_verse(verse)
            if keyword in tokens:
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
    print()