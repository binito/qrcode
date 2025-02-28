import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Função para gerar e salvar o QR Code
def gerar_qrcode():
    # Obtém o link a partir do campo de entrada
    link = entry_link.get()
    
    # Verifica se o link não está vazio
    if not link:
        messagebox.showerror("Erro", "Por favor, insira um link.")
        return
    
    # Cria o QR code a partir do link
    qr = qrcode.QRCode(
        version=1,  # Tamanho do QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erro
        box_size=10,  # Tamanho de cada box do QR code
        border=4,  # Largura da borda
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Cria a imagem do QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Pede ao usuário o local para salvar o arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
    
    if file_path:
        try:
            # Salva a imagem no caminho escolhido
            img.save(file_path)
            messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar a imagem: {e}")
    else:
        messagebox.showwarning("Aviso", "O salvamento foi cancelado.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de QR Code")

# Configurações de layout
label_link = tk.Label(root, text="Digite o link:")
label_link.pack(pady=5)

entry_link = tk.Entry(root, width=60)
entry_link.pack(pady=5)

botao_gerar = tk.Button(root, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack(pady=20)

# Inicia a interface gráfica
root.mainloop()
