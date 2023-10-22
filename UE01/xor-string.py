def xor_string(input_str, key_byte):
    """
    Perform an XOR operation on each byte of the input string with the key_byte.

    :param input_str: string, the input text to be XORed
    :param key_byte: int, a single-byte key (0-255) to XOR with each byte of the input_str
    :return: bytes, the result of the XOR operation as a bytes object
    """
    # Ensure the key is a single byte
    if not 0 <= key_byte <= 255:
        raise ValueError("key_byte must be in range(256) (i.e., 0 through 255)")

    # Convert the string to bytes
    input_bytes = input_str.encode('utf-8')

    # Perform the XOR operation
    xor_result = bytes(byte ^ key_byte for byte in input_bytes)

    return xor_result

def main():
    # Prompt user for the input string
    input_str = input("Enter the string to XOR: ")

    # The XOR key byte is fixed as 0x96 for each character in this example
    key_byte = 0x96

    # Check for empty input
    if not input_str:
        print("Error: String cannot be empty!")
        return

    # Perform XOR operation on the input string
    xor_result = xor_string(input_str, key_byte)

    # Print the XOR result in hexadecimal
    # Since the result can contain non-ASCII characters, we display it in hex
    print("\nXOR Result (in hex):", xor_result.hex())

    # Demonstrating that you can reverse the operation with the same key_byte
    # We need to ensure we interpret the XOR'ed bytes without considering them as UTF-8 or any encoding
    original_bytes = bytes(byte ^ key_byte for byte in xor_result)

    try:
        # Try to decode the original bytes using utf-8 encoding
        original_str = original_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # If decoding fails, the original text might have had characters outside utf-8
        # In such a case, it's not always possible to get the original text accurately
        print("Error: Cannot decode using utf-8, the original string might have characters outside utf-8 encoding.")
        return

    print("Original string after reverse XOR:", original_str)

# Run the script
if __name__ == "__main__":
    main()

