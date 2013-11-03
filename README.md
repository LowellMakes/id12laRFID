id12laRFID
==========

Function: RFID entry/machine use system for Makerspaces

##Usage:
    readRFID.py -f & (run as background process)
    readRFID.py -r <room1> (check acces to room /print Card ID)
the user log is saved in the same folder "userlog.txt"

    Hardware Connection:
    SFE RFID bread out        Raspberry Pi(Rev2/1)
    VCC           --------->  P1
    GND           --------->  P6
    TXD           --------->  P8 (GPIO 14)
   
Magnetic Lock is connected to Relay1 on PiFace

######used this guide to free the UART, http://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi
######use this guide to setup Piface http://www.farnell.com/datasheets/1684425.pdf
######this needs the pyserial library

####userlist:
CSV database for users, rooms, and card ID

 
###TODO:
 - [x] Read RFID
 - [x] Validate user from DB
 - [x] Activate Relays
 - [x] Maintain user access logs
 - [ ] Deamon process to monitor tasks
 - [ ] Failsafe
 - [ ] SQL support
 - [ ] Web interface for user management
