
#-*- coding: utf-8 -*-

import numpy as np
import PIL
import os
from matplotlib import pyplot

IMGSZIE = 128

class PGM(object):
    def __init__(self, filepath):
        with open(filepath, "rb") as f:
            #header = f.read(15)
            #print(header)
            self.type = "p5"#header[0:2]
            self.width = IMGSZIE #int(header[3:6])-3
            self.height = IMGSZIE #int(header[7:10])
            self.maxval = 256 #int(header[11:14])
            
            self.datalen = self.width * self.height
            self.data = f.read(self.datalen)
            self.dataf =np.zeros((self.height, self.width))

            for i in range(len(self.data)-1) :
                y = i%self.width
                x = int(i/self.width)

                if self.data[i] == '' :
                    self.dataf[x][y] = int(0)
                else  :
                    self.dataf[x][y] = int(self.data[i])
                #print (self.dataf[x][y])
                
            #print (self.dataf)

    def get_imagedata(self):
        return self.dataf

Train_dir = "./data/rawdata"

facelist =[]
filenames = os.listdir(Train_dir)

faceCount = 0
for filename in filenames:
    full_filename = os.path.join(Train_dir, filename)
    print (full_filename)
    train_pgm = PGM(full_filename)
    facelist.append(np.reshape(train_pgm.get_imagedata(), IMGSZIE*IMGSZIE))
    faceCount = faceCount + 1
  
print(facelist)

MeanMat =np.zeros((IMGSZIE * IMGSZIE),dtype=np.float)
for i in range(IMGSZIE*IMGSZIE) :
    for j in range (faceCount) :
        MeanMat[i] = MeanMat[i] + facelist[j][i]
    MeanMat[i] = MeanMat[i] / faceCount

DbMat =np.zeros((faceCount,IMGSZIE * IMGSZIE),dtype=np.float)
for i in range(IMGSZIE*IMGSZIE) :
    for j in range (faceCount) :
        DbMat[j][i] = facelist[j][i] - MeanMat[i]

CovMat = (np.dot(DbMat,DbMat.T))/IMGSZIE * IMGSZIE 
print (CovMat.shape)
print (CovMat)

#image = PIL.Image.open('face01.pgm')
#print(image)
#image.show()

pyplot.imshow(np.reshape(MeanMat,(IMGSZIE,IMGSZIE)), pyplot.cm.gray)
pyplot.show()