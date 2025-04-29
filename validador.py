import os

def validar_documento(caminho):
    extensoes_validas = [".png", ".jpg", ".jpeg", ".pdf"]
    _, ext = os.path.splitext(caminho)
    return ext.lower() in extensoes_validas

def validar_link(link):
    return link.startswith("http://") or link.startswith("https://")
