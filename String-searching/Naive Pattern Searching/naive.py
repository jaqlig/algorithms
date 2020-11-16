def naive(text, pattern):
    positions = []

    def inner():
        for j in range(len(pattern)):
            if text[i+j] != pattern [j]:
                return
        positions.append(i)

    for i in range(len(text)):
        inner()

    return positions

# example:

text = "abghfebcaghfdhdbecabdeagdfghabdhgfcbdcdeaghfgfdhdfbabcegagdhbehgfdhgdfbace"
pattern = "deag"
print(pattern, "->", text)
print(naive(text, pattern))
