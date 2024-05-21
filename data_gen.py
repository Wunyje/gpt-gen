# Open a binary file for writing
with open('data_test.bin', 'wb') as file:
    # Generate 256 segments of 32 bytes each
    for i in range(1, 257):
        # Convert the integer to a 256-bit binary representation
        data = i.to_bytes(32, 'big')
        # Write the binary data to the file
        file.write(data)

print("Binary file created successfully.")
