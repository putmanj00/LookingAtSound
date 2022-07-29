import pyaudio
import wave
FORMAT = pyaudio.paInt16
CHANNELS = 2
SAMPLE_RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "test19.wav"
audio = pyaudio.PyAudio()
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=SAMPLE_RATE, input=True,
                    frames_per_buffer=CHUNK)
print("Recording...")
frames = []
for i in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Finished Recording!")
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(SAMPLE_RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()