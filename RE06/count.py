def count(word, phrase):
    counter = 0
    phrase = phrase.upper()
    word = word.upper()
    phrase_split = phrase.split()
    for word_phrase in phrase_split:
        if word_phrase == word:
            counter += 1
    return counter
