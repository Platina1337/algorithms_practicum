def huffman_decode():
    # Входные данные
    n, size = 12, 60
    codes = {
        ' ': '1011', '.': '1110', 'D': '1000',
        'c': '000', 'd': '001', 'e': '1001',
        'i': '010', 'm': '1100', 'n': '1010',
        'o': '1111', 's': '011', 'u': '1101'
    }
    encoded = "100011110001001101000111111011001010011000010110011010111110"

    # Создаем словарь для декодирования
    decode_dict = {code: char for char, code in codes.items()}
    
    # Декодируем строку
    current_code = ""
    decoded = ""
    
    for bit in encoded:
        current_code += bit
        if current_code in decode_dict:
            decoded += decode_dict[current_code]
            current_code = ""
    
    print(decoded)

if __name__ == "__main__":
    huffman_decode()
