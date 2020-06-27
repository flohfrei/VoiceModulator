import wave
import struct
import random
import math

with wave.open('/home/user1/projects/VoiceModulator/testfile2.wav','wb') as wfile:
    sampleRate=44100.0 #hertz
    duration=4.0 #seconds
    frequency = 440.0 #hertz
    wfile.setnchannels(1)
    wfile.setsampwidth(2)
    wfile.setframerate(sampleRate)
    #white noise
    # for i in range(99999):
    #     val = random.randint(-32767,32767)
    #     data = struct.pack('<h',val)
    #     wfile.writeframesraw(data)

# ding_wav = wave.open(fname, 'rb')
# ding_data = ding_wav.readframes(ding_wav.getnframes())
# audio = pyaudio.PyAudio()
# stream_out = audio.open(
#     format=audio.get_format_from_width(ding_wav.getsampwidth()),
#     channels=ding_wav.getnchannels(),
#     rate=ding_wav.getframerate(), input=False, output=True)
# stream_out.start_stream()
# stream_out.write(ding_data)
# time.sleep(0.2)
# stream_out.stop_stream()
# stream_out.close()
# audio.terminate()

# import wave, struct, math, random
# sampleRate = 44100.0 # hertz
# duration = 1.0 # seconds
# frequency = 440.0 # hertz
# obj = wave.open('sound.wav','w')
# obj.setnchannels(1) # mono
# obj.setsampwidth(2)
# obj.setframerate(sampleRate)
# for i in range(99999):
#    value = random.randint(-32767, 32767)
#    data = struct.pack('<h', value)
#    obj.writeframesraw( data )
# obj.close()
