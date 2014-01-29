#!/usr/bin/env python

from Tkinter import *
from record import*
import wave, struct, Tkinter
import tkFileDialog
import sys
import pyaudio

from wavefile import*

selectedFile = ['','','']
p1 = 0
p2 = 0
p3 = 0

window = Tk()

window.geometry('1100x740+200+0')
window.title('Wave Mixer')

play1Var = IntVar()
play2Var = IntVar()
play3Var = IntVar()

check1 = IntVar() 
check2 = IntVar()
check3 = IntVar()

amp1 = IntVar()
tShift1 = DoubleVar()
tScale1 = IntVar()

check4 = IntVar() 
check5 = IntVar()
check6 = IntVar()

amp2 = IntVar()
tShift2 = DoubleVar()
tScale2 = IntVar()

check7 = IntVar() 
check8 = IntVar()
check9 = IntVar()

amp3 = IntVar()
tShift3 = DoubleVar()
tScale3 = IntVar()



def play1():
    global p1    
    global play1Var
    if p1 is 1:
        p1 = 0
    
    if selectedFile[0] is not '':
        wave1 = wave_mixture(selectedFile[0])
        
        #print 'time scale factor: ',tScale1.get()
       
        if amp1.get() is not 0:
            wave1.ampScaling(amp1.get()) 
            wave1.data = wave1.scaledData

        if tShift1.get() is not 0:
            wave1.timShifting(tShift1.get()) 
            wave1.data = wave1.shiftedData
            wave1.length = wave1.new_length

        if tScale1.get() is not 0:
            wave1.timScaling(tScale1.get()) 
            wave1.data = wave1.tscaledData
            wave1.length = wave1.new_length

        if check1.get() is 1:
            wave1.timReversal() 
            wave1.data = wave1.rev_data
        
        wave1.write1('new1.wav')

        chunk = 1024
        wavFile = wave.open('new1.wav','rb')
        
        player = pyaudio.PyAudio()

        stream = player.open(format = player.get_format_from_width(wavFile.getsampwidth()),channels=wavFile.getnchannels(),rate = wavFile.getframerate(),output = True)

        data = wavFile.readframes(chunk)


        while data is not '' and p1 is 0:
            stream.write(data)
            data = wavFile.readframes(chunk)

        stream.stop_stream()
        stream.close()
        player.terminate()
    else:
        print 'Please Select the 1st wave file'

    return

def play2():
    global p2
    global play2Var
    if p2 is 1:
        p2 = 0
    
    if selectedFile[1] is not '':
        wave2 = wave_mixture(selectedFile[1])


        #print 'time scale factor: ',tScale2.get()
        
        if amp2.get() is not 0:
            wave2.ampScaling(amp2.get()) 
            wave2.data = wave2.scaledData

        if tShift2.get() is not 0:
            wave2.timShifting(tShift2.get()) 
            wave2.data = wave2.shiftedData
            wave2.length = wave2.new_length

        if tScale2.get() is not 0:
            wave2.timScaling(tScale2.get()) 
            wave2.data = wave1.tscaledData
            wave2.length = wave2.new_length

        if check4.get() is 1:
            wave2.timReversal() 
            wave2.data = wave2.rev_data

        wave2.write1('new2.wav')
        
        chunk = 1024
        wavFile = wave.open('new2.wav','rb')

        player = pyaudio.PyAudio()

        stream = player.open(format = player.get_format_from_width(wavFile.getsampwidth()),channels=wavFile.getnchannels(),rate = wavFile.getframerate(),output = True)

        data = wavFile.readframes(chunk)

        while data is not '' and p2 is 0:
            stream.write(data)
            data = wavFile.readframes(chunk)

        stream.stop_stream()
        stream.close()

        player.terminate()

    else:
        print 'Please Select the 2nd wave file'

    return

def play3():
    global p3
    global play3Var
    if p3 is 1:
        p3 = 0
    
    if selectedFile[2] is not '':
        wave3 = wave_mixture(selectedFile[2])
       
        #print 'time scale factor: ',tScale3.get()
 
        if amp3.get() is not 0:
            wave3.ampScaling(amp3.get()) 
            wave3.data = wave3.scaledData

        if tShift3.get() is not 0:
            wave3.timShifting(tShift3.get()) 
            wave3.data = wave3.shiftedData
            wave3.length = wave3.new_length

        if tScale3.get() is not 0:
            wave3.timScaling(tScale3.get()) 
            wave3.data = wave3.tscaledData
            wave3.length = wave3.new_length
        
        if check7.get() is 1:
            wave3.timReversal() 
            wave3.data = wave3.rev_data

        wave3.write1('new3.wav')

        chunk = 1024
        wavFile = wave.open('new3.wav','rb')

        player = pyaudio.PyAudio()

        stream = player.open(format = player.get_format_from_width(wavFile.getsampwidth()),channels=wavFile.getnchannels(),rate = wavFile.getframerate(),output = True)

        data = wavFile.readframes(chunk)

        while data is not '' and p3 is 0:
            stream.write(data)
            data = wavFile.readframes(chunk)

        stream.stop_stream()
        stream.close()

        player.terminate()

    else:
        print 'Please Select the 3rd wave file'

    return



def pause1():
    global p1
    p1 = 1
    return

def pause2():
    global p2
    p2 = 1
    return

def pause3():
    global p3
    p3 = 1
    return

def mute():
    return;


def Open1() :
    global newfile1
    newfile1 = tkFileDialog.askopenfilename()
    newf = newfile1.split('/')[-1]
    wave1Label2 = Label(frame1, text= newf).grid(row=1, column=0, sticky = 'E')
    selectedFile[0] = newfile1

def Open2() :
    global newfile2
    newfile2 = tkFileDialog.askopenfilename()
    newf = newfile2.split('/')[-1]
    wave2Label2 = Label(frame2, text= newf).grid(row=1, column=0, sticky = 'E')
    selectedFile[1] = newfile2

def Open3() :
    global newfile3
    newfile3 = tkFileDialog.askopenfilename()
    newf = newfile3.split('/')[-1]
    wave3Label2 = Label(frame3, text= newf).grid(row=1, column=0, sticky = 'E')
    selectedFile[2] = newfile3


'''Upper Frame'''
frame_up = Frame(window)
frame_up.pack(side = TOP)

'''Lower Frame'''
frame_down = Frame(window)
frame_down.pack(side = TOP)

'''Bottom Frame'''
frame_record = Frame(window)
frame_record.pack(side = TOP)



'''Left Frame'''
frame1 = Frame(frame_up, bd = 5)
frame1.pack(side = LEFT)




wave1Label1 = Label(frame1, text = 'Wave1')
openFile1Butt = Button(frame1, text = "Select File", command = Open1)
wave1Check1 = Checkbutton(frame1, text='Time Reversal', variable=check1, onvalue = 1, offvalue = 0)
wave1Check2 = Checkbutton(frame1, text='Select for Modulation', variable=check2, onvalue = 1, offvalue = 0)
wave1Check3 = Checkbutton(frame1, text='Select for Mixing', variable=check3, onvalue = 1, offvalue = 0)
wave1SliderL1 = Label(frame1, text='Amplitude')
wave1Slider1 = Scale(frame1, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 1, variable = amp1, to = 5)
wave1SliderL2 = Label(frame1, text='Time Shift')
wave1Slider2 = Scale(frame1, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 0.5, resolution = 0.5, variable = tShift1, from_ = -1.0, to = 1.0)
wave1SliderL3 = Label(frame1, text='Time Scaling')
wave1Slider3 = Scale(frame1, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 2, resolution = 2, variable = tScale1, from_ = -8, to = 8)

wave1Play = Scale(frame1, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, variable = play1Var, to = 100000)
playbutton1 = Button(frame1, text='Play', command=play1, state = 'active')
pausebutton1 = Button(frame1, text='Pause', command=pause1, state = 'active')
mutebutton1 = Button(frame1, text='Mute', command=mute)

wave1Label1.grid(row=0, column=0, sticky = 'W')
openFile1Butt.grid(row=1, column=0, sticky = 'W', columnspan = 2)
wave1SliderL1.grid(row=2, column=0)
wave1Slider1.grid(row=3, column=0) 
wave1SliderL2.grid(row=4, column=0) 
wave1Slider2.grid(row=5, column=0) 
wave1SliderL3.grid(row=6, column=0)
wave1Slider3.grid(row=7, column=0) 
wave1Check1.grid(row=8, column = 0, sticky = 'W')
wave1Check2.grid(row=9, column = 0, sticky = 'W')
wave1Check3.grid(row=10, column = 0, sticky = 'W')
playbutton1.grid(row =11, column = 0, columnspan = 3 )
#pausebutton1.grid(row =11, column = 0, columnspan = 3)
#mutebutton1.grid(row =11, column = 0, columnspan = 3, sticky = 'E')
wave1Play.grid(row =12, column = 0)

'''Middle Frame'''
frame2 = Frame(frame_up, bd=5)
frame2.pack(side = LEFT)


wave2Label1 = Label(frame2, text = 'Wave2')
openFile2Butt = Button(frame2, text = "Select File", command = Open2)
wave2Check1 = Checkbutton(frame2, text='Time Reversal', variable=check4, onvalue = 1, offvalue = 0)
wave2Check2 = Checkbutton(frame2, text='Select for Modulation', variable=check5, onvalue = 1, offvalue = 0)
wave2Check3 = Checkbutton(frame2, text='Select for Mixing', variable=check6, onvalue = 1, offvalue = 0)
wave2SliderL1 = Label(frame2, text='Amplitude')
wave2Slider1 = Scale(frame2, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 1, variable = amp2, to = 5)
wave2SliderL2 = Label(frame2, text='Time Shift')
wave2Slider2 = Scale(frame2, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 0.5, resolution = 0.5, variable = tShift2, from_=-1.0, to = 1.0)
wave2SliderL3 = Label(frame2, text='Time Scaling')
wave2Slider3 = Scale(frame2, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 2, resolution = 2, variable = tScale2,from_ = -8, to = 8)

wave2Play = Scale(frame2, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, variable = play2Var)
playbutton2 = Button(frame2, text='Play', command=play2, state = 'active')
pausebutton2 = Button(frame2, text='Pause', command=pause2, state = 'active')
mutebutton2 = Button(frame2, text='Mute', command=mute)

wave2Label1.grid(row=0, column=0, sticky = 'W')
openFile2Butt.grid(row=1, column=0, sticky = 'W', columnspan = 2)
wave2SliderL1.grid(row=2, column=0)
wave2Slider1.grid(row=3, column=0) 
wave2SliderL2.grid(row=4, column=0) 
wave2Slider2.grid(row=5, column=0) 
wave2SliderL3.grid(row=6, column=0)
wave2Slider3.grid(row=7, column=0) 
wave2Check1.grid(row=8, column = 0, sticky = 'W')
wave2Check2.grid(row=9, column = 0, sticky = 'W')
wave2Check3.grid(row=10, column = 0, sticky = 'W')
playbutton2.grid(row =11, column = 0, columnspan = 3)
#pausebutton2.grid(row =11, column = 0, columnspan = 3)
#mutebutton2.grid(row =11, column = 0, columnspan = 3, sticky = 'E')
wave2Play.grid(row =12, column = 0)

'''Right Frame'''
frame3 = Frame(frame_up, bd=5)
frame3.pack(side = LEFT)


wave3Label1 = Label(frame3, text = 'Wave3')
openFile3Butt = Button(frame3, text = "Select File", command = Open3)
wave3Check1 = Checkbutton(frame3, text='Time Reversal', variable=check7, onvalue = 1, offvalue = 0)
wave3Check2 = Checkbutton(frame3, text='Select for Modulation', variable=check8, onvalue = 1, offvalue = 0)
wave3Check3 = Checkbutton(frame3, text='Select for Mixing', variable=check9, onvalue = 1, offvalue = 0)
wave3SliderL1 = Label(frame3, text='Amplitude')
wave3Slider1 = Scale(frame3, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 1, variable = amp3, to = 5)
wave3SliderL2 = Label(frame3, text='Time Shift')
wave3Slider2 = Scale(frame3, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 0.5, resolution = 0.5, variable = tShift3, from_ = -1, to = 1)
wave3SliderL3 = Label(frame3, text='Time Scaling')
wave3Slider3 = Scale(frame3, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, tickinterval = 2, resolution = 2, variable = tScale3,from_= -8, to = 8)

wave3Play = Scale(frame3, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10, variable = play3Var)
playbutton3 = Button(frame3, text='Play', command=play3, state = 'active')
pausebutton3 = Button(frame3, text='Pause', command=pause3, state = 'active')
mutebutton3 = Button(frame3, text='Mute', command=mute)

wave3Label1.grid(row=0, column=0, sticky = 'W')
openFile3Butt.grid(row=1, column=0, sticky = 'W', columnspan = 2)
wave3SliderL1.grid(row=2, column=0)
wave3Slider1.grid(row=3, column=0) 
wave3SliderL2.grid(row=4, column=0) 
wave3Slider2.grid(row=5, column=0) 
wave3SliderL3.grid(row=6, column=0)
wave3Slider3.grid(row=7, column=0) 
wave3Check1.grid(row=8, column = 0, sticky = 'W')
wave3Check2.grid(row=9, column = 0, sticky = 'W')
wave3Check3.grid(row=10, column = 0, sticky = 'W')
playbutton3.grid(row =11, column = 0, columnspan = 3)
#pausebutton3.grid(row =11, column = 0, columnspan = 3)
#mutebutton3.grid(row =11, column = 0, columnspan = 3, sticky = 'E')
wave3Play.grid(row =12, column = 0)

'''Down Frame'''

framel = Frame(frame_down, bd = 50)
framel.pack(side = LEFT)

framer = Frame(frame_down, bd = 50)
framer.pack(side = RIGHT)

def playModulate():
 
    opened = False
    if selectedFile[0] is not '':
        wave1 = wave_mixture(selectedFile[0])
        if amp1.get() is not 0:
            wave1.ampScaling(amp1.get()) 
            wave1.data = wave1.scaledData

        if tShift1.get() is not 0:
            wave1.timShifting(tShift1.get()) 
            wave1.data = wave1.shiftedData
            wave1.length = wave1.new_length

        if tScale1.get() is not 0:
            wave1.timScaling(tScale1.get()) 
            wave1.data = wave1.tscaledData
            wave1.length = wave1.new_length
        
        if check1.get() is 1:
            wave1.timReversal() 
            wave1.data = wave1.rev_data
        

    if selectedFile[1] is not '':
        wave2 = wave_mixture(selectedFile[1])
        if amp2.get() is not 0:
            wave2.ampScaling(amp2.get()) 
            wave2.data = wave2.scaledData

        if tShift2.get() is not 0:
            wave2.timShifting(tShift2.get()) 
            wave2.data = wave2.shiftedData
            wave2.length = wave2.new_length

        if tScale2.get() is not 0:
            wave2.timScaling(tScale2.get()) 
            wave2.data = wave2.tscaledData
            wave2.length = wave2.new_length

        if check4.get() is 1:
            wave2.timReversal() 
            wave2.data = wave2.rev_data
        

    if selectedFile[2] is not '':
        wave3 = wave_mixture(selectedFile[2])
        if amp3.get() is not 0:
            wave3.ampScaling(amp3.get()) 
            wave3.data = wave3.scaledData

        if tShift3.get() is not 0:
            wave3.timShifting(tShift3.get()) 
            wave3.data = wave3.shiftedData
            wave3.length = wave3.new_length

        if tScale3.get() is not 0:
            wave3.timScaling(tScale3.get()) 
            wave3.data = wave3.tscaledData
            wave3.length = wave3.new_length
        
        if check7.get() is 1:
            wave3.timReversal() 
            wave3.data = wave3.rev_data
        


    new_data = [] 

    modulate1, modulate2, modulate3 = 0,0,0

    if check2.get() is 1:
        waveMod = wave_mixture(selectedFile[0])
        print 'Modulatig file 1'
#        print len(wave1.data)
#        new_data  wave1.data
        modulate1 = 1
        for i in range(len(wave1.data)):
            if i < len(new_data):
                new_data.append(wave1.data[i])
                if new_data[i] > 32767:
                    new_data[i] = 32767
                elif new_data[i] < -32768:
                    new_data[i] = -32768
            else:
                new_data.append(wave1.data[i])
    
    if check5.get() is 1:
        modulate2 = 1
        print 'Modulating file 2'
        if modulate1 is 1:
            for i in range(len(wave2.data)):
                if i < len(new_data):
                    new_data[i] *= wave2.data[i]
                    if new_data[i] > 32767:
                        new_data[i] = 32767
                    elif new_data[i] < -32768:
                        new_data[i] = -32768
                else:
                    new_data.append(wave2.data[i])
        else :
            waveMod = wave_mixture(selectedFile[1])
            new_data = wave2.data


    if check8.get() is 1:
        print 'Modulating file 3'
        modulate3 = 1

        if modulate1 is 1 or modulate2 is 1:
            for i in range(len(wave3.data)):
                if i < len(new_data):
                    new_data[i] *= wave3.data[i]
                    if new_data[i] > 32767:
                        new_data[i] = 32767
                    elif new_data[i] < -32768:
                        new_data[i] = -32768
                else:
                    new_data.append(wave3.data[i])
        else:
            waveMod = wave_mixture(selectedFile[2])
            new_data = wave3.data

               
    waveMod.data = new_data

    #print 'Mod Data: ',waveMod.data

    waveMod.write2('Mix.wav')


    chunk = 1024
    wavFile = wave.open('Mix.wav','rb')

    player = pyaudio.PyAudio()

    stream = player.open(format = player.get_format_from_width(wavFile.getsampwidth()),channels=wavFile.getnchannels(),rate = wavFile.getframerate(),output = True)

    data = wavFile.readframes(chunk)

    while data is not '' :
        stream.write(data)
        data = wavFile.readframes(chunk)

    stream.stop_stream()
    stream.close()

    player.terminate()

    return

def pauseModulate():
    return

modulatePlay = Scale(framel, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10)
modulatePlaybutton = Button(framel, text='Play', command=playModulate)
modulatePausebutton = Button(framel, text='Pause', command=pauseModulate)
modulateMutebutton = Button(framel, text='Mute', command=mute)
modulateLabel = Label(framel, text = 'Modulate and Play')
modulatePlaybutton.grid(row =0, column = 0, columnspan = 3)
#modulatePausebutton.grid(row =0, column = 0, columnspan = 3)
#modulateMutebutton.grid(row =0, column = 0, columnspan = 3, sticky = 'E')
modulatePlay.grid(row =1, column = 0)
modulateLabel.grid(row=2,column = 0)

def playMix():

    opened = False
    if selectedFile[0] is not '':
        wave1 = wave_mixture(selectedFile[0])
        if amp1.get() is not 0:
            wave1.ampScaling(amp1.get()) 
            wave1.data = wave1.scaledData

        if tShift1.get() is not 0:
            wave1.timShifting(tShift1.get()) 
            wave1.data = wave1.shiftedData
            wave1.length = wave1.new_length

        if tScale1.get() is not 0:
            wave1.timScaling(tScale1.get()) 
            wave1.data = wave1.tscaledData
            wave1.length = wave1.new_length
        
        if check1.get() is 1:
            wave1.timReversal() 
            wave1.data = wave1.rev_data
        

    if selectedFile[1] is not '':
        wave2 = wave_mixture(selectedFile[1])
        if amp2.get() is not 0:
            wave2.ampScaling(amp2.get()) 
            wave2.data = wave2.scaledData

        if tShift2.get() is not 0:
            wave2.timShifting(tShift2.get()) 
            wave2.data = wave2.shiftedData
            wave2.length = wave2.new_length

        if tScale2.get() is not 0:
            wave2.timScaling(tScale2.get()) 
            wave2.data = wave2.tscaledData
            wave2.length = wave2.new_length

        if check2.get() is 1:
            wave2.timReversal() 
            wave2.data = wave2.rev_data
        

    if selectedFile[2] is not '':
        wave3 = wave_mixture(selectedFile[2])
        if amp3.get() is not 0:
            wave3.ampScaling(amp3.get()) 
            wave3.data = wave3.scaledData

        if tShift3.get() is not 0:
            wave3.timShifting(tShift3.get()) 
            wave3.data = wave3.shiftedData
            wave3.length = wave3.new_length

        if tScale3.get() is not 0:
            wave3.timScaling(tScale3.get()) 
            wave3.data = wave3.tscaledData
            wave3.length = wave3.new_length
        
        if check3.get() is 1:
            wave3.timReversal() 
            wave3.data = wave3.rev_data
        


    new_data = [] 

    mix1, mix2, mix3 = 0,0,0

    if check3.get() is 1:
        waveMix = wave_mixture(selectedFile[0])
        print 'Mixing file 1'
#        print len(wave1.data)
#        new_data  wave1.data
        mix1 = 1
        for i in range(len(wave1.data)):
            if i < len(new_data):
                new_data.append(wave1.data[i])
                if new_data[i] > 32767:
                    new_data[i] = 32767
                elif new_data[i] < -32768:
                    new_data[i] = -32768
            else:
                new_data.append(wave1.data[i])
    
    if check6.get() is 1:
        mix2 = 1
        print 'Mixing file 2'
        if mix1 is 1:
            for i in range(len(wave2.data)):
                if i < len(new_data):
                    new_data[i] += wave2.data[i]
                    if new_data[i] > 32767:
                        new_data[i] = 32767
                    elif new_data[i] < -32768:
                        new_data[i] = -32768
                else:
                    new_data.append(wave2.data[i])
        else :
            waveMix = wave_mixture(selectedFile[1])
            new_data = wave2.data


    if check9.get() is 1:
        print 'Mixing file 3'
        mix3 = 1

        if mix1 is 1 or mix2 is 1:
            for i in range(len(wave3.data)):
                if i < len(new_data):
                    new_data[i] += wave3.data[i]
                    if new_data[i] > 32767:
                        new_data[i] = 32767
                    elif new_data[i] < -32768:
                        new_data[i] = -32768
                else:
                    new_data.append(wave3.data[i])
        else:
            waveMix = wave_mixture(selectedFile[2])
            new_data = wave3.data

               
    waveMix.data = new_data

    #print 'Mix Data :', waveMix.data

    waveMix.write2('Mix.wav')


    chunk = 1024
    wavFile = wave.open('Mix.wav','rb')

    player = pyaudio.PyAudio()

    stream = player.open(format = player.get_format_from_width(wavFile.getsampwidth()),channels=wavFile.getnchannels(),rate = wavFile.getframerate(),output = True)

    data = wavFile.readframes(chunk)

    #print data,'read data'
    while data is not '' :
        #print 'writing to stream mix'
        stream.write(data)
        data = wavFile.readframes(chunk)

    stream.stop_stream()
    stream.close()

    player.terminate()

    return

def pauseMix():
    return

mixPlay = Scale(framer, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10)
mixPlaybutton = Button(framer, text='Play', command=playMix)
mixPausebutton = Button(framer, text='Pause', command=pauseMix)
mixMutebutton = Button(framer, text='Mute', command=mute)
mixLabel = Label(framer, text = 'Mix and Play')
mixPlaybutton.grid(row =0, column = 0, columnspan = 3)
#mixPausebutton.grid(row =0, column = 0, columnspan = 3)
#mixMutebutton.grid(row =0, column = 0, columnspan = 3, sticky = 'E')
mixPlay.grid(row =1, column = 0)
mixLabel.grid(row=2,column = 0)

def record():
    records = waveRecorder()
    records.record_to_file('recording.wav')

def playRecord():

    chunk = 1024
    wavFile = wave.open('recording.wav','rb')

    player = pyaudio.PyAudio()
 
    stream = player.open(
        format = player.get_format_from_width(wavFile.getsampwidth()),
        channels=wavFile.getnchannels(),
        rate = wavFile.getframerate(),
        output = True)

    data= wavFile.readframes(chunk)
    
    while data is not '' :
        stream.write(data)
        data = wavFile.readframes(chunk)

    stream.stop_stream()
    stream.close()

    player.terminate()

    return

def pauseRecord():
    return

record = Button(frame_record, text='Record', command=record)
recordPlaybutton = Button(frame_record, text='Play', command=playRecord)
recordPausebutton = Button(frame_record, text='Pause', command=pauseRecord)
seekPlay = Scale(frame_record, orient=HORIZONTAL, length = 300, width = 20, sliderlength = 10)

record.grid(row = 1,column=0)
recordPlaybutton.grid(row = 1, column = 2)
#recordPausebutton.grid(row = 1, column = 2)
seekPlay.grid(row = 2,column = 0, columnspan = 3)


window.mainloop()
