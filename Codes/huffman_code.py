class Node():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def openNode(self):
        return (self.left, self.right)

def tree(node, binary=""):
    if type(node) is str:
        return {node: binary}

    (left, right) = node.openNode()
    dict = {}
    dict.update(tree(left, binary + "0"))
    dict.update(tree(right, binary + "1"))
    return dict

def huffmanCode(text):

    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    while len(freq) >= 2:
        (character1, freq1) = freq[-1]
        (character2, freq2) = freq[-2]
        freq = freq[:-2]
        node = Node(character1, character2)
        freq.append((node, freq1 + freq2))

        freq = sorted(freq, key=lambda x: x[1], reverse=True)

    huffman_code = tree(freq[0][0])
    return huffman_code

def codeInHuffman(text, separator=False):
    
    huffman_code = huffmanCode(text)

    for i in sorted(huffman_code.keys()):
        print("{} => {}".format(i, huffman_code[i]))

    coded = ""

    for i in text:
        coded += huffman_code[i]
        if separator:
            coded += " "

    return coded

# Example:

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
print(text)
print(codeInHuffman(text, True))
