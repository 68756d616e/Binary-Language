# Binary Language 2 Bit 

# created by Zia, ZJHS, AKA Encrypzion, Lord Biscuit 👀
# True purpose unknown
# Additional purpose was to create a language out of binary, this is a very basic version and not the full product
# Other versions will be different and include grouping and sound

# Welcome message
print("Welcome to a 2 Bit Binary Language")

# A list of 2 bit binary conversion into text - 1 or 0 will be considered as a remainder if the sequence is odd
binary_conversion = {
    '00': 'Sa',
    '01': 'So',
    '10': 'To',
    '11': 'Ta'
}

# A looped question prompting the user to input a binary sequence
# It requests a binary input only, converts it into the text and divideds the conversion into segments of two before printing
# It will also leave a remainder, if the sequence is odd
# Error messages will display if the user inputs anything other than binary 0 or 1
while True:
    binary_input = input("Please enter a binary sequence: ")
    text_output = "" # empty
    remaining_input = "" # empty

    if not all(bit in ['0', '1'] for bit in binary_input): # There is no conversion for 0 or 1 individually
        print("Error occured: Please input a binary input with a minimum of 2 numbers.")
        continue

    if len(binary_input) < 2: # Less lan 2 # There is no conversion for anything less that 2 characters or two binary numbers
        print("Error occured: Please input a binary input with a minimum of 2 numbers.")
        continue

    if len(binary_input) % 2 == 1:
        remaining_input = binary_input[-1]
        binary_input = binary_input[:-1]

    for z in range(0, len(binary_input), 2):
        two_bits = binary_input[z:z+2]
        if two_bits not in binary_conversion:
            print(f"Error occured: Invalid bits {two_bits}")
            break
        text_output += binary_conversion[two_bits] + " "

    else:
        if len(remaining_input) > 0:
            print(f"{text_output[:-1]} , and a remainder of {remaining_input}")
        else:
            print(text_output[:-1])
