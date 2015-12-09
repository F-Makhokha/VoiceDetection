#!/usr/bin/env python

'''   
  Author: Fannie Makhokha
 
  Created on 03 August 2015, 11:42 AM
 '''
from subprocess import call
import logging
import datetime
import os
import glob
import time
import sh
import shutil
import os.path
import serial

'''
Here we will put the appropriate port needed to be activated
/dev/ttyS0 and so forth
from my machine /dev/ttyS4 seems to be free and writable

path for the wavefile needs to be changed to meet the deployment.
'''
#dmesg | grep tty
ser = serial.Serial('/dev/ttyS4')
#ser = serial.Serial('/dev/tty0')
#ser = serial.Serial('/dev/ttyS3')


def OpenPort():
    #Activativate Port
    print ("You can now Talk for 30 seconds")
    #port activate goes here
    ser.setRTS(True)
    time.sleep(30)
    print ("Time up!!!!!!!")
    
def ClosePort():
    #closing the port
    print ("We are closing the port")
    #port closing goes here
    ser.setRTS(False)
    print ("Port is closed!!!!!!!")  

# This is the sensitivity of the audio
threshold = '10%'

if  __name__ == "__main__":
    logging.basicConfig(filename='conection_to_site.log',
						format='%(filename)s [%(lineno)d] %(message)s',
                        level=logging.INFO)
    while (1):
        if os.path.isfile('deleteme.wav') and os.access('/home/fannie/Documents/VOICEACTIVITYDETECTION/2py/mysox/', os.R_OK):
            os.remove('deleteme.wav')
            print('file deleted')
            OpenPort()
            ClosePort()
            
        start_now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        start_time = datetime.datetime.now()
        start = start_time.strftime('%Y-%m-%d %H:%M:%S')
        output_filename = 'deleteme.wav'

        Executecommand = ['rec', '-c', '1', output_filename, 'rate', '8k', 'silence',
			'1', '0.1', threshold, '1', '3.0', threshold]

        call(Executecommand)

        end_time = datetime.datetime.now()
        end = end_time.strftime('%Y-%m-%d %H:%M:%S')
        logging.info("%s ~ %s (%f)" %(start, end,(end_time-start_time).total_seconds()))
        #keep closing for safety
        ClosePort()
        
#close again for safety
ClosePort()

        

