# -*- coding: utf-8 -*-
"""
Persian text preprocessing for the sentiment-analysis pipeline.

Extracted from src/persian-sentiment-analysis.py so the cleaning logic can
be tested and reused on its own. The behaviour is unchanged: Arabic-shaped
letters are mapped to Persian ones, punctuation and non-Persian characters
are stripped, Hazm normalizes the text, and stopwords are dropped
(optionally with stemming).

Author: Mohammad Abbasi
GitHub: https://github.com/mohammad-abbasi-sh/persian-sentiment-analysis
"""

import re
from pathlib import Path

from hazm import Normalizer, Stemmer, word_tokenize

__all__ = ["preprocess", "load_stopwords", "TEXT_CLEANING_RE"]

# Keep only Persian letters (used after normalization).
TEXT_CLEANING_RE = r"[^آ-ی]"


def load_stopwords(path=None):
    """Load the stopwords list.

    Defaults to ``dataset/stopwords.txt`` at the repo root, resolved
    relative to this file so it works no matter where the caller runs from.
    """
    if path is None:
        path = Path(__file__).resolve().parent.parent / "dataset" / "stopwords.txt"
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


stopwords = load_stopwords()

normalizer = Normalizer()
stemmer = Stemmer()


def preprocess(text, stem=False):
    text = text.replace('.', ' ')
    text = text.replace('ي', 'ی').replace('ك', 'ک')
    text = text.replace("-", "")
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace("«", " ")
    text = text.replace("»", " ")
    text = normalizer.normalize(text)
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text)).strip()  # remove all character except farsi character

    tokens = []
    # for token in text.split():
    for token in word_tokenize(text):
        if token not in stopwords:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)
