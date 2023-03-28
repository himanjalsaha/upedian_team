# run pip install comtypes
import os
import comtypes.client
import time
wdFormatPDF = 17
# absolute path is needed
# be careful about the slash '\', use '\\' or '/' or raw string r"..."
in_file=input(r'absolute path of input docx file 1: ')
out_file=input(r'absolute path of output pdf file 1: ')

'''in_file2=input(r'absolute path of input docx file 2')
out_file2=input(r'absolute path of outputpdf file 2')
'''
# print out filenames
print (in_file)
print (out_file)
'''print (in_file2)
print (out_file2)'''
# create COM object
word = comtypes.client.CreateObject('Word.Application')
# key point 1: make word visible before open a new document
word.Visible = True
# key point 2: wait for the COM Server to prepare well.
time.sleep(3)
# convert docx file 1 to pdf file 1
doc=word.Documents.Open(in_file) # open docx file 1
doc.SaveAs(out_file, FileFormat=wdFormatPDF) # conversion
doc.Close() # close docx file 1
word.Visible = False
#if 2 files then adding this code
'''# convert docx file 2 to pdf file 2
doc = word.Documents.Open(in_file2) # open docx file 2
doc.SaveAs(out_file2, FileFormat=wdFormatPDF) # conversion
doc.Close() # close docx file 2   
word.Quit() # close Word Application'''