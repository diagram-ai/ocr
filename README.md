# Optical Character Recogniton

This project is implemented using Tesseract OCR for character recogniton in images and pdf.

Currently 2 languages are supported, English and Kannada.

A web interface is developed using Django framework, which allows users to upload an image or a pdf on the webpage that returns the text grabbed from the file uploaded.

### Dependencies:

To install Django:

> pip install Django

Install dependencies for ocr:

> sudo apt-get install tesseract-ocr

> pip install pytesseract

To work with images:

> sudo pip install pillow

To work with pdf:

> sudo apt-get install imagemagick

> pip install wand

Other dependencies:

> pip install autocorrect

To download the trained data for Kannada, go to 
`https://github.com/indic-ocr/tessdata/blob/master/kan/kan.traineddata`
and paste that file in tessdata in your local folder where tesseract is installed.

## Procedure:

At the terminal, go to the folder containing the project and type the following command to start the localhost server.
> python manage.py runserver

To tag the few proper nouns in english that might not be recognised corectly, run the `filtered.py` script.

`filtered.py` depends on nltk tokenizing modules. To install them, run-

> nltk.download('punkt')

#### The extraction is quite resource intensive and takes time(depends on the hardware used), especially if the uploaded file is a large pdf. It is advised to break the pdf into chunks of a couple of pages(5-6) per file and uploading them for quicker results.

The extracted text can also be found int the project folder in a text file `extracted.txt`.
