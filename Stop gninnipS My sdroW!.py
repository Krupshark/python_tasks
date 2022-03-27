def spin_words(sentence):
    words = sentence.split(' ')
    new_words = [w[::-1] if len(w) >= 5 else w for w in words]
    return ' '.join(new_words)


print(spin_words("Hey fellow warriors"))
