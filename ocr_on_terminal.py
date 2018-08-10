#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: vysh
"""

#Make sure this script is in the same folder as the file from which text is to be extracted

from wand.image import Image as wi
from autocorrect import spell
from PIL import Image
import pytesseract
import os
import io


def imgOcrEng(file_name):
	im = Image.open(file_name)
	text = pytesseract.image_to_string(im, lang='eng')

	fin = open('temp-extracted.txt','w')
	fin.write(text)
	fin.close()

	fhand = open('temp-extracted.txt')
	fout = open('extracted.txt','w')


	for line in fhand:
	    line.rstrip()
	    words=line.split()
	    for word in words:
	        word=spell(word)+' '
	        fout.write(word)
	    fout.write('\n')
	fout.close()

	f = open("extracted.txt", "r")
	text = f.read()
	f.close()

	os.remove("temp-extracted.txt")
	#os.remove("extracted.txt")
	return text



def pdfOcrEng(file_name):
    pdf = wi(filename = file_name, resolution = 300)
    pdfImage = pdf.convert('jpeg')

    imageBlobs = []

    for img in pdfImage.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob('jpeg'))

    extracted_text = []

    for imgBlob in imageBlobs:
        im = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(im, lang = 'eng')
        extracted_text.append(text)

    fin = open('temp-extracted.txt','w')
    fin.writelines(["%s\n" % item  for item in extracted_text])
    fin.close()

    fhand = open('temp-extracted.txt')
    fout = open('extracted.txt','w')

    for line in fhand:
        line.rstrip()
        words=line.split()
        for word in words:
            word=spell(word)+' '
            fout.write(word)
        fout.write('\n')
    fout.close()


    f = open("extracted.txt", "r")
    text = f.read()
    f.close()

    os.remove("temp-extracted.txt")
    #os.remove("extracted.txt")
    return text



def imgOcrKan(file_name):
 	im = Image.open(file_name)
 	text = pytesseract.image_to_string(im, lang='kan')

 	fout = open('extracted.txt','w')
 	fout.write(text)
 	fout.close()

 	return text



def pdfOcrKan(file_name):
	pdf = wi(filename = file_name, resolution = 300)
	pdfImage = pdf.convert('jpeg')

	imageBlobs = []

	for img in pdfImage.sequence:
		imgPage = wi(image = img)
		imageBlobs.append(imgPage.make_blob('jpeg'))

	extracted_text = []

	for imgBlob in imageBlobs:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'eng')
		extracted_text.append(text)

	fin = open('extracted.txt','w')
	fin.writelines(["%s\n" % item  for item in extracted_text])
	fin.close()

	f = open('extracted.txt','r')
	text = f.read()
	f.close()

	return text



def imgOcrTam(file_name):
 	im = Image.open(file_name)
 	text = pytesseract.image_to_string(im, lang='tam')

 	fout = open('extracted.txt','w')
 	fout.write(text)
 	fout.close()

 	return text



def pdfOcrTam(file_name):
	pdf = wi(filename = file_name, resolution = 300)
	pdfImage = pdf.convert('jpeg')

	imageBlobs = []

	for img in pdfImage.sequence:
		imgPage = wi(image = img)
		imageBlobs.append(imgPage.make_blob('jpeg'))

	extracted_text = []

	for imgBlob in imageBlobs:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'tam')
		extracted_text.append(text)

	fin = open('extracted.txt','w')
	fin.writelines(["%s\n" % item  for item in extracted_text])
	fin.close()

	f = open('extracted.txt','r')
	text = f.read()
	f.close()

	return text



def imgOcrTel(file_name):
 	im = Image.open(file_name)
 	text = pytesseract.image_to_string(im, lang='tel')

 	fout = open('extracted.txt','w')
 	fout.write(text)
 	fout.close()

 	return text



def pdfOcrTel(file_name):
	pdf = wi(filename = file_name, resolution = 300)
	pdfImage = pdf.convert('jpeg')

	imageBlobs = []

	for img in pdfImage.sequence:
		imgPage = wi(image = img)
		imageBlobs.append(imgPage.make_blob('jpeg'))

	extracted_text = []

	for imgBlob in imageBlobs:
		im = Image.open(io.BytesIO(imgBlob))
		text = pytesseract.image_to_string(im, lang = 'tel')
		extracted_text.append(text)

	fin = open('extracted.txt','w')
	fin.writelines(["%s\n" % item  for item in extracted_text])
	fin.close()

	f = open('extracted.txt','r')
	text = f.read()
	f.close()

	return text

def main():
	print("Optical Character Recognition.\n")
	lang_choice = int(input("Select Language:\n\n1.English\n2.Kannada\n3.Tamil\n4.Telegu\n"))
	file_type = int(input("\nSelect the file type:\n1.Image\n2.pdf\n"))
	file_name = input("\nEnter the file name: ")

	if lang_choice == 1:
		if file_type == 1:
			text = imgOcrEng(file_name)
			print(text)
		elif file_type == 2:
			text = pdfOcrEng(file_name)
			print(text)
		else:
			print("Invalid Choice.")
			return

	elif lang_choice == 2:
		if file_type == 1:
			text = imgOcrKan(file_name)
			print(text)
		elif file_type == 2:
			text = pdfOcrKan(file_name)
			print(text)
		else:
			print("Invalid Choice.")
			return


	elif lang_choice == 3:
		if file_type == 1:
			text = imgOcrTam(file_name)
			print(text)
		elif file_type == 2:
			text = pdfOcrTam(file_name)
			print(text)
		else:
			print("Invalid choice.")
			return


	elif lang_choice == 4:
		if file_type == 1:
			text = imgOcrTel(file_name)
			print(text)
		elif file_type == 2:
			text = pdfOcrTel(file_name)
			print(text)
		else:
			print("Invalid Choice.")
			return

	else:
		print("Invalid choice.")
		return

	print("\n\nExtracted text can also be found in the same folder in a file- 'extracted.txt'\n")

	return

if __name__== "__main__":
  main()
