from collections import defaultdict

BYTE_TO_BIT = 8


class BinNode(object):
    def __init__(self):
        self.children = defaultdict()
        self.symbol = None


class PrefixCodeTree:
    def __init__(self):
        self.root = BinNode()

    def insert(self, codeword, symbol):
        temp_node = self.root
        for code in codeword:
            code = int(code)
            if code not in temp_node.children:
                temp_node.children[code] = BinNode()
            temp_node = temp_node.children[code]
        temp_node.symbol = symbol

    def decode(self, encoded_data, data_len):
        bit_counter = 0
        temp_node = self.root
        decoded_data = []

        for _byte in encoded_data:
            bit_level = BYTE_TO_BIT - 1
            while bit_level >= 0:
                bit_counter += 1

                if bit_counter > data_len:
                    break

                # get the bit at bit_level
                cur_bit = 1 if _byte & (1 << bit_level) > 0 else 0
                bit_level -= 1

                # if there's no corresponding path in the tree, the data might be corrupted, return None
                if cur_bit not in temp_node.children:
                    return None

                # move to the next corresponding node
                temp_node = temp_node.children[cur_bit]

                # if the node is leaf, receive the symbol and start over at the root
                if temp_node.symbol is not None:
                    decoded_data.append(temp_node.symbol)
                    temp_node = self.root

        if temp_node is not self.root:
            return None

        return ''.join(decoded_data)


if __name__ == '__main__':
    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }
    codeTree = PrefixCodeTree()
    for _symbol, _codeword in codebook.items():
        codeTree.insert(_codeword, _symbol)
    for _len in range(25):
        print(_len)
        print(codeTree.decode(b'\xd2\x9f\x20', _len))
