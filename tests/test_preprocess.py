# -*- coding: utf-8 -*-
"""Unit tests for src/preprocess.py.

Run from the repo root:  python -m unittest discover -s tests -v
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from preprocess import preprocess  # noqa: E402


class TestPreprocess(unittest.TestCase):
    def test_arabic_shaped_letters_are_mapped_to_persian(self):
        self.assertEqual(preprocess("كتاب خوب"), "کتاب خوب")

    def test_stopwords_are_removed(self):
        # "دیگران" is in dataset/stopwords.txt; "یک" is too.
        self.assertEqual(preprocess("دیگران کتاب خوبی خواندند"), "کتاب خوبی خواندند")
        self.assertEqual(preprocess("كتاب يک خوب است"), "کتاب خوب است")

    def test_digits_and_latin_characters_are_removed(self):
        self.assertEqual(preprocess("کتاب 123 خوب"), "کتاب خوب")

    def test_punctuation_is_removed(self):
        result = preprocess("کتاب (خوب) «عالی»")
        self.assertEqual(result, "کتاب خوب عالی")

    def test_empty_input_returns_empty_string(self):
        self.assertEqual(preprocess(""), "")

    def test_stemming_option_stems_tokens(self):
        # Hazm stems "کتاب‌ها" to "کتاب" (the plural suffix token stems to "").
        self.assertEqual(preprocess("کتاب‌ها", stem=True).strip(), "کتاب")

    def test_plain_sentence_is_kept(self):
        self.assertEqual(preprocess("محمد خیلی خوب و مهربان است"), "محمد خوب مهربان است")


if __name__ == "__main__":
    unittest.main()
