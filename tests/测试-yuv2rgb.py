# import cv2
# # fileName = "../Track_keyPoint/ignore_video/DecodedVideo.yuv"
# fileName = "../Track_keyPoint/ignore_video/001_out.jpg"
# img = cv2.imread(fileName)
# # print(img)

# cv2.imshow('img', img)
# cv2.waitKey(0)

import PIL
import  numpy as np
from PIL import Image


def readYuvFile(filename,width,height):
    fp=open(filename,'rb')
    # uv_width=width//2
    uv_width=width//2
    uv_height=height//2

    Y=np.zeros((height,width), np.uint8,'C')
    U=np.zeros((uv_height,uv_width), np.uint8,'C')
    V=np.zeros((uv_height,uv_width), np.uint8,'C')

    for m in range(height):
        for n in range(width):
            Y[m,n]=ord(fp.read(1))
    for m in range(uv_height):
        for n in range(uv_width):
            V[m,n]=ord(fp.read(1))
            U[m,n]=ord(fp.read(1))

    fp.close()
    return (Y,U,V)

def yuv2rgb(Y,U,V,width,height):

    U=np.repeat(U,2,0)
    U=np.repeat(U,2,1)

    V=np.repeat(V,2,0)
    V=np.repeat(V,2,1)

    rf=np.zeros((height,width),float,'C')
    gf=np.zeros((height,width),float,'C')
    bf=np.zeros((height,width),float,'C')

    rf=Y+1.14*(V-128.0)
    gf=Y-0.395*(U-128.0)-0.581*(V-128.0)
    bf=Y+2.032*(U-128.0)

    for m in range(height):
        for n in range(width):
            if(rf[m,n]>255):
                rf[m,n]=255;
            if(gf[m,n]>255):
                gf[m,n]=255;
            if(bf[m,n]>255):
                bf[m,n]=255;

    r=rf.astype(np.uint8)
    g=gf.astype(np.uint8)
    b=bf.astype(np.uint8)
    return (r,g,b)

if __name__=='__main__':
    width=1920
    height=1080
    data=readYuvFile('../Track_keyPoint/ignore_video/DecodedVideo.yuv', width, height)
    Y=data[0]
    im=Image.frombytes('L',(width,height),Y.tostring())
    # im.save('/home/sl/y.bmp')
    im.show()
