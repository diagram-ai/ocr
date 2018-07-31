from django.shortcuts import render
import random
import ocr
import os

images = ["png", "jpg", "jpeg", "bmp", "gif"]


def generate_file_name():
	while 1:
		x = str(random.random())[2:]
		return x


def index(request):
	if request.method == "GET":
		return render(request, 'kan/upload.html', {"result": False})

	if request.method == "POST":
		files = request.FILES

		extension = str(files["image"]).split(".")[-1]

		image_data = b""
		for chunk in files["image"].chunks():
			image_data += chunk

		file_name = generate_file_name() + "." + extension
		f = open(file_name, "wb")
		f.write(image_data)
		f.close()

		type = "image" if extension in images else ("pdf" if extension == "pdf" else "null")

		print(type)


		# OCR function call
		if type == "image":
			text = ocr.imgOcrKan(file_name)

		elif type == "pdf":
			text = str(ocr.pdfOcrKan(file_name))

		else:
			text = 'UPLOAD ONLY IMAGE OR PDF.'


		#os.remove(file_name)

		return render(request, 'kan/upload.html', {"result": text})





	#render looks in the templates directory
	#if you have multiple apps, create another directory for the app
	#in templates directory to avoid conflicting names
