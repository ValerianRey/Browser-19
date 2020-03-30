import numpy as np
import os
import re


def clean_and_tokenize(text):
    """
    Cleaning a document with:
        - Lowercase
        - Removing numbers with regular expressions
        - Removing punctuation with regular expressions
        - Removing other artifacts
    And separate the document into words by simply splitting at spaces
    Params:
        text (string): a sentence or a document
    Returns:
        tokens (list of strings): the list of tokens (word units) forming the document
    """
    # Lowercase
    text = text.lower()
    # Remove numbers
    text = re.sub(r"[0-9]+", "", text)
    # Remove punctuation
    remove_punct = re.compile("[.;:!\'?,\"()\[\]]")
    text = remove_punct.sub("", text)
    # Remove HTML artifacts specific to the corpus we're going to work with
    replace_html = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    text = replace_html.sub(" ", text)

    tokens = text.split()
    return tokens

