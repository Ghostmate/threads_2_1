def single_root_words(root_word, *other_words):
    same_words = list()
    root_word = root_word.lower()
    for k in other_words:
        d = k.lower()
        if d in root_word:
            root_word = d

    for k in other_words:
        d = k.lower()
        if root_word in d:
            same_words.append(k)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)