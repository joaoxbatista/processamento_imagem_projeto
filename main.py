import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
	Métodos utilitários
'''
def cropt(image, height, width, rgb=False):
	if(rgb):
		(h, w, c) = image.shape
	else:
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


# 3 - determinar o limiar da imagem
ret, img1gb = cv2.threshold (img1g, 110,255, cv2.THRESH_BINARY)
ret, img1gab = cv2.threshold (img1ga, 110,255, cv2.THRESH_BINARY)

fig = plt.gcf()
fig.canvas.set_window_title('iron nodule images + result')

plt.subplot(2, 2, 1)
plt.imshow(cropt(img1, 100, 0, True))
plt.title("normal image")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(cropt(img1a, 100, 0, True))
plt.title("attack image")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(negative(img1gb), cmap = 'gray')
plt.title("normal treshold + invert")
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(negative(img1gab), cmap = 'gray')
plt.title("attack treshold + invert")
plt.xticks([])
plt.yticks([])

plt.show()


# 3 - gerar o histograma da imagem
fig = plt.gcf()
fig.canvas.set_window_title('iron nodule histogram + result')

plt.subplot(2, 2, 1)
plt.hist(img1g.ravel(), 256, [0, 256])
plt.title('normal image'), 
plt.xticks([]), 
plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(img1ga.ravel(), 256, [0, 256])
plt.title('attack image'), 
plt.xticks([]), 
plt.yticks([])


plt.subplot(2, 2, 3)
plt.hist(negative(img1gb).ravel(), 256, [0, 256])
plt.title('normal treshold + invert'), 
plt.xticks([]), 
plt.yticks([])

plt.subplot(2, 2, 4)
plt.hist(negative(img1gab).ravel(), 256, [0, 256])
plt.title('attack treshold + invert'), 
plt.xticks([]), 
plt.yticks([])

plt.show()

# 4 - separar a imagem com base no limiar
# 5 - inverter a imagem
