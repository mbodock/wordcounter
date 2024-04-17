import unittest

from dataclasses import dataclass

from counter.counter import count_words

@dataclass
class Case:
    name: str
    text: str
    count: int


class WordCounterTestCase(unittest.TestCase):
    inputs = [
        Case('Two spaces', ' word1   word2 ',  2),
        Case('Two words.', 'word1 word2',  2),
        Case('New line between words', 'word1\nword2',  2),
        Case('Tree words', 'word1 word2 word3',  3),
        Case('Single word', 'word1',  1),
        Case('Two emojis', '😊 😊',  2),
        Case('Two emojis with no space', '😊😊',  1),
        Case('Single emojis', '😊',  1),
        Case('Composable emoji', '\U0001F468\u200D\U0001F469\u200D\U0001F466',  1),
        Case('Hyphenated words', 'A six-pack package', 3),
        Case('Ponctuation should not be accounted', 'word1, \'word2\': word3.',  2),
        Case('Grouped foreign characters counts as a single word', 'For instance \'大きな言葉\' here.',  4),
    ]

    def test_count_words(self):
        for i in self.inputs:
            self.assertEqual(count_words(i.text), i.count, "fail on case: " + i.name)


if  __name__ == '__main__':
    unittest.main()
