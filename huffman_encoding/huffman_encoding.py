from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = Node(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)
    
    return heap[0]

def build_codes(root, code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = code
        return
    build_codes(root.left, code + "0", codes)
    build_codes(root.right, code + "1", codes)
    return codes

def huffman_encode():
    text = "Errare humanum est."
    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded = "".join(codes[char] for char in text)
    
    print(f"{len(codes)} {len(encoded)}")
    for char in sorted(codes.keys()):
        print(f"'{char}': {codes[char]}")
    print(encoded)

if __name__ == "__main__":
    huffman_encode()
