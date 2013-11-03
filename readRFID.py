import sys
import os
import time
import serial
import csv
import optparse
import piface.pfio as pfio

def RFIDread():
    ser = serial.Serial("/dev/ttyAMA0")
    print "waiting for a card"
    id = ser.read(13)
    print "The ID is :"
    print id
    ser.close()
    return id[1:]

def validateUser(id='',room=''):
    with open('userlist.csv','rb') as file:
        reader = csv.reader(file)
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if id in row['id']:
                if 'yes' in row[room]:
                #    print 'yes'
                    return 1
                else:
                #    print 'No'
                    return 0
                

def main():
    parser = optparse.OptionParser()
    parser.add_option('-r', '--room',help='check access to this room',
                      dest='roomname', default='room1', action='store')
    parser.add_option('-f', '--forever', help='run forever',
                      dest='runf', default=False, action='store_true')
    (opts, args) = parser.parse_args()
    pfio.init()
    pin = 0
    if(opts.runf == False):
        room = opts.roomname
        ID=RFIDread()
        key=validateUser(str(ID),str(room))
    else:
        while(True):
            roomcount = 0
            ID=RFIDread()
            if validateUser(str(ID),'room1'):
                roomcount = roomcount + 1
                print "access granted to room1"
                pfio.digital_write(0,1)
                time.sleep(3)
                pfio.digital_write(0,0)
            if validateUser(str(ID),'room2'):
                roomcount = roomcount +1
                print "access granted to room2"
                pfio.digital_write(1,1)
                time.sleep(3)
                pfio.digital_write(1,0)
            if validateUser(str(ID),'room3'):
                roomcount = roomcount +1
                print "access granted to room3"
                pfio.digital_write(2,1)
                time.sleep(3)
                pfio.digital_write(2,0) 
            if roomcount == 3:
                print "Sorry! No access"

    if room == 'room1':
        pin = 0
    elif room == 'room2':
        pin = 1
    elif room == 'room3':
        pin = 2

    if key:
        print "!! Access Granted !!"
        pfio.digital_write(pin,1)
        time.sleep(3)
        pfio.digital_write(pin,0)
    else:
        print "Sorry! No access"

if __name__ == "__main__":
    main()
    
 
