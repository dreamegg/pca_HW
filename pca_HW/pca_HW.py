
#with codecs.open("face01.pgm", "r",encoding='utf-8', errors='ignore') as f:
#-*- coding: utf-8 -*-

import numpy as np
import PIL
import os
from matplotlib import pyplot

class PGM(object):
    def __init__(self, filepath):
        with open(filepath, "rb") as f:
            #header = f.read(15)
            #print(header)
            self.type = "p5"#header[0:2]
            self.width = 128 #int(header[3:6])-3
            self.height = 128 #int(header[7:10])
            self.maxval = 256 #int(header[11:14])
            
            self.datalen = self.width * self.height
            self.data = f.read(self.datalen)
            print(len(self.data) , self.datalen)
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
for filename in filenames:
    full_filename = os.path.join(Train_dir, filename)
    print (full_filename)
    train_pgm = PGM(full_filename)
    facelist.append(train_pgm.get_imagedata())
  
#image = PIL.Image.open('face01.pgm')
#print(image)
#image.show()

pyplot.imshow(train_pgm.get_imagedata(), pyplot.cm.gray)
pyplot.show()
