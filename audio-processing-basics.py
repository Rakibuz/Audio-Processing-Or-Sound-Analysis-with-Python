import wave

#Audio signal parameters

#-- number of channels
#- sample width
#-- Frame Rate/ sample rate    44,100 Hz
#-- number of frames
#--- value of a frame 

obj =wave.open("sample.wav", "rb")

print("Number of Channels",obj.getnchannels())
print("Width",obj.getsampwidth())
print("Frame Rate",obj.getframerate())
print("Number of Frames",obj.getnframes())

print("Parameters",obj.getparams())


# wav file time duration calculation
t_audio=obj.getnframes()/obj.getframerate()
print(t_audio)


frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))
print(len(frames)/2)

obj.close()


obj_new = wave.open("sample_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(8000)

obj_new.writeframes(frames)

obj_new.close()