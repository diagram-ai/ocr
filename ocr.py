#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: vysh
"""

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
	fout = open('img-eng-extracted.txt','w')


	for line in fhand:
	    line.rstrip()
	    words=line.split()
	    for word in words:
	        word=spell(word)+' '
	        fout.write(word)
	    fout.write('\n')
	fout.close()

	f = open("img-eng-extracted.txt", "r")
	text = f.read()
	f.close()

	os.remove("temp-extracted.txt")
	os.remove("img-eng-extracted.txt")
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

    fin = open('extracted.txt','w')
    fin.writelines(["%s\n" % item  for item in extracted_text])
    fin.close()

    fhand = open('extracted.txt')
    fout = open('pdf-eng-extracted.txt','w')

    for line in fhand:
        line.rstrip()
        words=line.split()
        for word in words:
            word=spell(word)+' '
            fout.write(word)
        fout.write('\n')
    fout.close()


    f = open("pdf-eng-extracted.txt", "r")
    text = f.read()
    f.close()

    os.remove("extracted.txt")
    os.remove("pdf-eng-extracted.txt")
    return text



def imgOcrKan(file_name):
 	im = Image.open(file_name)
 	text = pytesseract.image_to_string(im, lang='kan')
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

	fin = open('pdf-kan-extracted.txt','w')
	fin.writelines(["%s\n" % item  for item in extracted_text])
	fin.close()

	return extracted_text