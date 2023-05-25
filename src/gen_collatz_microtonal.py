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

def microtonal_freq(base_freq, step, ratio):
    return base_freq * np.power(ratio, step)

sample_rate = 44100
sequence = list(collatz(6))  # starting number is 6
waveforms = []

for number in sequence:
    freq = microtonal_freq(220, number, 1.01)  # map the number in the sequence to a frequency on a microtonal scale
    wave = generate_wave(freq, 1.0, sample_rate)
    waveforms.append(wave)

waveforms = np.concatenate(waveforms)
wavfile.write('collatz_microtonal.wav', sample_rate, waveforms.astype(np.float32))
