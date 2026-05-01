"""
Course:
Python (Exercism)

Objective:
Develop functions for creating, transforming, and adding prefixes and suffixes to strings.

Notes:
- Este exercício foi fácil e acho que é porque sei o conceito de prefixos e sufixos.
- Nos exercícios com matemática preciso gastar mais tempo e energia para resolver,
o que significa que preciso estudar mais matemática para entender mais facilmente programação.
"""


# 1. Add a prefix to a word
def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


# 2. Add prefixes to word groups
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    separator = ' :: ' + prefix

    return separator.join(vocab_words)


# 3. Remove a suffix from a word
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    root = word[:-4]
    if root[-1] == 'i':
        return root[:-1] + 'y'
    return root


# 4. Extract and transform a word
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words = sentence.split()
    adjective = words[index].strip('.')
    verb = adjective + 'en'
    return verb