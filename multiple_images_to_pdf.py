# run pip install Pillow before using
import sys
from PIL import Image
a=input("how many images do you want to convert to pdf?(max 6): ")
if a=='1' or a=='one':
    b=input("enter the path to the image that you want to convert: ")
    c=input("enter the path where you want to save the pdf: ")
    d=input("enter the name of the pdf that you want to save: ")
    e=c+'\\'
    f=e+d+'.pdf'
    image1=Image.open(b)
    im1=image1.convert('RGB')
    im1.save(f)
    print("FINISHED!!!")
    sys.exit()
elif a=='2' or a=='two':
    b=input("enter the path to the first image that you want to convert: ")
    c=input("enter the path to the second image that you want to convert: ")
    d=input("enter the path where you want to save the pdf: ")
    e=input("enter the name of the pdf that you want to save: ")
    f=c+'\\'
    g=e+d+'.pdf'
    image1=Image.open(b)
    image2=Image.open(c)
    im1=image1.convert('RGB')
    im2=image2.convert('RGB')
    imagelist = [im2]
    im1.save(g,save_all=True, append_images=imagelist)
    print("FINISHED!!!")
    sys.exit()
elif a=='3' or a=='three':
    a=input("enter the path to the first image that you want to convert: ")
    b=input("enter the path to the second image that you want to convert: ")
    c=input("enter the path to the third image that you want to convert: ")
    d=input("enter the path where you want to save the pdf: ")
    e=input("enter the name of the pdf that you want to save: ")
    f=d+'\\'
    g=f+e+'.pdf'
    image1=Image.open(a)
    image2=Image.open(b)
    image3=Image.open(c)
    im1=image1.convert('RGB')
    im2=image2.convert('RGB')
    im3=image3.convert('RGB')
    imagelist = [im2,im3]
    im1.save(g,save_all=True, append_images=imagelist)
    print("FINISHED!!!")
    sys.exit()
elif a=='4' or a=='four':
    a=input("enter the path to the first image that you want to convert: ")
    b=input("enter the path to the second image that you want to convert: ")
    c=input("enter the path to the third image that you want to convert: ")
    d=input("enter the path to the forth image that you want to convert: ")
    e=input("enter the path where you want to save the pdf: ")
    f=input("enter the name of the pdf that you want to save: ")
    g=e+'\\'
    h=g+f+'.pdf'
    image1 = Image.open(a)
    image2 = Image.open(b)
    image3 = Image.open(c)
    image4 = Image.open(d)
    im1 = image1.convert('RGB')
    im2 = image2.convert('RGB')
    im3 = image3.convert('RGB')
    im4 = image4.convert('RGB')
    imagelist = [im2,im3,im4]
    im1.save(h,save_all=True, append_images=imagelist)
    print("FINISHED!!!")
    sys.exit()
elif a=='5' or a=='five':
    a=input("enter the path to the first image that you want to convert: ")
    b=input("enter the path to the second image that you want to convert: ")
    c=input("enter the path to the third image that you want to convert: ")
    d=input("enter the path to the forth image that you want to convert: ")
    e=input("enter the path to the fifth image that you want to convert: ")
    f=input("enter the path where you want to save the pdf: ")
    g=input("enter the name of the pdf that you want to save: ")
    h=f+'\\'
    i=h+g+'.pdf'
    image1 = Image.open(a)
    image2 = Image.open(b)
    image3 = Image.open(c)
    image4 = Image.open(d)
    image5 = Image.open(e)
    im1 = image1.convert('RGB')
    im2 = image2.convert('RGB')
    im3 = image3.convert('RGB')
    im4 = image4.convert('RGB')
    im5 = image5.convert('RGB')
    imagelist = [im2,im3,im4,im5]
    im1.save(h,save_all=True, append_images=imagelist)
    print("FINISHED!!!")
    sys.exit()
elif a=='6' or a=='six':
    a=input("enter the path to the first image that you want to convert: ")
    b=input("enter the path to the second image that you want to convert: ")
    c=input("enter the path to the third image that you want to convert: ")
    d=input("enter the path to the forth image that you want to convert: ")
    e=input("enter the path to the fifth image that you want to convert: ")
    f=input("enter the path to the sixth image that you want to convert: ")
    g=input("enter the path where you want to save the pdf: ")
    h=input("enter the name of the pdf that you want to save: ")
    i=g+'\\'
    j=i+h+'.pdf'
    image1 = Image.open(a)
    image2 = Image.open(b)
    image3 = Image.open(c)
    image4 = Image.open(d)
    image5 = Image.open(e)
    image6 = Image.open(f)
    im1 = image1.convert('RGB')
    im2 = image2.convert('RGB')
    im3 = image3.convert('RGB')
    im4 = image4.convert('RGB')
    im5 = image5.convert('RGB')
    im6 = image6.convert('RGB')
    imagelist = [im2,im3,im4,im5,im6]
    im1.save(h,save_all=True, append_images=imagelist)
    print("FINISHED!!!")
    sys.exit()