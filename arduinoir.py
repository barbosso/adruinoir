import os
import  serial
import time

ArduinoSerial = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2) 



while True:
    data = ArduinoSerial.readline()
    print(data) #read the serial data and print it as line
    if data.decode().strip() == '410A857':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --button=enter')

    if data.decode().strip() == '41048B7':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --button=up')

    if data.decode().strip() == '410C837':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --button=down')

    if data.decode().strip() == '41028D7':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --button=left')

    if data.decode().strip() == '4106897':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --button=right')

    if data.decode().strip() == '41020DF':
        os.system('kodi-send --host=127.0.0.1 --port=9777 -a mute')

    if data.decode().strip() == '41008F7':
        os.system('kodi-send --host=127.0.0.1 --port=9777 -a back')

    if data.decode().strip() == '410EA15':
        os.system('kodi-send --host=127.0.0.1 --port=9777 -a playpause')

    if data.decode().strip() == '410A05F':
        os.system('warp-cli disconnect')
        os.system("""
        kodi-send --host=127.0.0.1 --port=9777 --action='ActivateWindow(Videos,"plugin://plugin.video.movix/channels", return)'
        """
        )

    if data.decode().strip() == '41040BF':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --action=volumeup')

    if data.decode().strip() == '410C03F':
        os.system('kodi-send --host=127.0.0.1 --port=9777 --action=volumedown')

    if data.decode().strip() == '410708F':
        os.system('warp-cli connect')


    if data.decode().strip() == '41000FF':
        time.sleep(30)
        os.system('/usr/bin/poweroff -h')
    else:
        pass
