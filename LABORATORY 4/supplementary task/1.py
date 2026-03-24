def word_filter(sentence, bad_words):
    words = sentence.split()
    filtered = []
    for w in words:
        if w.lower() in [bw.lower() for bw in bad_words]:
            filtered.append('*' * len(w))
        else:
            filtered.append(w)
    return ' '.join(filtered)

# Example
print(word_filter("This is a bad example", ["bad"]))
# Output: This is a *** example
