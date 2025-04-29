import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
from validador import validar_documento
from ai_analysis import simular_ia_analise
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

dados_usuario = {}

def selecionar_documento():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens e PDFs", "*.png *.jpg *.jpeg *.pdf")])
    if caminho:
        if validar_documento(caminho):
            dados_usuario["documento"] = caminho
            messagebox.showinfo("Sucesso", "Documento carregado e validado com sucesso.")
        else:
            messagebox.showerror("Erro", "Formato de documento inválido.")

def salvar_json(dados):
    with open("perfil_fan.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def gerar_pdf(dados, resultado_ia):
    nome_arquivo = "perfil_fan.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Perfil do Fã de eSports")
    y -= 30

    c.setFont("Helvetica", 12)
    for chave, valor in dados.items():
        texto = f"{chave.capitalize()}: {valor}"
        c.drawString(50, y, texto[:100])
        y -= 20
        if y < 100:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)

    # Análise da IA detalhada
    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Análise por IA:")
    y -= 20

    c.setFont("Helvetica", 11)
    for linha in resultado_ia.split("\n"):
        c.drawString(50, y, linha[:100])
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 11)

    c.save()

    try:
        if os.name == 'nt':  # Windows
            os.startfile(nome_arquivo)
        elif os.name == 'posix':  # Linux ou Mac
            os.system(f"xdg-open '{nome_arquivo}'")
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")


def enviar_dados():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cpf = entry_cpf.get()
    interesses = entry_interesses.get()
    eventos = entry_eventos.get()
    redes = entry_redes.get()
    sites = entry_sites.get()

    campos = [nome, endereco, cpf]
    if not all(campos):
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    dados_usuario.update({
        "nome": nome,
        "endereco": endereco,
        "cpf": cpf,
        "interesses": interesses,
        "eventos": eventos,
        "redes_sociais": redes,
        "sites_esports": sites
    })

    resultado_ia = simular_ia_analise(redes, sites,interesses)
    salvar_json(dados_usuario)
    gerar_pdf(dados_usuario, resultado_ia)

    perfil = f"""
    Nome: {nome}
    Endereço: {endereco}
    CPF: {cpf}
    Interesses: {interesses}
    Eventos: {eventos}
    Documento: {'Enviado' if 'documento' in dados_usuario else 'Não enviado'}
    IA diz: {resultado_ia}
    Arquivos: perfil_fan.json e perfil_fan.pdf gerados com sucesso.
    """
    messagebox.showinfo("Perfil do Fã", perfil)

# Interface com Tkinter
app = tk.Tk()
app.title("Know Your Fan - Cadastro de Fã de eSports")
app.geometry("500x600")

tk.Label(app, text="Nome completo:").pack()
entry_nome = tk.Entry(app, width=50)
entry_nome.pack()

tk.Label(app, text="Endereço:").pack()
entry_endereco = tk.Entry(app, width=50)
entry_endereco.pack()

tk.Label(app, text="CPF:").pack()
entry_cpf = tk.Entry(app, width=50)
entry_cpf.pack()

tk.Label(app, text="Interesses (jogos, times):").pack()
entry_interesses = tk.Entry(app, width=50)
entry_interesses.pack()

tk.Label(app, text="Eventos/compras no último ano:").pack()
entry_eventos = tk.Entry(app, width=50)
entry_eventos.pack()

tk.Button(app, text="Upload de Documento", command=selecionar_documento).pack(pady=5)

tk.Label(app, text="Links de redes sociais:").pack()
entry_redes = tk.Entry(app, width=50)
entry_redes.pack()

tk.Label(app, text="Links de sites de eSports favoritos:").pack()
entry_sites = tk.Entry(app, width=50)
entry_sites.pack()

tk.Button(app, text="Enviar", command=enviar_dados).pack(pady=10)

app.mainloop()
