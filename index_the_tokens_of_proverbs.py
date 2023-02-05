import json

proverbs_book_id = 19

with open(f'./books/{proverbs_book_id}.json', 'r') as f:
    proverbs = json.load(f)

class Tokens:
    tokens_count = {}

    def __str__(self):
        return str(self.tokens_count)

    def add_tokens_list(self, tokens_list):
        for token in tokens_list:
            self.__add_token(token)

    def __add_token(self, token):
            token_count = self.tokens_count.get(token)
            if token_count == None:
                # New token in the dictionary
                new_value_of_token_count = 1
            else:
                new_value_of_token_count = token_count + 1
            self.tokens_count.update({token: new_value_of_token_count})

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

def add_tokens_from_proverbs(token_obj):
    result = []

    for c_id, chapter in enumerate(proverbs):
        for v_id, verse in enumerate(chapter):
            tokens = tokenize_verse(verse)
            token_obj.add_tokens_list(tokens)
            print(f'{c_id+1:02}:{v_id+1:02} {tokens}')
            # if keyword in tokens:
            #     print(f'{c_id+1:02}:{v_id+1:02} {verse}')
        break


def analyze_tokens():
    result = []

    for c_id, chapter in enumerate(proverbs):
        for v_id, verse in enumerate(chapter):
            tokens = tokenize_verse(verse)
            print(f'{c_id+1:02}:{v_id+1:02} {tokens}')
            # if keyword in tokens:
            #     print(f'{c_id+1:02}:{v_id+1:02} {verse}')
        break

analyze_tokens()
tokens_obj = Tokens()
add_tokens_from_proverbs(tokens_obj)
# print(tokens_obj)
# print(tokens_obj.tokens_count.items())
tokens_dictionary = tokens_obj.tokens_count
sorted_tokens_dictionary = {}
for t in sorted(tokens_dictionary, key=tokens_dictionary.get, reverse=True):
    sorted_tokens_dictionary[t] = tokens_dictionary[t]
print(sorted_tokens_dictionary)