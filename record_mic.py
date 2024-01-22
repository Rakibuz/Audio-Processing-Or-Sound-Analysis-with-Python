import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNENLS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    
    format =FORMAT,
    channels=CHANNENLS,
    rate=RATE,
    input =True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Start Recording")
seconds=5
frames=[]
for i in range(0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    data=stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.start_stream()
stream.close()
p.terminate()

obj=wave.open("output.wav","wb")
obj.setnchannels(CHANNENLS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
