import os
import shutil
import sys


def organizar_por_extensao (diretorio):
    if not os.path.isdir(diretorio):
        print("O caminho fornecido não é uma pasta válida ")
        return
    
    categorias = {
        "Documentos":[".doc",".docx",".pdf", ".txt"],
        "Planilhas": [".xls", ".xlsx", ".csv"],
        "Apresentações": [".ppt", ".pptx"],
        "Imagens": [".jpg",".jpeg",".gif",".png", ".bmp",".dib",".rle",".ico"],
        "Videos": [".mp4", ".avi",".mov"],
        "Áudios": [".mp3",".wav",".aac",".au"],
        "Compactados": [".zip",".rar",".7z"],
        "Instaladores": [".exe", ".msi"],
        "Photoshop&Corel":[".psd", ".cdr", ".cdx", ".cdt", ".drw"]
    }


    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue

        _, extensao = os.path.splitext(arquivo)

        destino = None
        for categoria, extensoes in categorias.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(diretorio, categoria)
                break

        if destino:
            os.makedirs(destino, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(destino, arquivo))
            print(f"Movido: {arquivo} →  {destino}")
        else:
            outros = os.path.join(diretorio, "Outros")
            os.makedirs(outros, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(outros, arquivo))
            print(f"Movido: {arquivo} → {outros}")

if __name__ == "__main__":
    if len(sys.argv)< 2:
        print("Erro: Nenhum caminho foi fornecido.")
    else: 
        caminho_pasta = sys.argv[1]
        organizar_por_extensao(caminho_pasta)