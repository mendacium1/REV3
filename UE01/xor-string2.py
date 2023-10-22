def xor_string(input_str, hex_key):
    """
    Perform an XOR operation on the input string with a multi-byte key represented in hexadecimal.

    :param input_str: string, the input text to be XORed
    :param hex_key: string, key in hexadecimal used for XOR operation
    :return: bytes, the result of the XOR operation as a bytes object
    """
    # Convert the hex key to a bytes object
    try:
        key_bytes = bytes.fromhex(hex_key)
    except ValueError:
        raise ValueError("Invalid hexadecimal key. Hexadecimal key must be a valid sequence of bytes.")

    # Ensure the key is not empty
    if not key_bytes:
        raise ValueError("Key cannot be empty.")

    # Convert the input string to bytes
    input_bytes = input_str.encode('utf-8')

    # Perform the XOR operation
    xor_result = bytes(input_byte ^ key_bytes[i % len(key_bytes)] for i, input_byte in enumerate(input_bytes))

    return xor_result

def main():
    # Prompt user for the input string
    input_str = input("Enter the string to XOR: ")

    # Prompt user for the key in hexadecimal format
    hex_key = input("Enter the XOR key in hexadecimal format: ")

    # Check for empty input string
    if not input_str:
        print("Error: String cannot be empty!")
        return

    # Perform XOR operation on the input string
    try:
        xor_result = xor_string(input_str, hex_key)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Print the XOR result in hexadecimal format
    print("\nXOR Result (in hex):", xor_result.hex())

    # Demonstrating the reverse of the operation with the same hex_key
    try:
        original_str = xor_string(xor_result.decode('ISO-8859-1'), hex_key).decode('utf-8')
    except UnicodeDecodeError:
        print("Error: Cannot decode the result. The XOR operation might have produced non-UTF-8 bytes.")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("Original string after reverse XOR:", original_str)

# Run the script
if __name__ == "__main__":
    main()

