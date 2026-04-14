import cv2
import numpy as np

def criar_imagem_autoral(largura=640, altura=360):
    """
    Gera uma imagem autoral (criada por código) em BGR (padrão do OpenCV),
    com gradiente + formas + texto.
    """
    img = np.zeros((altura, largura, 3), dtype=np.uint8)

    # Gradiente no canal azul e verde (autoral)
    for x in range(largura):
        azul = int(255 * (x / (largura - 1)))
        verde = int(255 * (1 - x / (largura - 1)))
        img[:, x] = (azul, verde, 80)

    # Formas geométricas (autoral)
    cv2.circle(img, (int(largura * 0.25), int(altura * 0.5)), 60, (0, 0, 255), -1)      # círculo vermelho
    cv2.rectangle(img, (int(largura * 0.55), int(altura * 0.35)),
                  (int(largura * 0.85), int(altura * 0.75)), (255, 255, 255), 3)       # retângulo branco
    cv2.line(img, (0, altura - 1), (largura - 1, 0), (0, 255, 255), 2)                  # linha amarela

    # Texto (autoral)
    cv2.putText(img, "Smoke Test - OpenCV", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (20, 20, 20), 3, cv2.LINE_AA)
    cv2.putText(img, "Imagem autoral gerada por codigo", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 20, 20), 2, cv2.LINE_AA)

    return img

def main():
    # 1) Cria imagem autoral
    colorida = criar_imagem_autoral()

    # 2) Converte para tons de cinza
    cinza = cv2.cvtColor(colorida, cv2.COLOR_BGR2GRAY)

    # (Opcional) salvar a imagem em disco como evidência também
    cv2.imwrite("imagem_autoral_cinza.png", cinza)

    # 3) Abre janela nativa com cv2.imshow
    janela = "Smoke Test - Tons de Cinza (pressione Q para sair)"
    cv2.imshow(janela, cinza)

    # Mantém a janela aberta até apertar Q ou ESC
    while True:
        key = cv2.waitKey(20) & 0xFF
        if key in (ord('q'), 27):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()