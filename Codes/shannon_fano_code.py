def shannon_fano(text):
    
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    if (len(freq) == 2):
        l = list(freq.items())
        return {0: l[0], 1: l[1]}

    elif (len(freq) == 1):
        l = list(freq.items())
        return {0: l[0]}

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    left, right = splitList(freq)

    return {0: shannon_fano(left), 1: shannon_fano(right)}

def splitList(freq_list):

    half_value = sum([frequency for _, frequency in freq_list]) / 2

    left_half = {}
    right_half = {}
    current_value = 0

    for item in freq_list:
        symbol, freq = item

        if current_value >= half_value:
            right_half[symbol] = freq
        else:
            left_half[symbol] = freq

        current_value += freq

    return left_half, right_half

def tree(dictionary, formatted={}, binary=""):

    for key, value in dictionary.items():
        if type(value) is dict:
            tree(value, formatted, binary + str(key))
        else:
            formatted[value[0]] = binary + str(key)

    return formatted

def codeInShannonFano(text, separator=False):

    codes_base = shannon_fano(text)

    shannon_fano_code = tree(codes_base)

    for i in sorted(shannon_fano_code.keys()):
        print("{} => {}".format(i, shannon_fano_code[i]))

    coded = ""

    for i in text:
        coded += shannon_fano_code[i]
        if separator:
            coded += " "

    return coded


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
print(text)
print(codeInShannonFano(text, True))
