from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal,os,subprocess


#Kill gphoto2 process when we start the camera
def killgphoto2Process():
    # writing the command that we want to execute which can have an output and an error
    p = subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
    output, error = p.communicate()
    
    # searching for the line that has the process we want to kill
    for line in output.splitlines():
        #finding the value in byte format
        if b'gvfsd-gphoto2' in line:
            # kill the process if we find it
            pid = int(line.split(None,1)[0]) # gets the PID and stores it as int
            
            os.kill(pid,signal.SIGKILL)
            
shot_date = datetime.now().strftime("%Y-%m-%d")
shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
picID = "PiShots"


clearCommand = ["--folder", "/store_00020001/DCIM/100CANON", "-R", "--delete-all-files"]
triggerCommand = ["--trigger-capture"]
downloadCommand = ["--get-all-files"]
folder_name = shot_date+picID
save_location="/home/pi/Desktop/gphoto/images/"+folder_name

def createSaveFolder():
    try:
        os.makedirs(save_location)
    except:
        print("Failed to create new directory. Directory may already exist")
    os.chdir(save_location) #changing to that directory to run scripts

def captureImages():
    gp(triggerCommand)
    sleep(3)
    gp(downloadCommand)
    gp(clearCommand)

#renaming images function
def renameFiles(ID):
    for filename in os.listdir("."):
        if len(filename) < 13:
            newFile = (shot_time + ID)+".JPG"
            os.rename(filename,newFile)
            print("Renamed the jpg")
            return newFile
def openImage(location):
    try:     
        print("opening image...")
        p = subprocess.Popen(['xdg-open',location],stdout=subprocess.PIPE)
        error = p.communicate()
        print("image opened successfully")
    except:
        print(error)
        #print("Failed to open image")
def normalPicture():
    createSaveFolder()
    captureImages()
    file=renameFiles(picID)
    openImage(file)
def timelapse():
    while True:
        createSaveFolder()
        captureImages()
        file=renameFiles(picID)
        openImage(file)
        sleep(2)
        
killgphoto2Process()
gp(clearCommand)
normalPicture()
#timelapse()