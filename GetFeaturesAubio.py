import librosa 
import stempeg
import sys
import time
import pyaudio
import aubio
import numpy as np
import sys
import os

print("Starting Code")


def aubiorun(a,rate):
    win_s = 1024                # fft size
    hop_s = win_s // 2          # hop size

    bpmlist=[]
    timelist=[]



    filename = a
    samplerate = rate

    # create aubio source
    a_source =aubio.source(filename,samplerate,hop_s)
    # a_source = aubio.source(filename, samplerate, hop_s)
    samplerate = a_source.samplerate

    # create aubio tempo detection
    a_tempo = aubio.tempo("default", win_s, hop_s, samplerate)

    # create a simple click sound
    click = 0.7 * np.sin(2. * np.pi * np.arange(hop_s) / hop_s * samplerate / 3000.)
    
    firsttime=time.time()
    previoustime=firsttime

    def pyaudio_callback(_in_data, _frame_count, _time_info, _status):
        global previoustime 
        samples, read = a_source()
        is_beat = a_tempo(samples)
        if is_beat:
            nowtime=time.time()
            bpm= 60// (nowtime-previoustime)
            bpmlist.append(str(bpm))
            previoustime= nowtime
            timelist.append(str(nowtime-firsttime))
            #print(bpm," ",nowtime-firsttime)
            #print ('tick') # avoid print in audio callback
        audiobuf = samples.tobytes()
        if read < hop_s:
            return (audiobuf, pyaudio.paComplete)
        return (audiobuf, pyaudio.paContinue)

    # create pyaudio stream with frames_per_buffer=hop_s and format=paFloat32
    p = pyaudio.PyAudio()
    pyaudio_format = pyaudio.paFloat32
    frames_per_buffer = hop_s
    n_channels = 1
    stream = p.open(format=pyaudio_format, channels=n_channels, rate=samplerate,
            output=True, frames_per_buffer=frames_per_buffer,
            stream_callback=pyaudio_callback)

    # start pyaudio stream
    stream.start_stream()

    # wait for stream to finish
    while stream.is_active():
        time.sleep(0.1)

    # stop pyaudio stream
    stream.stop_stream()
    stream.close()
    # close pyaudio
    p.terminate()
    return bpmlist,timelist


 
def makedataset(a):

    filename=a
    path ="C:/Users/ROG/Downloads/musdb18/Tempwav/"     
    path2 ="C:/Users/ROG/Downloads/musdb18/Temp/"
    filepath= "C:/Users/ROG/Downloads/musdb18/train/" +filename+".mp4"
    print(filepath)
    S, rate = stempeg.read_stems(filepath)

    librosa.output.write_wav(path + '0.wav', S[0].T, rate)
    librosa.output.write_wav(path + '1.wav', S[1].T, rate)
    librosa.output.write_wav(path + '2.wav', S[2].T, rate)
    librosa.output.write_wav(path + '3.wav', S[3].T, rate)
    librosa.output.write_wav(path + '4.wav', S[4].T, rate)
    print("Temporary wav files Created")



    col1,col2=aubiorun(path +'0.wav',rate)
    print("part 0 done")
    col3,col4=aubiorun(path +'1.wav',rate)
    print("part 1 done")
    col5,col6=aubiorun(path +'2.wav',rate)
    print("part 2 done")
    col7,col8=aubiorun(path +'3.wav',rate)
    print("part 3 done")
    col9,col10=aubiorun(path +'4.wav',rate)
    print("part 4 done")


    savepath= path2+filename+"0bpm.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col1))

    savepath= path2+filename+"0time.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col2))

    savepath= path2+filename+"1bpm.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col3))

    savepath= path2+filename+"1time.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col4))
        
    savepath= path2+filename+"2bpm.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col5))

    savepath= path2+filename+"2time.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col6))

    savepath= path2+filename+"3bpm.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col7))

    savepath= path2+filename+"3time.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col8))

    savepath= path2+filename+"4bpm.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col9))

    savepath= path2+filename+"4time.txt"
    with open(savepath, "w") as outfile:
        outfile.write(",".join(col10))
        
    os.remove(path +'0.wav')
    os.remove(path +'1.wav')
    os.remove(path +'2.wav')
    os.remove(path +'3.wav')
    os.remove(path +'4.wav')
    print("Temporary wav files Deleted")
    
    

import os
txtfile= 'C:/Users/ROG/Downloads/musdb18/list2.txt'
with open(txtfile) as f:
    lines = f.read().splitlines() 
for i in lines:
    makedataset(i)
