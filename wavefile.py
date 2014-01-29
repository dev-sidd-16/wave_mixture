#!/usr/bin/env python

from Tkinter import *
from record import*
import wave, struct, Tkinter
import tkFileDialog
import sys
import pyaudio

selectedFile = ['','','']
p1 = 0
p2 = 0
p3 = 0

class wave_mixture:

    def __init__(self,filName):
        
        waveFile = wave.open(filName,'rb')
        
        self.data = []
        self.noOfChannels = waveFile.getnchannels()
        self.widthSample = waveFile.getsampwidth()
        self.rateFrame = waveFile.getframerate()
        self.length = waveFile.getnframes()

        self.samples = self.length * self.noOfChannels
        self.raw_data = waveFile.readframes(self.length)

        if self.widthSample is 1:
            fmt = "%iB" %self.samples
        elif self.widthSample is 2:
            fmt = "%ih" %self.samples


        input_data = struct.unpack(fmt, self.raw_data)

        self.data = list(input_data)

        self.length = len(self.data)
        #print self.data
        waveFile.close()

    def write1(self,newFile):
        wavFile = wave.open(newFile,'w')
        nChannels = self.noOfChannels
        sampWidth = self.widthSample
        frameRate = self.rateFrame
        nFrames = self.length
        compType = 'NONE'
        compName = 'not compressed'

        wavFile.setparams((nChannels, sampWidth, frameRate, nFrames, compType, compName))

        for i in range(nFrames):
            if sampWidth is 1:
                fmt = "%iB" %self.length*self.noOfChannels
            elif sampWidth is 2:
                fmt = "%ih" %self.length*self.noOfChannels

        new_data = struct.pack(fmt,*(self.data))
        wavFile.writeframes(new_data)


        wavFile.close()

        return

    def ampScaling(self,factor):

        wavFile = []        
        wavFile = self.data

        newData = []
        length = self.length

        for i in range(0,length):
            if self.noOfChannels is 1:
                if(wavFile[i] * factor > 32767):
                    wavFile[i] = 32767
                elif(wavFile[i] * factor < -32768):
                    wavFile[i] = -32768
                else:
                    wavFile[i] = wavFile[i]*factor
            elif self.noOfChannels is 2:
                if(wavFile[i] * factor > 2147483647):
                    wavFile[i] = 2147483647
                elif(wavFile[i] * factor < -2147483648):
                    wavFile[i] = -2147483648
                else:
                    wavFile[i] = wavFile[i]*factor
            
        self.scaledData = wavFile
        self.length = len(self.data)
        return

    def timShifting(self,factor):
        wavFile = self.data

        newData = []

        oldRate = self.rateFrame
        toShift = factor * oldRate
        
        toShift = int(abs(toShift))        
        #print toShift,'Shifted by ??'
        if self.noOfChannels is 1:
            if factor < 0:
                wavFile = wavFile[toShift::1]
    
            else:
                zeroes = []
                for i in range(0,toShift):
                    zeroes.append(0)
                wavFile = zeroes+wavFile

        elif self.noOfChannels is 2:        
            if factor < 0:
                wavFile = wavFile[2*toShift::1]

            else:
                zeroes = []
                for i in range(0,2*toShift):
                    zeroes.append(0)
                wavFile = zeroes+wavFile

        self.shiftedData = wavFile
        self.new_length = len(self.shiftedData)/self.noOfChannels

        self.length = len(self.data)
        return

    def timScaling(self, factor):
        if factor < 0:
            factor = -(1.0/factor)
            #print factor

        new_data = []
        l1, l2 = [], []
        lenth = int(self.length/factor)
        if self.noOfChannels is 1:
            for i in range(lenth):
                new_data.append(self.data[int(factor*i)])
        else:
            for i in range(self.length):
                if i%2 is 1:
                    l1.append(self.data[i])
                else:
                    l2.append(self.data[i])

            for i in range(int(len(l2)/factor)):
                new_data.append(l2[int(factor*i)])
                new_data.append(l1[int(factor*i)])

        self.tscaledData = new_data
        self.new_length = len(self.tscaledData)/self.noOfChannels

        self.length = self.new_length
        return

    def timReversal(self):
        wavFile = self.data
        
        length = self.length 

        for i in range(0,length/2):
            temp = wavFile[i]
            wavFile[i] = wavFile[length-i-1]
            wavFile[length-i-1] = temp

        self.rev_data = wavFile

        self.length = len(self.data)
        return

    def write2(self,newFile):
        wavFile = wave.open(newFile,'w')
        nChannels = self.noOfChannels
        sampWidth = self.widthSample
        frameRate = self.rateFrame
        nFrames = self.length
        compType = 'NONE'
        compName = 'not compressed'

        wavFile.setparams((nChannels, sampWidth, frameRate, nFrames, compType, compName))

        for i in range(nFrames):
            if sampWidth is 1:
                new_data = struct.pack("B",self.data[i])
            elif sampWidth is 2:
                new_data = struct.pack("h",self.data[i])
        
            wavFile.writeframes(new_data)

        self.data = new_data
        wavFile.close()

        return



