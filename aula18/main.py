import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def criar_banco():
    try:
        conectar = sqlite3.connect('Cadastro-banco.db')
        cursor = conectar.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cadastro(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       telefone TEXT NOT NULL,
                       endereco TEXT NOT NULL
                       )''')
        conectar.commit()
        conectar.close()
    except Exception as erro:
        print(f'Erro ao se conectar com o banco de dados: {erro}')

def salvar_cadastro():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get() 
    endereco = entry_endereco.get()

    if not nome or not email or not telefone or not endereco:
        messagebox.showwarning('Atenção', 'Por favor, preencha todos os campos!')
        return 

    try:
        conectar = sqlite3.connect('Cadastro-banco.db')
        cursor = conectar.cursor()
        cursor.execute('''INSERT INTO cadastro (nome, email, telefone, endereco) 
                          VALUES (?, ?, ?, ?)''', (nome, email, telefone, endereco))
        conectar.commit()
        conectar.close()

        messagebox.showinfo('Sucesso', 'Cliente cadastrado com sucesso!')

      
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)

    
        listar_clientes()

    except Exception as erro:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar: {erro}')

def listar_clientes():

    for linha in tree.get_children():
        tree.delete(linha)
    
    try:
        conectar = sqlite3.connect('Cadastro-banco.db')
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM cadastro")
        clientes_cadastrados = cursor.fetchall()
        
        for cliente in clientes_cadastrados:
            tree.insert("", tk.END, values=cliente)
            
        conectar.close()
    except Exception as erro:
        messagebox.showerror('Erro', f'Erro ao buscar dados: {erro}')

def apagar_cliente():
    item_selecionado = tree.focus()
    
    if not item_selecionado:
        messagebox.showwarning('Atenção', 'Por favor, selecione um cliente na tabela para apagar.')
        return
    
    valores = tree.item(item_selecionado, 'values')
    id_cliente = valores[0]
    nome_cliente = valores[1]
    
    confirmacao = messagebox.askyesno('Confirmar Exclusão', f'Tem certeza que deseja apagar o cliente: {nome_cliente}?')
        
    if confirmacao:
        try:
            conectar = sqlite3.connect('Cadastro-banco.db')
            cursor = conectar.cursor()
            cursor.execute("DELETE FROM cadastro WHERE id = ?", (id_cliente,))
            conectar.commit()
            conectar.close()
            
            messagebox.showinfo('Sucesso', 'Cliente apagado com sucesso!')
            listar_clientes()
            
        except Exception as erro:
            messagebox.showerror('Erro', f'Erro ao apagar cliente: {erro}')


criar_banco()

root = tk.Tk()
root.title('Cadastro de clientes')
root.geometry('650x600')


tk.Label(root, text='Nome').pack(pady=2)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack(pady=2)

tk.Label(root, text='Email').pack(pady=2)
entry_email = tk.Entry(root, width=40)
entry_email.pack(pady=2)

tk.Label(root, text='Telefone').pack(pady=2)
entry_telefone = tk.Entry(root, width=40) 
entry_telefone.pack(pady=2)

tk.Label(root, text='Endereço').pack(pady=2)
entry_endereco = tk.Entry(root, width=40)
entry_endereco.pack(pady=2)


frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=15)

btn_salvar = tk.Button(frame_botoes, text='Salvar Cadastro', width=15, bg='green', fg='white', command=salvar_cadastro)
btn_salvar.pack(side=tk.LEFT, padx=10)

btn_apagar = tk.Button(frame_botoes, text='Apagar Selecionado', width=15, bg='red', fg='white', command=apagar_cliente)
btn_apagar.pack(side=tk.LEFT, padx=10)


colunas = ("ID", "Nome", "Email", "Telefone", "Endereço")
tree = ttk.Treeview(root, columns=colunas, show="headings")

tree.heading("ID", text="ID")
tree.column("ID", width=30, anchor=tk.CENTER)

tree.heading("Nome", text="Nome")
tree.column("Nome", width=150)

tree.heading("Email", text="Email")
tree.column("Email", width=150)

tree.heading("Telefone", text="Telefone")
tree.column("Telefone", width=100, anchor=tk.CENTER)

tree.heading("Endereço", text="Endereço")
tree.column("Endereço", width=150)

tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)


listar_clientes()

root.mainloop()