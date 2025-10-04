import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, filedialog

# Criar banco de dados SQLite
conn = sqlite3.connect("dados_web.db")
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    preco TEXT,
    disponibilidade TEXT
)
""")

def extrair_dados(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a resposta foi bem-sucedida
        soup = BeautifulSoup(resposta.text, "html.parser")
        
        livros = []
        for item in soup.find_all("article", class_="product_pod"):
            titulo = item.h3.a["title"]
            preco = item.find("p", class_="price_color").text
            disponibilidade = item.find("p", class_="instock availability").text.strip()
            livros.append((titulo, preco, disponibilidade))
        
        return livros
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao acessar o site: {e}")
        return []

def salvar_dados_no_sqlite(livros):
    cursor.executemany("INSERT INTO dados (titulo, preco, disponibilidade) VALUES (?, ?, ?)", livros)
    conn.commit()

def exportar_dados():
    df = pd.read_sql_query("SELECT * FROM dados", conn)
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    
    if file_path:
        if file_path.endswith(".csv"):
            df.to_csv(file_path, index=False)
        else:
            df.to_excel(file_path, index=False)
        messagebox.showinfo("Sucesso", f"Dados exportados para {file_path}")

def iniciar_extracao():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Atenção", "Por favor, insira um URL!")
        return
    
    livros_extraidos = extrair_dados(url)
    if livros_extraidos:
        salvar_dados_no_sqlite(livros_extraidos)
        messagebox.showinfo("Sucesso", "Dados extraídos e armazenados com sucesso!")

# Criando interface gráfica
root = tk.Tk()
root.title("Web Scraping para Excel/CSV")

tk.Label(root, text="Insira o URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Extrair Dados", command=iniciar_extracao).pack(pady=5)
tk.Button(root, text="Exportar para CSV/Excel", command=exportar_dados).pack(pady=5)

root.mainloop()

# Fechar conexão com o banco de dados ao encerrar
conn.close()
