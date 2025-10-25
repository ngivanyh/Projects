BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PADDING = "="

def encode():
    usr_in = input("String to encode (UTF-8 encoding): ")
    
    bin_chars = ""; encoded = ""

    for byte in bytes(usr_in, "utf-8"):
        c = bin(byte).replace("0b", "").zfill(8)
        
        bin_chars += c

    start, s = 0, 0; bits = len(bin_chars); end = 0

    for end in range(24, bits + 1, 24):
        for e in range(6, 24 + 1, 6):
            encoded += BASE64[int(bin_chars[start:end][s:e], 2)]
            s = e
        start = end; s = 0

    if end != bits:
        missing_bits = bits - end; s = 0
        last_bits = bin_chars[end:bits]
                
        while (len(last_bits) % 6) != 0: last_bits += "0"
        
        for e in range(6, len(last_bits) + 1, 6):
            encoded += BASE64[int(last_bits[s:e], 2)]
            s = e

        encoded += PADDING * (3 - missing_bits // 8)

    print(encoded)

def decode():
    usr_in = input("String to decode (UTF-8 encoding): ")
    padding = usr_in.count("="); usr_in = usr_in.replace("=", "")
    
    print(padding, usr_in)
    

def main():
    mode = input("Select one of two modes (e/d): ").lower()

    match mode:
        case "e": encode()
        case "d": decode()
        case _: pass

if __name__ == "__main__":
    main()