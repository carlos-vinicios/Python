import cv2
import numpy as np

#Abrindo, exibindo e mostrando informações sobre uma imagem
#a = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/rick1.jpg", 0) #ler uma imagem

#cv2.imshow("Mostrando Imagem", a) #mostra a imagem em uma janela
#cv2.waitKey(0) #mostra a imagem até uma entrada do teclado

#cv2.imwrite("Imagem_cinza.jpg", a) #salva a imagem ( padrão = local do arquivo .py)

#print(a.shape)
#print(a.size)
#print(a.dtype)

#Criando uma imagem vermelha
# a = np.zeros([400, 300, 3], dtype=np.uint8)
#
# a[:, :, 0] = 255 #todos os pixels de todas as linhas e colunas, modifiquem a primeira dimensão para azul
# a[:100, :100] = [0, 0, 255] #alterando os pixels das primeiras 100 linhas e 100 colunas para vermelho
#
# cv2.imshow("Imagem", a)
# cv2.waitKey(0)


#Realiza uma mine transição de imagens
# a = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/rick1.jpg")
# b = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/rick2.jpg")
#
# peso1 = 1
# peso2 = 0
#
# for i in range(10):
#     slide = cv2.addWeighted(a, peso1, b, peso2, 0) #adiciona as imagens estabelecendo peso para cada uma
#     cv2.imshow("Mostrando Slide", slide)
#     cv2.waitKey(1000) #mostra a imagem até uma entrada do teclado
#
#     peso1 -= 0.1
#     peso2 += 0.1
#
# cv2.waitKey(0)

#Blur de imagem
# a = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/Vindicators.png")
#
# cv2.imshow("Antes do Blur", a)
#
# blur_a = cv2.GaussianBlur(a, (11,11), 1)
#
# cv2.imshow("Depois do Blur", blur_a)
#
# cv2.waitKey(0)

#Remover ruídos
# a = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/ruidos.png")
#
# blur_a = cv2.medianBlur(a, 5) #blur mediano para remoção de ruídos
#
# cv2.imshow("Depois do Blur", blur_a)
# cv2.waitKey(0)

#Criação de mascaras
a = cv2.imread("/home/carlos_vinicios/Downloads/Imagens OpenCV/Googlelogo.png")

lin, col = a.shape[:2] #pega as dimensões da imagem

newLin = int(lin*0.6) #pega apenas 60% do seu tamanho (Largura x Altura)
newCol = int(lin*0.6)

new_a = cv2.resize(a, (newCol, newLin)) #redimensiona a imagem

new_a = cv2.cvtColor(new_a, cv2.COLOR_BGR2GRAY)

#só funciona com imagens já em escala de cinza, pois não reconhece o RGB
ret, thresh = cv2.threshold(new_a, 0, 255, cv2.THRESH_BINARY) #ret é o limiar do que o algoritmo escolheu

b = np.zeros((newLin, newCol, 3), dtype=np.uint8)

b[:, :, 0] = 255

cv2.imshow("Mascara", thresh)
cv2.imshow("Azulão", b)

g_a = cv2.bitwise_and(b, b, mask=thresh) #compara duas imagens baseado na mascara

cv2.imshow("Google Azulão", g_a)

cv2.waitKey(0)
