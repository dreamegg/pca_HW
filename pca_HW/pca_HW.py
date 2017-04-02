
#with codecs.open("face01.pgm", "r",encoding='utf-8', errors='ignore') as f:
import numpy as np
from matplotlib import pyplot

class PGM(object):
    def __init__(self, filepath):
        with open(filepath, "r",encoding='utf-8', errors='ignore') as f:
            header = f.read(15)
            print(header)
            self.type = header[0:2]
            self.width = int(header[3:6])
            self.height = int(header[7:10])
            self.maxval = int(header[11:14])
            self.datalen = self.width* self.height

            self.data = f.read(self.datalen)



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
'''
mypgm = PGM('face01.pgm')
#pyplot.imshow(image, pyplot.cm.gray)
pyplot.show()
