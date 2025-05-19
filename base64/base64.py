BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+="

def encode():
    global BASE64
    
    usr_in = input("String to encode: ")
    
    bin_chars = ""; encoded = ""
    
    for char in usr_in:
        a = str(bin(ord(char))).replace("0b", "")
        
        if len(a) < 8:
            lenDiff = 8 - len(a); zeroes = ""
            for _ in range(lenDiff): zeroes += "0"
            a = zeroes + a
        
        bin_chars += a
        
    start = 0; s = 0; bits = len(bin_chars)
    
    for end in range(24, bits + 1, 24):
        for e in range(6, 24 + 1, 6):
            encoded += BASE64[int(bin_chars[start:end][s:e], 2)]
            s = e
        start = end; s = 0
        
    print(bin_chars)
    
    if end != bits:
        misssing_bits = bits - end; s = 0
        bits_needed = 0; last_bits = bin_chars[end:bits]
        
        print(misssing_bits)
        
        while ((misssing_bits + bits_needed) % 6) != 0: bits_needed += 1; last_bits += "0"
        
        for e in range(6, len(last_bits) + 1, 6):
            encoded += BASE64[int(last_bits[s:e], 2)]
            s = e

            encoded += BASE64[-1] * (((misssing_bits + bits_needed) // 6) - (misssing_bits // 6))
            
        
    print(encoded)

def decode():
    pass

def main():
    mode = input("Select one of two modes (e/d): ").lower()

    match mode:
        case "e": encode()
        case "d": decode()
        case _: pass

if __name__ == "__main__":
    main()