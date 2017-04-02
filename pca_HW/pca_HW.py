
#with codecs.open("face01.pgm", "r",encoding='utf-8', errors='ignore') as f:
import numpy as np
import os
from matplotlib import pyplot

class PGM(object):
    def __init__(self, filepath):
        with open(filepath, "r",errors='ignore') as f:
            header = f.read(15)
            print(header)
            self.type = header[0:2]
            self.width = int(header[3:6])
            self.height = int(header[7:10])
            self.maxval = int(header[11:14])
            self.datalen = self.width* self.height

            #self.data = f.read(self.datalen)
            #print(len(self.data))
            self.dataf =np.zeros((self.height, self.width))
            i=0
            for i in range(self.datalen) :
                a= f.read(1) 
                y = i%self.width
                x = int(i/self.width)
                #print(x,y)

                if a == '' :
                    self.dataf[x][y] = 0
                else  :
                    self.dataf[x][y] = ord(a)
                    if ord(a) == 255 :
                        print ("%X"%ord(a))
                
                    #print (a, end="")
                #print (self.dataf[x][y])
                
 #int(ord(a))
                #print("%X"%i ,i,self.dataf[i])
            print (self.dataf)

            

    def get_imagedata(self):
        return self.dataf

Train_dir = ".\data\\faces_training"

filenames = os.listdir(Train_dir)
for filename in filenames:
    full_filename = os.path.join(Train_dir, filename)
    print (full_filename)
    train_pgm = PGM(full_filename)
   

arr = np.asarray(train_pgm.get_imagedata())
pyplot.imshow(train_pgm.get_imagedata(), pyplot.cm.gray)
pyplot.show()
