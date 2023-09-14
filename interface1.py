import tkinter as tk

def exibir_mensagem():
    nome = entry_nome.get()
    mensagem = entry_mensagem.get()
    resultado.config(text=f"{nome}: {mensagem}")

# Cria a janela
janela = tk.Tk()
janela.title("Mensagem Personalizada")

# Cria um rótulo para o nome
label_nome = tk.Label(janela, text="Celso Eduardo Bento Pugim:")
label_nome.pack()

# Cria uma caixa de entrada para o nome
entry_nome = tk.Entry(janela)
entry_nome.pack()

# Cria um rótulo para a mensagem
label_mensagem = tk.Label(janela, text="Mensagem:")
label_mensagem.pack()

# Cria uma caixa de entrada para a mensagem
entry_mensagem = tk.Entry(janela)
entry_mensagem.pack()

# Cria um botão para exibir a mensagem
botao_exibir = tk.Button(janela, text="Exibir Mensagem", command=exibir_mensagem)
botao_exibir.pack()

# Cria uma área para exibir a mensagem com o nome
resultado = tk.Label(janela, text="", font=("Helvetica", 12))
resultado.pack()

# Inicia a interface gráfica
janela.mainloop()