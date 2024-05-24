def main():
    # Generate xdma_data_write.bin
    with open('xdma_data_write.bin', 'wb') as f:
        for i in range(1, 257):
            # Convert the integer to a 256-bit binary representation in little-endian format
            data = (i).to_bytes(32, byteorder='little')
            f.write(data)

    # Generate xdma_write_down.bin
    with open('xdma_write_down.bin', 'wb') as f:
        # Write 32 bytes of 0xff
        data = b'\xff' * 32
        f.write(data)

if __name__ == "__main__":
    main()
