import pyaudio
import wave

import os
directory = os.path.dirname(os.path.abspath(__file__))
print(directory)

# Set up audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = os.path.join(directory, "output.wav")

# Create PyAudio object
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording audio...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording audio.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
p.terminate()

# Save recorded audio to WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Recorded audio saved to: {WAVE_OUTPUT_FILENAME}")

