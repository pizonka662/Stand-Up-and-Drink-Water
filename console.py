from tabnanny import check

import serial
import threading
import time

def readFromSerial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.5)
    '''
    while True:
        data = ser.readline().decode().strip()
        if data:
            separateData = data.split("|")
            height, weight = float(separateData[0]), float(separateData[1])
            print("Height: " , height, " Weight: ", weight)
    '''
    return ser

def checkTableHeight(input, maxTimeSitting=10):
    minHeight = 72
    counter = 0
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

def checkWaterDrank(input):
    while True:
        data = input.readline().decode().strip()
        print(data)
        #if data:
           #waterLevel = float(data.split("|")[1])
            #print("Water level: ", waterLevel)

if __name__ == '__main__':
    ser = readFromSerial('COM3', 115200)
    #checkTableHeight(ser)
    time.sleep(3)
    heightThread = threading.Thread(target=checkTableHeight, args=(ser,))
    heightThread.start()
    time.sleep(3)
    waterThread = threading.Thread(target=checkWaterDrank, args=(ser, ))
    waterThread.start()