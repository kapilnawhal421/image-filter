import PIL
import numpy as np
from PIL import Image
from numpy import asarray
# load the image
my_image = Image.open('D:\image\images(4).jpg')
# convert image to numpy array
data = asarray(my_image)
print(type(data))
# summarize shape
print(data.shape)
print(np.std(data))
data2=data.copy()
print(data2.min())
data_shape=list(data2.shape)
a=data2.argmin()
b=a//data_shape[2]
depth=b//data_shape[1]
row=b%data_shape[1]
coloum=a%data_shape[2]
data2[depth,row,coloum]=-9000
print(data2.min())
print(data2.max())
e=data2.argmax()
f=e//data_shape[2]
depth2=f//data_shape[1]
row2=f%data_shape[1]
coloum2=e%data_shape[2]
data2[depth2,row2,coloum2]=data2[depth2,row2,coloum2]+90000
print(data2.max())
print(data2[0,0,0])
data2[0,0,0]=-2
print(data2[0,0,0])
print(data2[0,0,0])
data2[0,0,0]=-2
print(data2[0,0,0])
print(data2[depth,row,coloum])
#create Pillow image
#data3=data2.resize(300,300,3)
i=0
j=0
k=0
while(i<data_shape[0]):
    j=0
    while(j<data_shape[1]):
        k=0
        while(k<data_shape[2]):
            if(data2[i][j][k]<30 and data2[i][j][k]>0):
                data2[i][j][k]=0
            k=k+1
        j=j+1
    i=i+1
i=0
j=0
k=0
while(i<data_shape[0]):
    j=0
    while(j<data_shape[1]):
        k=0
        while(k<data_shape[2]):
            if(data2[i][j][k]<255 and data2[i][j][k]>220):
                data2[i][j][k]=255
            k=k+1
        j=j+1
    i=i+1
"""i=0
j=0
k=0
while(i<data_shape[0]):
    j=0
    while(j<data_shape[1]):
        k=0
        while(k<data_shape[2]):
            if(data2[i][j][k]<127 and data2[i][j][k]>110):
                data2[i][j][k]=127
            k=k+1
        j=j+1
    i=i+1
i=0
j=0
k=0
while(i<data_shape[0]):
    j=0
    while(j<data_shape[1]):
        k=0
        while(k<data_shape[2]):
            if(data2[i][j][k]<145 and data2[i][j][k]>127):
                data2[i][j][k]=127
            k=k+1
        j=j+1
    i=i+1
"""
"""data3R=data2.copy()
data3R[:,:,0]=127
data3R[:,:,1]=127
data3R[:,:,2]=127"""
imagex = Image.fromarray(data2)
print(data2)

# summarize image details
print(imagex.mode)
print(imagex.size)
imagex.save("ein1.jpg")
print(data2.dtype)
print(np.std(data2))
