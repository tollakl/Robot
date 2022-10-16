import pandas as pd
import os
import cv2
from datetime import datetime

global steeringList, imgList, countFolder

countFolder = 0
counter = 0
imgList = []
steeringList = []

#Get the directory path. You have to create the folder DataCollected
myDirectory = os.path.join(os.getcwd(), 'DataCollected')

# se om mappe allerede finnes og/eller legg på nytt tall
while os.path.exists(os.path.join(myDirectory,f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG"+str(countFolder)
os.mkdir(newPath)


#Lage en funksjon som tar inn bilder og styrevinkel og lagrer de i listene
def saveData(img, steering):
    global steeringList, imgList
    #Lager variabel som lagrer tid fra timestamp
    now = datetime.now()
    #lager en variabel til et timestamp må gjøre i to steg for å konvertere til en string og ta vekk et komma
    timestamp = str(datetime.timestamp(now)).replace('.',"")
    #lager filnavn til å lagre bilder i
    fileName = os.path.join(newPath,f'Image_{timestamp}.jpg')
    #lagrer bilde som filnavnet
    cv2.imwrite(fileName, img)
    #legger filnavnet i global liste for å bruke det i csvloggen
    imgList.append(fileName)
    #legger styrevinkel i global liste for å bruke det i csvloggen
    steeringList.append(steering)

#save logfile to csv using Pandas
def saveLog():
    global imgList, steeringList
    #lager colonnennavn og hva som skal være i colonnene
    rawData = {'Image': imgList, 'Steering': steeringList}
    #Lager selve "tabellen"
    df = pd.DataFrame(rawData)
    #lager csvfilen i rette mappe og med filnavn
    df.to_csv(os.path.join(myDirectory, f'log_{str(countFolder)}.csv'), index=True, header=True)
    print('Log saved')
    print('Total images:', len(imgList))


#ser om filen
if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    for i in range(10):
        _, img = capture.read()
        saveData(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow("Image", img)
    saveLog()




