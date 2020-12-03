import string 
alphabet = list(string.ascii_lowercase)

def alpha(character, turns):
    
    while((turns) > 25):
        turns -= 26
    while((turns) < -25):
        turns += 26
    if (alphabet.index(character) + turns) > 25:
        return alphabet[alphabet.index(character) + turns - 26]
    else:
        return alphabet[alphabet.index(character) + turns]


def code(input, turns):
    coded = ""
    x = 0
    for character in input:
        if input[x] != " ":
            coded += alpha(character, turns)
        else:
            coded += " "
        x += 1
    return coded

# Example:

input = "abcdefghijklmnopqrstuvwxyz"
turns = 2
print(input, "->")
print(code(input, turns))