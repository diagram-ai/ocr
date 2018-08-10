# Optical Character Recogniton

This project is implemented using Tesseract OCR for character recogniton in images and pdf.

Currently 4 languages are supported, English, Kannada, Tamil and Telegu.

A web interface is developed using Django framework, which allows users to upload an image or a pdf onto the webpage that returns the text grabbed from the file uploaded.

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

To download the trained data for Kannada,Tamil and Telegu, go to
`https://github.com/indic-ocr/tessdata/`
The respective trained data will be found in the folders `kan` `tam` and `tel`. Download and copy those file into `tessdata` in your local folder where `tesseract` is installed.

## Procedure:

At the terminal, go to the folder containing the project and type the following command to start the localhost server.
> python manage.py runserver

To tag the few proper nouns in english that might not be recognised corectly, run the `filtered.py` script.

`filtered.py` depends on nltk tokenizing modules. To install them, run-

> nltk.download('punkt')

#### The extraction is quite resource intensive and takes time(depends on the hardware used), especially if the uploaded file is a large pdf. It is advised to break the pdf into chunks of a couple of pages(8-10) per file and uploading them for quicker results.

The extracted text can also be found int the project folder in a text file `extracted.txt`.


#### To run extract text without web interface:
Install the dependencies mentioned earlier and just download the `ocr_on_terminal.py` file. Copy the file(from which text is to be extracted) into the folder containing `ocr_on_terminal_on_terminal_on_terminal.py`.

Run `ocr_on_terminal_on_terminal.py` on the command prompt/terminal.
> python ocr_on_terminal.py

Extracted text can also be found in `extracted.txt` inside the same directory. 


##### Note: If you are facing an error saying `normproto file is not in unichar set`, you have to install the support for indian languages' character set.

