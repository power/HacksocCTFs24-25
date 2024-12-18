def encrypt(text, shift):
    result = []
    min_ascii, max_ascii = 32, 365  # Range of printable ASCII characters
    ascii_range = max_ascii - min_ascii + 1  # Total number of characters in this range

    for char in text:
        # Convert character to ASCII and apply the rotating shift
        ascii_value = ord(char)
        new_ascii = (ascii_value - min_ascii + shift) % ascii_range + min_ascii
        
        # Convert back to char and add to our answer
        result.append(chr(new_ascii))
        
        # Increment shift for the next character to keep rotating
        shift += 1

    return ''.join(result)

# Example usage
text = 'I thought it would be funny to mess with you and make this way longer then it needed to be. Anyway, here is your flag: hacksoc_ctf{cRACKed_iTTTtt}'
shift = 9
a = encrypt(text, shift)
print(a)
f = open("output.txt", "a", encoding="UTF-8")
f.write(a)
f.close()

