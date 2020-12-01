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
    nodes = freq

    while len(nodes) >= 2:
        (character1, freq1) = nodes[-1]
        (character2, freq2) = nodes[-2]
        nodes = nodes[:-2]
        node = Node(character1, character2)
        nodes.append((node, freq1 + freq2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffman_code = tree(nodes[0][0])
    return(huffman_code)

def huffman(text, separator=False):
    
    huffman_code = huffmanCode(text)    
    coded = ""

    for i in text:
        coded += huffman_code[i]
        if separator:
            coded += " "

    return coded

# Example:

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
print(text)
print(huffman(text))

print("\n")

text2 = "Lorem ipsum dolor sit amet"
# Second argument adds space between codes, if True
print(text2)
print(huffman(text2, True))