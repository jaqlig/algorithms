def rabinKarp(text, pattern, alphabet):   

    positions = []
    position_pointer = 0

    q = 47 # any prime number for hash function

    def hash(value):
        out = 0
        for i in range(len(value)):
            out += alphabet[value[i]] * (len(alphabet)) ** abs(i-len(value)+1)
        return out % q

    def nextHash(previous_hash, removed, added):
        return ((previous_hash - alphabet[removed] * len(alphabet) ** (len(pattern)-1)) * len(alphabet) + alphabet[added]) % q


    match = list(text[0:len(pattern)])
    pointer = len(pattern)

    hashed_pattern = hash(pattern)
    hashed_match = hash(match)

    def checkMatch():
        if hashed_match == hashed_pattern:
            for i in range(len(pattern)):
                if not match[i] == pattern[i]:
                    return
            positions.append(position_pointer)
        else:
            return

    checkMatch()

    for i in range(len(text) - len(pattern)):
        position_pointer += 1
        removed = match.pop(0)
        added = text[pointer]
        match.append(text[pointer])        

        hashed_match = nextHash(hashed_match, removed, added)
        pointer += 1

        checkMatch()

    return positions

# example:

alphabet = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
text = "abghfebcaghfdhdbecabdeagdfghabdhgfcbdcdeaghfgfdhdfbabcegagdhbehgfdhgdfbace"
pattern = "deag"
print(pattern, "->", text)
print(rabinKarp(text, pattern, alphabet))
