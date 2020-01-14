# RaspberryPi ImageCapture

A python script that allows you to take images using your raspberryPi and save them on your pi. Uses the gphoto library

## setup

1. Install gphoto2 library `sudo apt-get install gphoto2`
2. Detect camera using `gphoto2 --auto-detect`
3. Change capture target to Camera Memory Card `gphoto2 --set-config capturetarget=1`
4. Run `gphoto2 --list-files` to locate folder where images have been stored
5. Install sh using pip `sudo pip3 install sh`
6. Run program using python3
