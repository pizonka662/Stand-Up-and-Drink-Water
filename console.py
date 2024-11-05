from tabnanny import check

import serial
import threading
import time

def readFromSerial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=1.5)
    '''
    while True:
        data = ser.readline().decode().strip()
        if data:
            separateData = data.split("|")
            height, weight = float(separateData[0]), float(separateData[1])
            print("Height: " , height, " Weight: ", weight)
    '''
    return ser

def checkTableHeight(input, maxTimeSitting=.1):
    minHeight = 72
    counter = 0
    print("height: ", input)
    '''
    while True:
        data = input.readline().decode().strip()
        if data:
            height = float(data.split("|")[0])
                print("Height: ", height)
        
                #for every tick the table is still at sitting height, count up
                if height <= minHeight:
                    counter+=1
                else:
                    counter = 0
        
                #if the time passes the maxTimeSitting parameter, eventually send a notification to stand up.
                if counter > maxTimeSitting:
                    print("It's time to stand up.")
                    counter = 0
        '''
def checkWaterDrank(input):
    print("weight: ", input)
        #if data:
           #waterLevel = float(data.split("|")[1])
            #print("Water level: ", waterLevel)

if __name__ == '__main__':
    ser = readFromSerial('COM3', 115200)
    #checkTableHeight(ser)
    while True:
        heightData = float(ser.readline().decode().strip().split("|")[0])
        waterData = float(ser.readline().decode().strip().split("|")[1])

        heightThread = threading.Thread(target=checkTableHeight, args=(heightData,))
        heightThread.start()

        waterThread = threading.Thread(target=checkWaterDrank, args=(waterData, ))
        waterThread.start()