#!/usr/bin/env python3

# count_sentences.py

# count_sentences.py

# count_sentences.py
import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Use regular expression to find sentences
        sentences = re.split(r'[.!?]+', self._value)
        # Remove empty strings from the list
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
