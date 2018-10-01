import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
	Métodos utilitários
'''
def cropt(image, height, width):
	(h, w) = image.shape
	return image[0:(h-height), 0:(w-width)]

def negative(image):
	return (255 - image)

# 0 - ler imagem
img1 = cv2.imread('images/1.jpg')
img1a = cv2.imread('images/1a.jpg')

# 1 - converter imagem para 8 bits
img1g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1ga = cv2.cvtColor(img1a, cv2.COLOR_BGR2GRAY)

# 2 - cortar a imagem para remover faixa branca 
img1g = cropt(img1g, 100, 0)
img1ga = cropt(img1ga, 100, 0)

# # 3 - visualizar imagem 
# plt.subplot(121),plt.imshow(img1g, cmap = 'gray')
# plt.title('Imagem sem ataque quimico'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(img1ga, cmap = 'gray')
# plt.title('Imagem com ataque quimico'), plt.xticks([]), plt.yticks([])
# plt.show()

# # 2 - gerar o histograma da imagem
# plt.hist(img1g.ravel(), 256, [0, 256])
# plt.show()
# plt.hist(img1ga.ravel(), 256, [0, 256])
# plt.show()

# 3 - determinar o limiar da imagem
ret, img1gb = cv2.threshold (img1g, 110,255, cv2.THRESH_BINARY)
ret, img1gab = cv2.threshold (img1ga, 110,255, cv2.THRESH_BINARY)

plt.subplot(1, 2, 1,)
plt.imshow(negative(img1gb), cmap = 'gray')
plt.title("Figure 1: normal image")

plt.subplot(1, 2, 2)
plt.imshow(negative(img1gab), cmap = 'gray')
plt.title("Figure 2: attack image")

plt.show()

# 4 - separar a imagem com base no limiar
# 5 - inverter a imagem
