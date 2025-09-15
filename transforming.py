import cv2
import imutils

imagem = cv2.imread('images/weg-propaganda.jpg')

# recorte = imagem[100:200, 100:200]
# cv2.imshow("Recorte da imagem", recorte)

cv2.imshow("Original", imagem)

proporcao = 100.0 / imagem.shape[1]
tamanho_novo = (100, int(imagem.shape[0] * proporcao))
img_redimensionada = cv2.resize(imagem, tamanho_novo,
interpolation = cv2.INTER_AREA)

cv2.imshow("Redimensionada", img_redimensionada)
cv2.waitKey(0)

