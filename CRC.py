def crc_encode(data_str, key_str):
    # Input validation
    if not set(data_str).issubset({'0', '1'}) or not set(key_str).issubset({'0', '1'}):
        raise ValueError("Inputs must contain only 0s and 1s.")

    n = len(key_str)
    # Convert binary strings to integers
    data = int(data_str, 2)
    key = int(key_str, 2)

    # Append (n - 1) zeros to the data by shifting left
    dividend = data << (n - 1)

    # Pad key alignment bit mask
    pick = len(bin(dividend)) - 2

    # Modulo-2 division using bitwise XOR
    while pick >= n:
        if (dividend >> (pick - n)) & (1 << (n - 1)):
            dividend ^= (key << (pick - n))
        pick -= 1

    # Format the remainder back to a binary string with leading zeros
    remainder = format(dividend, f'0{n - 1}b')
    return remainder, data_str + remainder


def crc_decode(received_str, key_str):
    n = len(key_str)
    received = int(received_str, 2)
    key = int(key_str, 2)

    pick = len(bin(received)) - 2
    while pick >= n:
        if (received >> (pick - n)) & (1 << (n - 1)):
            received ^= (key << (pick - n))
        pick -= 1

    return received == 0


# --- Demonstration ---
if __name__ == "__main__":
    # Sender Side
    data_input = input("Enter Data Bits: ").strip()
    key_input = input("Enter Generator Polynomial: ").strip()

    rem, codeword = crc_encode(data_input, key_input)
    print(f"\nCRC Remainder : {rem}")
    print(f"Transmitted Codeword : {codeword}")

    # Receiver Side
    received_input = input("\nEnter Received Codeword: ").strip()
    if crc_decode(received_input, key_input):
        print("No Error Detected")
    else:
        print("Error Detected")


OUTPUT:-
Enter Data Bits: 100100
Enter Generator Polynomial: 1101

CRC Remainder : 001
Transmitted Codeword : 100100001

Enter Received Codeword: 100100010
Error Detected