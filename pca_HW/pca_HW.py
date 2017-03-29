
#with codecs.open("face01.pgm", "r",encoding='utf-8', errors='ignore') as f:
import numpy as np
from matplotlib import pyplot
import codecs
import image

class PGM(object):
    def __init__(self, filepath):

        with codecs.open(filepath, "r",encoding='utf-8', errors='ignore') as f:
            # suppose all header info in first line:
            info = f.readline().split()
            self.type = info[0]
            info = f.readline().split()        
            self.width = int(info[0])
            self.height = 98 #int(info[1])
            info = f.readline().split()        
            self.maxval = int(info[0])
            size = self.width * self.height

            buffer = f.read()
            print(len(buffer))
            self.data =[]
            for i in range(size):
                self.data.append(ord(buffer[i]))
            print(self.data)
            np.reshape(self.data, (self.width , int(len(buffer)/self.width)))
            print(self.data)


    def get_img(self):
        if self._img is None:
            # only executed once
            size = (self.width, self.height)
            mode = 'L'
            data = self.data
            #self.img = Image.frombuffer(mode, size, data)

        return self.img

    def get_imagedata(self):
        return self.data

    Image = property(get_img)

mypgm = PGM('face01.pgm')
image = mypgm.get_imagedata
#pyplot.imshow(image, pyplot.cm.gray)
pyplot.show()
