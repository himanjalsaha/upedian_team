# run pip install Pillow before using
import sys
from PIL import Image
a=input("enter the path to the image that you want to convert: ")
b=input("enter the path where you want to save the pdf: ")
c=input("enter the name of the pdf that you want to save: ")
d=b+'\\'
e=d+c+'.pdf'
image1=Image.open(a)
im1=image1.convert('RGB')
im1.save(e)
print("FINISHED!!!")
sys.exit()