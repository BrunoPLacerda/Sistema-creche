import tkinter as tk
import sqlite3
from tkinter import ttk

# Função para realizar consulta no banco de dados
def search_data():
    # Conectar ao banco de dados
    conn = sqlite3.connect('BDCRECHE.db')
    cursor = conn.cursor()

    # Consulta SQL para buscar nomes que contenham o termo da pesquisa
    query = "SELECT * FROM Creche WHERE nome LIKE ?"
    cursor.execute(query, ('%' + search_entry.get() + '%',))
    
    # Buscar todos os resultados
    rows = cursor.fetchall()

    # Fechar a conexão
    conn.close()

    # Limpando a tabela antes de adicionar novos resultados
    for row in tree.get_children():
        tree.delete(row)

    # Inserindo os resultados na tabela
    for row in rows:
        tree.insert("", tk.END, values=row)

# Interface gráfica usando Tkinter
app = tk.Tk()
app.title("Sistema de Consulta - Creche")
app.geometry("600x400")

# Campo de busca
tk.Label(app, text="Buscar por nome:").pack(pady=5)
search_entry = tk.Entry(app)
search_entry.pack(pady=5)

# Botão de busca
search_button = tk.Button(app, text="Buscar", command=search_data)
search_button.pack(pady=5)

# Tabela de resultados (Treeview)
columns = ("ID", "Nome", "Cargo", "Data de Nascimento", "Endereço")
tree = ttk.Treeview(app, columns=columns, show="headings")

# Definir cabeçalhos da tabela
for col in columns:
    tree.heading(col, text=col)

tree.pack(expand=True, fill='both')

# Iniciar a interface gráfica
app.mainloop()
