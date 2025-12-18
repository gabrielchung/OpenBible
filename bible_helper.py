import json

def get_book_index(kjv, book_name):
    try:
        return kjv["books"].index(book_name)
    except ValueError:
        return None


def get_max_chapter_num(kjv, book_name):
    book_index = get_book_index(kjv, book_name)
    if book_index is None:
        return None

    return len(kjv["content"][book_index])


def get_max_verse_num(kjv, book_name, chapter_num):
    book_index = get_book_index(kjv, book_name)
    if book_index is None:
        return None

    chapters = kjv["content"][book_index]

    if not (1 <= chapter_num <= len(chapters)):
        return None

    return len(chapters[chapter_num - 1])


def get_verse(kjv, book_name, chapter_num, verse_num):
    book_index = get_book_index(kjv, book_name)
    if book_index is None:
        return None

    chapters = kjv["content"][book_index]

    if not (1 <= chapter_num <= len(chapters)):
        return None

    verses = chapters[chapter_num - 1]

    if not (1 <= verse_num <= len(verses)):
        return None

    return verses[verse_num - 1]

def load_bible(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def build_translation_prompt(verse_text):
    return f"""You are a Bible translation assistant.

Task:
Translate the following Bible verse from Early Modern English (KJV style) into clear, natural modern English.

Rules (must follow strictly):
- Preserve the original meaning and theological sense.
- Do NOT add commentary, explanations, or interpretation.
- Do NOT include verse numbers, book names, quotation marks, or extra punctuation.
- Do NOT include any preface or suffix text.
- Output ONLY the translated verse as a single plain-text sentence or paragraph.
- Use modern grammar and vocabulary, but keep a reverent, neutral tone.

Verse:
{verse_text}
"""

def build_single_word_translation_prompt(word):
    return f"""You are a English translator.

Task:
Translate the following single word from Old English into its modern English equivalent.

Rules (must follow strictly):
- The input is exactly ONE word.
- Output exactly ONE word.
- Do NOT add explanations, notes, or alternative forms.
- Do NOT include punctuation or quotation marks.
- Preserve the original meaning as used in the Bible context.
- If the word is already modern English, output the same word unchanged.
- Use lowercase or capitalized form matching the input word.

Word:
{word}
"""


def breaking_verse_into_words_list(verse_text):
    words = verse_text.split()
    return words

if __name__ == "__main__":
    bible_file = "kjv.json"

    