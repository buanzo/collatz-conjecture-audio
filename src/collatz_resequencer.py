import numpy as np
from scipy.io import wavfile
import argparse

def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    yield 1

def main(input_file, output_file, collatz_base):
    # Load the wav file
    sample_rate, data = wavfile.read(input_file)

    # Ensure data is 1D (mono)
    if len(data.shape) > 1:
        print("This script only supports mono .wav files")
        exit(1)

    # Normalize data to a scale of 0 to 1
    data = (data.astype(np.float32) + 32768.0) / 65535.0

    # Ensure the sequence doesn't exceed the data length
    sequence = list(collatz(collatz_base))

    # Make sure that no index goes beyond the data length
    sequence = [s % len(data) for s in sequence]

    # Reorder samples according to the sequence
    reordered_data = data[sequence]

    # Rescale data back to int16 range and convert to int16
    reordered_data = (reordered_data * 65535.0 - 32768.0).astype(np.int16)

    # Write the output file
    wavfile.write(output_file, sample_rate, reordered_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Reorder .wav file samples according to the Collatz sequence.')
    parser.add_argument('input_file', type=str, help='Path to the input .wav file')
    parser.add_argument('output_file', type=str, help='Path to save the output .wav file')
    parser.add_argument('--collatz-base', type=int, default=6, help='Base number to start the Collatz sequence')
    args = parser.parse_args()

    main(args.input_file, args.output_file, args.collatz_base)
