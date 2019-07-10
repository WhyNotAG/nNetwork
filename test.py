import dlib
import cv2
import tkinter as tk
from skimage import io #загрузка фотографий из файлов
from scipy.spatial import distance 
#расчет евклидового пространства между векторами признаков
def create(ph1,ph2):
	sp = dlib.shape_predictor('/Users/aleksandrgolubkin/Documents/nNetwork/shape_predictor_68_face_landmarks.dat')
# описание модели для выделения на фотографии лица

	facerec = dlib.face_recognition_model_v1('/Users/aleksandrgolubkin/Documents/nNetwork/dlib_face_recognition_resnet_model_v1.dat')
# обученная нейронная сеть

	print(ph1)
	detector = dlib.get_frontal_face_detector()
	img = io.imread(ph1)

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

	img = io.imread(ph2)

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
		result = True
	else:
		result = False

	# dlib.hit_enter_to_continue()
	return result

