import string 
alphabet = list(string.ascii_lowercase)

def alpha(a, place, turns):
    
    while((place + turns) > 24):
        turns -= 24
    while((place + turns) < -24):
        turns += 24
    if (alphabet.index(a) + turns) > 24:
        return alphabet[alphabet.index(a) - turns]
    else:
        return alphabet[alphabet.index(a) + turns]

def crypt(input, turns):
    coded = ""
    x = 0
    for a in input:
        if input[x] != " ":
            coded += alpha(a, x, turns)
        else:
            coded += " "
        x += 1
    
    return coded


# Example: 

input = "abcdefghijk"
turns = 7

print(crypt(input, turns))