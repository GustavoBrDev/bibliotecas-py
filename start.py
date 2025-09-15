

# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('images/weg-propaganda.jpg')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem

print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem

print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Lendo o valor de um pixel
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB

print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# Modificando a imagem
for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
        imagem[y:y+5, x: x+5] = (255,0,0)

#Cria um retangulo azul por toda a largura da imagem
imagem[30:50, :] = (255, 0, 0)

#Cria um quadrado vermelho
imagem[100:150, 50:100] = (0, 0, 255)

#Cria um retangulo amarelo por toda a altura da imagem
imagem[:, 200:220] = (0, 255, 255)

#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
imagem[150:300, 250:350] = (0, 255, 0)

#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
imagem[300:400, 50:150] = (255, 255, 0)

#Cria um quadrado branco
imagem[250:350, 300:400] = (255, 255, 255)

#Cria um quadrado preto
imagem[70:100, 300: 450] = (0, 0, 0)


# Mostra a imagem com a função imshow
cv2.imshow("Visualizando Imagem", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla

# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
