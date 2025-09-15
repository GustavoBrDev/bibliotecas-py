import cv2

imagem = cv2.imread('images/weg-propaganda.jpg')

vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)

# Linhas ( imagem, começo, fim, cor )
cv2.line(imagem, (0, 0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)

# Retângulo ( imagem, começo, fim, cor, altura? )
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)

# ?
(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)

# Círculos
for raio in range(0, 175, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho)


# Adicionando texto
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte,2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)

