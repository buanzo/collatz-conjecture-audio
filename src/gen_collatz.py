import numpy as np
from scipy.io import wavfile

def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    yield 1

def generate_wave(frequency, length, rate):
    t = np.linspace(0., length, rate)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

sample_rate = 44100
sequence = list(collatz(6))  # starting number is 6
waveforms = []

for number in sequence:
    freq = 440 * number  # map the number in the sequence to a frequency
    wave = generate_wave(freq, 1.0, sample_rate)
    waveforms.append(wave)

waveforms = np.concatenate(waveforms)
wavfile.write('collatz.wav', sample_rate, waveforms.astype(np.float32))
