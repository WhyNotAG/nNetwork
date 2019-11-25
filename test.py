import dlib
import cv2
import base64
import tkinter as tk
from skimage import io #загрузка фотографий из файлов
from scipy.spatial import distance
from io import StringIO
import sqlite3 as lite
import sys


def img_to_base64(ph):
	with open(ph, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
	return encoded_string

def base64_to_img(strBase):
	with open("imageToSave.png", "wb") as fh:
		fh.write(base64.decodebytes(strBase))


#расчет евклидового пространства между векторами признаков
def create(ph1):

	con = lite.connect('face.db')

	sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# описание модели для выделения на фотографии лица


	facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
# обученная нейронная сеть

	print(ph1)
	detector = dlib.get_frontal_face_detector()
	img = io.imread(ph1)
	bs64 = img_to_base64(ph1)
	print(bs64)
	base64_to_img(bs64)

	win1 = dlib.image_window()
	win1.clear_overlay()
	win1.set_image(img)
	dets = detector(img,1)


	for k,d in enumerate(dets):
		print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
			k, d.left, d.top(), d.right(), d.bottom()))
		shape = sp(img,d)

		win1.clear_overlay()
		win1.add_overlay(d)
		win1.add_overlay(shape)

	cv2.imwrite("out1.jpg", img)
# dlib.hit_enter_to_continue()
	face_descriptot1 = facerec.compute_face_descriptor(img,shape)

# print(face_descriptot1)

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM face")
		rows = cur.fetchall()

		for row in rows:
			text = row[1]
			img = io.imread(text)

			win2 = dlib.image_window()
			win2.clear_overlay()
			win2.set_image(img)
			dets_webcam = detector(img,1)

			for k,d in enumerate(dets_webcam):
				print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
					k, d.left, d.top(), d.right(), d.bottom()))
	# cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255, 255, 255), 2)
				shape = sp(img,d)

				win2.clear_overlay()
				win2.add_overlay(d)
				win2.add_overlay(shape)

# cv2.imwrite("out2.jpg", img)

			face_descriptot2 = facerec.compute_face_descriptor(img,shape)

			a = distance.euclidean(face_descriptot1, face_descriptot2)

			if (a <= 0.55):
				result = row[0]
				break
			else:
				result = "Error"

	# dlib.hit_enter_to_continue()

	return result

