from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Lexical categories that should count as a word.
# Short list available at https://www.nltk.org/book/ch05.html#tab-universal-tagset
# for a complete list check nltk.help.upenn_tagset().
IGNORED_CATEGORIES = (
    'SYM', '$', '\'\'', '(', ')', ',', '--', '.', ':',
    'POS',  # ignore genitive markers
)

def count_words(text: str) -> int:
    """Counts the number of words in text.

    Note:
        It assumes that the text is in English and the required models are
        accessible to NLTK[1].

    1 - https://www.nltk.org/data.html
    """
    tokens = word_tokenize(text)
    tags = pos_tag(tokens)
    count = 0
    for t in tags:
        if t[1] not in IGNORED_CATEGORIES:
            count +=1
    return count
