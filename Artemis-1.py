#Artemis-1


import time
from PIL import Image

s = input('if you want to start say "yes" or "no": ')

if s.lower() != 'yes':
    quit()
    
else:


    print('loading...')
    time.sleep(1)
    print('info/bash')
while True:
    info = input('linuxserver2@192.168.1.14=$')

    if info.lower() == "timelines":

        timeline = Image.open(r"G:\programing\code\Python-code\Artemis\timelines.png")
        timeline.show()

    if info.lower() == 'timeline map':
        timelinemap = Image.open(r"G:\programing\code\Python-code\Artemis\timelinemap.png")
        timelinemap.show()  
        
    if info.lower() == 'timeline 3d':
        timeline3d = Image.open(r"G:\programing\code\Python-code\Artemis\artemis-map-3d.jpg")
        timeline3d.show()
        
    if info.lower() == "splashdown location":
        print('location: pacific ocean')
        
    if info.lower() == 'quit':
        quit()
#lunch shell_____________________________________________________________________



    if info.lower() == "launch":
        print('loading launch shell')
        time.sleep(3)
        print('launch/bash')
        while True:
            launch = input('linuxserver1@192.168.1.15=$')
            if launch.lower() == "timelines":

                timeline = Image.open(r"G:\programing\code\Python-code\Artemis\timelines.png")

                timeline.show()
                
            if launch.lower() == 'timeline map':
                timelinemap = Image.open(r"G:\programing\code\Python-code\Artemis\timelinemap.png")
                timelinemap.show()

            if launch.lower() == 'timeline 3d':
                timeline3d = Image.open(r"G:\programing\code\Python-code\Artemis\artemis-map-3d.jpg")
                timeline3d.show()
                
            if launch.lower() == 'quit':
                quit()
            
            if launch.lower() == 'go':
               
               
               print('5')
               time.sleep(1)
               print('4')
               time.sleep(1)
               print('3')
               time.sleep(1)
               print('2')
               time.sleep(1)
               print('1')
               print('ignition')
               time.sleep(1.9)
               print('lift off!!!!    lacation:kennedy space center')
               print('')
               time.sleep(132)
               print('Solid rocket booster separation                   Altitude: 45km     (28mi)')
               print('')
               time.sleep(61)
               print('Service module panels jettisoned                  Altitude: 88km    (55mi)')
               print('')
               time.sleep(6)
               print('Launch abort tower jettison                       Altitude: 91km    (57mi)')
               print('')
               time.sleep(297)
               print('Main engine cutoff and core stage separation      Altitude: 157km   (98mi)')
               print('')
               time.sleep(604)
               print('Solar panel deployment begins                     Altitude: 484km   (301mi)')
               print('')
               time.sleep(1982)
               print('Perigee raise maneuver                            Altitude: 1,791km (1,113mi)')
               print('')
               time.sleep(2801)
               print('Trans-lunar injection (TLI) burn                  Altitude: 601km   (373mi)')
               print('')
               time.sleep(1687)
               print('Orion/ICPS separation                             Altitude: 3,849km (2,392mi)')
               time.sleep(3)
               Image.open(r"G:\programing\code\Python-code\Artemis\timelines.png")
               