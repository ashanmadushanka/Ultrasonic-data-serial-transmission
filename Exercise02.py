import serial #Import Serial Library
from vpython import * #Import all the vPython library

arduinoSerialData = serial.Serial('com5', 9600) #Create an object for the Serial port. Adjust 'com5' to whatever port your arduino is sending to.
measuringRod = cylinder( radius= .1, length=6, color=color.yellow, pos= vector(-3,-2,0), make_trail=True)
lengthLabel = label(pos= vector(0,5,0), text='Target Distance is: ', box=False, height=50, make_trail=True)
target=box(pos= vector(0,-.5,0), length=.2, width=3, height=3, color=color.green)
while (1==1):  #Create a loop that continues to read and display the data
    rate(20)#Tell vpython to run this loop 20 times a second
    if (arduinoSerialData.inWaiting()>0):  #Check to see if a data point is available on the serial port
        myData = arduinoSerialData.readline().decode('utf-8').rstrip() #Read the distance measure as a string
        print (myData) #Print the measurement to confirm things are working
        distance =float(myData) #convert reading to a floating point number
        measuringRod.length=distance #Change the length of your measuring rod to your last measurement
        target.pos= vector(-3+distance,-.5,0)
        myLabel= 'Target Distance is: ' + myData #Create label by appending string myData to string
        lengthLabel.text = myLabel #display updated myLabel on your graphic
