def boyer_moore(text, pattern):
    positions = []
    i = len(pattern)-1

    # last indexes of every character in pattern, you can also use rfind()
    array = []
    array[:0] = pattern
    array.reverse()
    last = {}
    for z in pattern:
        if z in last:
            continue       
        last.update({z: len(pattern) - array.index(z)-1})

    while(i < len(text)):
        if(text[i] == pattern[-1]): # match on the last position
            match = 1
            j = i - 1
            for x in range(len(pattern)-1):
                if text[j] != pattern[j-i-1]:

                    match = 0
                    break
                else:
                    j -= 1
                    continue
            i += 1
            if match == 0:
                continue
            positions.append(i-len(pattern))

        
        elif not (text[i] in pattern): # no text[i] in pattern
            i += len(pattern)
        
        else: # there is text[i] in pattern
            i += len(pattern) - last[text[i]] - 1
    return positions

#example

text = "abghfebcaghfdhdbecabdeagdfghabdhgfcbdcdeaghfgfdhdfbabcegagdhbehgfdhgdfbace"
pattern = "deag"
print(pattern, "->", text)
print(boyer_moore(text, pattern))
