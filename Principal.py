import os
import platform
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
from usuario import *
from banco import Banco
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


class TelaLogin:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Tela de Login")

        self.fonte = ("Verdana", "10")

        # Configuração do formulário
        self.container = tk.Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 20
        self.container.pack()

        self.lblusuario = tk.Label(self.container, text="Usuário:", font=self.fonte)
        self.lblusuario.pack(pady=5)

        self.txtusuario = tk.Entry(self.container, font=self.fonte)
        self.txtusuario.pack(pady=5)

        self.lblsenha = tk.Label(self.container, text="Senha:", font=self.fonte)
        self.lblsenha.pack(pady=5)

        self.txtsenha = tk.Entry(self.container, show="*", font=self.fonte)
        self.txtsenha.pack(pady=5)

        self.btnlogin = tk.Button(self.container, text="Entrar", font=self.fonte, command=self.login)
        self.btnlogin.pack(pady=10)

    def login(self):
        usuario = self.txtusuario.get()
        senha = self.txtsenha.get()

        if self.validar_login(usuario, senha):
            self.master.destroy()  # Fecha a tela de login

        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def validar_login(self, usuario, senha):
        banco = Banco()  # Certifique-se de ter a classe Banco configurada corretamente
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            linha = c.fetchone()
            c.close()
            return linha is not None
        except Exception as e:
            print(f"Erro ao validar login: {e}")
            return False



class MainApplication:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gerenciamento")
        self.master.geometry("800x600")

        # Criando o menu principal
        menu_bar = Menu(master)
        master.config(menu=menu_bar)

        # Criando os menus
        usuarios_menu = Menu(menu_bar, tearoff=0)
        cidades_menu = Menu(menu_bar, tearoff=0)
        clientes_menu = Menu(menu_bar, tearoff=0)
        sair_menu = Menu(menu_bar, tearoff=0)

        # Adicionando itens aos menus
        menu_bar.add_cascade(label="Usuários", menu=usuarios_menu)
        usuarios_menu.add_command(label="Gerenciar Usuários", command=self.abrir_tela_usuarios)

        menu_bar.add_cascade(label="Cidades", menu=cidades_menu)
        cidades_menu.add_command(label="Gerenciar Cidades", command=self.abrir_tela_cidades)

        menu_bar.add_cascade(label="Clientes", menu=clientes_menu)
        clientes_menu.add_command(label="Gerenciar Clientes", command=self.abrir_tela_clientes)

        menu_bar.add_cascade(label="Sair", menu=sair_menu)
        sair_menu.add_command(label="Sair", command=self.quit)

    def abrir_tela_usuarios(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = ApplicationUsuarios(self.new_window)

    def abrir_tela_cidades(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = ApplicationCidades(self.new_window)

    def abrir_tela_clientes(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = ApplicationClientes(self.new_window)

    def quit(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()
class ApplicationUsuarios:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")

        # Configuração dos containers
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack(fill=tk.BOTH, expand=True)

        # Título
        self.titulo = Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        # ID Usuário
        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=tk.LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=tk.LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=tk.RIGHT)

        # Nome
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=tk.LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=tk.LEFT)

        # Telefone
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=tk.LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=tk.LEFT)

        # E-mail
        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=tk.LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=tk.LEFT)

        # Usuário
        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=tk.LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=tk.LEFT)

        # Senha
        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=tk.LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=tk.LEFT)

        # Botões
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=tk.LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarUsuario)
        self.bntAlterar.pack(side=tk.LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirUsuario)
        self.bntExcluir.pack(side=tk.LEFT)

        # Mensagem
        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

        # Treeview
        self.columns = ("ID", "Nome", "Telefone", "Email", "Usuario", "Senha")
        self.treeview = ttk.Treeview(self.container1, columns=self.columns, show='headings')
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_select)
        self.update_treeview()

        # Botão Exportar para PDF
        self.btn_exportar_pdf = Button(master, text="Exportar Tabela para PDF", font=self.fonte,
                                       command=self.exportar_para_pdf)
        self.btn_exportar_pdf.pack(pady=10)

        # Botão Visualizar PDF
        self.btn_visualizar_pdf = Button(master, text="Visualizar PDFs", font=self.fonte, command=self.visualizar_pdfs)
        self.btn_visualizar_pdf.pack(pady=10)

        # Botão Sair
        self.btn_sair = Button(master, text="Sair", command=master.destroy, font=("Verdana", "12"))
        self.btn_sair.pack(pady=10)

    def on_treeview_select(self, event):
        selected_item = self.treeview.selection()
        if not selected_item:
            return
        item_values = self.treeview.item(selected_item)["values"]
        if item_values:
            self.txtidusuario.delete(0, tk.END)
            self.txtidusuario.insert(0, item_values[0])
            self.txtnome.delete(0, tk.END)
            self.txtnome.insert(0, item_values[1])
            self.txttelefone.delete(0, tk.END)
            self.txttelefone.insert(0, item_values[2])
            self.txtemail.delete(0, tk.END)
            self.txtemail.insert(0, item_values[3])
            self.txtusuario.delete(0, tk.END)
            self.txtusuario.insert(0, item_values[4])
            self.txtsenha.delete(0, tk.END)
            self.txtsenha.insert(0, item_values[5])

    def inserirUsuario(self):
        user = Usuarios(
            nome=self.txtnome.get(),
            telefone=self.txttelefone.get(),
            email=self.txtemail.get(),
            usuario=self.txtusuario.get(),
            senha=self.txtsenha.get()
        )
        resultado = user.insertUser()
        if "sucesso" in resultado.lower():
            messagebox.showinfo("Sucesso", resultado)
        else:
            messagebox.showerror("Erro", resultado)

        self.clear_entries()
        self.update_treeview()

    def alterarUsuario(self):
        user = Usuarios(
            idusuario=self.txtidusuario.get(),
            nome=self.txtnome.get(),
            telefone=self.txttelefone.get(),
            email=self.txtemail.get(),
            usuario=self.txtusuario.get(),
            senha=self.txtsenha.get()
        )
        resultado = user.updateUser()
        if "sucesso" in resultado.lower():
            messagebox.showinfo("Sucesso", resultado)
        else:
            messagebox.showerror("Erro", resultado)

        self.clear_entries()
        self.update_treeview()

    def excluirUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get())
        resultado = user.deleteUser()
        if "sucesso" in resultado.lower():
            messagebox.showinfo("Sucesso", resultado)
        else:
            messagebox.showerror("Erro", resultado)

        self.clear_entries()
        self.update_treeview()

    def clear_entries(self):
        self.txtidusuario.delete(0, tk.END)
        self.txtnome.delete(0, tk.END)
        self.txttelefone.delete(0, tk.END)
        self.txtemail.delete(0, tk.END)
        self.txtusuario.delete(0, tk.END)
        self.txtsenha.delete(0, tk.END)

    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        data = self.fetch_data()
        self.populate_treeview(data)

    def fetch_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def populate_treeview(self, data):
        for row in data:
            self.treeview.insert("", "end", values=row)

    def exportar_para_pdf(self):
        """Exporta os dados da Treeview para um arquivo PDF."""
        # Nome do arquivo PDF
        pdf_file = "usuarios_exportados.pdf"

        # Capturando os dados da Treeview
        dados = []
        for item in self.treeview.get_children():
            valores = self.treeview.item(item, 'values')
            dados.append(valores)

        # Checando se há dados para exportar
        if not dados:
            messagebox.showwarning("Atenção", "Não há dados para exportar.")
            return

        # Configurando o PDF
        with PdfPages(pdf_file) as pdf:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.axis('tight')
            ax.axis('off')

            # Cabeçalho e dados da tabela
            colunas = ["ID", "Nome", "Telefone", "Email", "Usuário", "Senha"]
            tabela = ax.table(cellText=dados, colLabels=colunas, cellLoc='center', loc='center')

            # Ajustando a fonte e o layout da tabela
            tabela.auto_set_font_size(False)
            tabela.set_fontsize(10)
            tabela.scale(2, 2)

            # Salvando a tabela no PDF
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()

        messagebox.showinfo("Sucesso", f"PDF '{pdf_file}' exportado com sucesso.")

    def visualizar_pdfs(self):
        """Abre uma janela para selecionar e visualizar os PDFs disponíveis."""
        # Criar uma nova janela para listar os PDFs
        janela_visualizar = Toplevel(self.master)
        janela_visualizar.title("Visualizar PDFs")
        janela_visualizar.geometry("400x300")

        # Listar arquivos PDF no diretório atual
        pdfs = [f for f in os.listdir() if f.endswith('.pdf')]

        # Verificação se há PDFs disponíveis
        if not pdfs:
            messagebox.showinfo("Informação", "Nenhum PDF disponível.")
            janela_visualizar.destroy()
            return

        # Criação de Listbox para mostrar PDFs
        listbox = Listbox(janela_visualizar, selectmode=tk.SINGLE)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Adicionar Scrollbar
        scrollbar = Scrollbar(janela_visualizar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Adicionar PDFs na Listbox
        for pdf in pdfs:
            listbox.insert(tk.END, pdf)

        # Botão para abrir o PDF selecionado
        btn_abrir = Button(janela_visualizar, text="Abrir PDF", command=lambda: self.abrir_pdf(listbox))
        btn_abrir.pack(pady=5)

    def abrir_pdf(self, listbox):
        # Abre o PDF selecionado pelo usuário.
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um PDF para abrir.")
            return

        pdf_selecionado = listbox.get(selecionado)

        # Abrir o PDF de acordo com o sistema operacional
        try:
            if platform.system() == "Windows":
                os.startfile(pdf_selecionado)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", pdf_selecionado])
            else:
                subprocess.run(["xdg-open", pdf_selecionado])
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o PDF: {str(e)}")


    def buscarUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        resultado = user.selectUser(user.idusuario)
        if resultado == "Busca feita com sucesso!":
            self.txtnome.delete(0, tk.END)
            self.txtnome.insert(0, user.nome)
            self.txttelefone.delete(0, tk.END)
            self.txttelefone.insert(0, user.telefone)
            self.txtemail.delete(0, tk.END)
            self.txtemail.insert(0, user.email)
            self.txtusuario.delete(0, tk.END)
            self.txtusuario.insert(0, user.usuario)
            self.txtsenha.delete(0, tk.END)
            self.txtsenha.insert(0, user.senha)
        else:
            self.lblmsg["text"] = resultado


class ApplicationCidades:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")

        # Containers para o formulário
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 10
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 15
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 15
        self.container7.pack(fill=tk.BOTH, expand=True)

        # Formulário de entrada de dados
        self.titulo = Label(self.container1, text="Informe os dados da cidade:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidcidade = Label(self.container2, text="ID Cidade:", font=self.fonte, width=10)
        self.lblidcidade.pack(side=tk.LEFT)

        self.txtidcidade = Entry(self.container2)
        self.txtidcidade["width"] = 10
        self.txtidcidade["font"] = self.fonte
        self.txtidcidade.pack(side=tk.LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarCidade)
        self.btnBuscar.pack(side=tk.RIGHT)

        self.lblnomecid = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecid.pack(side=tk.LEFT)

        self.txtnomecid = Entry(self.container3)
        self.txtnomecid["width"] = 25
        self.txtnomecid["font"] = self.fonte
        self.txtnomecid.pack(side=tk.LEFT)

        self.lblcep = Label(self.container4, text="CEP:", font=self.fonte, width=10)
        self.lblcep.pack(side=tk.LEFT)

        self.txtcep = Entry(self.container4)
        self.txtcep["width"] = 25
        self.txtcep["font"] = self.fonte
        self.txtcep.pack(side=tk.LEFT)

        self.lblUF = Label(self.container5, text="UF:", font=self.fonte, width=10)
        self.lblUF.pack(side=tk.LEFT)

        self.txtUF = Entry(self.container5)
        self.txtUF["width"] = 25
        self.txtUF["font"] = self.fonte
        self.txtUF.pack(side=tk.LEFT)

        self.bntInsert = Button(self.container6, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.bntInsert.pack(side=tk.LEFT)

        self.bntAlterar = Button(self.container6, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.bntAlterar.pack(side=tk.LEFT)

        self.bntExcluir = Button(self.container6, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.bntExcluir.pack(side=tk.LEFT)

        self.lblmsg = Label(self.container6, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

        # Configurando a Treeview para exibir os dados
        self.columns = ("ID", "Nome", "CEP", "UF")
        self.treeview = ttk.Treeview(self.container7, columns=self.columns, show='headings')
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Botão de Sair
        self.btnSair = Button(self.container7, text="Sair", font=self.fonte, width=12, command=self.sairAplicacao)
        self.btnSair.pack(side=tk.BOTTOM, pady=10)

        # Botão Exportar para PDF
        self.btn_exportar_pdf = Button(master, text="Exportar Tabela para PDF", font=self.fonte, command=self.exportar_para_pdf)
        self.btn_exportar_pdf.pack(pady=10)

        # Botão Visualizar PDF
        self.btn_visualizar_pdf = Button(master, text="Visualizar PDFs", font=self.fonte, command=self.visualizar_pdfs)
        self.btn_visualizar_pdf.pack(pady=10)

        # Adiciona o evento de seleção à Treeview
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)

        # Preenchendo a Treeview com dados do banco ao iniciar
        self.update_treeview()

    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())  # Limpa todos os dados existentes
        data = self.fetch_data()  # Busca os dados atualizados
        self.populate_treeview(data)  # Reinsere os dados

    def fetch_data(self):
        conn = sqlite3.connect('banco.db')  # Conectando ao banco de dados
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cidades")
        rows = cursor.fetchall()  # Buscando todos os resultados
        conn.close()
        return rows

    def populate_treeview(self, data):
        for row in data:
            self.treeview.insert("", "end", values=row)

    def inserirCidade(self):
        cidade = Cidades(
            nomecid=self.txtnomecid.get(),
            cep=self.txtcep.get(),
            UF=self.txtUF.get()
        )
        resultado = cidade.insertCidade()
        self.lblmsg["text"] = resultado
        messagebox.showinfo("Informação", resultado)  # Exibe uma caixa de mensagem com o resultado
        self.clear_entries()
        self.update_treeview()  # Atualiza a Treeview após inserir

    def alterarCidade(self):
        cidade = Cidades(
            idcidade=self.txtidcidade.get(),
            nomecid=self.txtnomecid.get(),
            cep=self.txtcep.get(),
            UF=self.txtUF.get()
        )
        resultado = cidade.updateCidade()
        self.lblmsg["text"] = resultado
        messagebox.showinfo("Informação", resultado)  # Exibe uma caixa de mensagem com o resultado
        self.clear_entries()
        self.update_treeview()  # Atualiza a Treeview após alterar

    def excluirCidade(self):
        idcidade = self.txtidcidade.get()
        cidade = Cidades(idcidade=idcidade)

        if cidade.temClientesAssociados():
            resultado = "Não é possível excluir a cidade. Existem clientes associados a ela."
            self.lblmsg["text"] = resultado
            messagebox.showinfo("Informação", resultado)
            return

        resultado = cidade.deleteCidade()
        self.lblmsg["text"] = resultado
        messagebox.showinfo("Informação", resultado)
        self.clear_entries()
        self.update_treeview()

    def deleteCidade(self):
        # Código para excluir a cidade do banco de dados
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cidades WHERE idcidade = ?', (self.idcidade,))
        conn.commit()
        conn.close()
        return "Cidade excluída com sucesso."

    def temClientesAssociados(self):
        # Verifica se há clientes associados a esta cidade
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clientes WHERE idcidade = ?', (self.idcidade,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0

    def buscarCidade(self):
        cidade = Cidades()
        idcidade = self.txtidcidade.get()
        resultado = cidade.selectCidade(idcidade)
        self.lblmsg["text"] = resultado
        messagebox.showinfo("Informação", resultado)  # Exibe uma caixa de mensagem com o resultado
        if resultado == "Busca feita com sucesso!":
            self.txtnomecid.delete(0, tk.END)
            self.txtnomecid.insert(tk.END, cidade.nomecid)
            self.txtcep.delete(0, tk.END)
            self.txtcep.insert(tk.END, cidade.cep)
            self.txtUF.delete(0, tk.END)
            self.txtUF.insert(tk.END, cidade.UF)

    def sairAplicacao(self):
        self.master.destroy()

    def on_treeview_select(self, event):
        selected_item = self.treeview.selection()  # Obtém o item selecionado
        if selected_item:
            item = self.treeview.item(selected_item)  # Obtém os dados do item selecionado
            cidade_data = item['values']  # Os valores são uma lista com os dados da linha
            self.txtidcidade.delete(0, tk.END)
            self.txtidcidade.insert(tk.END, cidade_data[0])
            self.txtnomecid.delete(0, tk.END)
            self.txtnomecid.insert(tk.END, cidade_data[1])
            self.txtcep.delete(0, tk.END)
            self.txtcep.insert(tk.END, cidade_data[2])
            self.txtUF.delete(0, tk.END)
            self.txtUF.insert(tk.END, cidade_data[3])

    def clear_entries(self):
        self.txtidcidade.delete(0, tk.END)
        self.txtnomecid.delete(0, tk.END)
        self.txtcep.delete(0, tk.END)
        self.txtUF.delete(0, tk.END)

    def exportar_para_pdf(self):
        """Exporta os dados da Treeview para um arquivo PDF."""
        pdf_file = "cidades_exportadas.pdf"

        # Capturando os dados da Treeview
        dados = []
        for item in self.treeview.get_children():
            valores = self.treeview.item(item, 'values')
            dados.append(valores)

        # Checando se há dados para exportar
        if not dados:
            messagebox.showwarning("Atenção", "Não há dados para exportar.")
            return

        # Configurando o PDF
        with PdfPages(pdf_file) as pdf:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.axis('tight')
            ax.axis('off')

            # Cabeçalho e dados da tabela
            colunas = ["ID", "Nome", "CEP", "UF"]
            tabela = ax.table(cellText=dados, colLabels=colunas, cellLoc='center', loc='center')

            # Ajustando a fonte e o layout da tabela
            tabela.auto_set_font_size(False)
            tabela.set_fontsize(10)
            tabela.scale(2, 2)

            # Salvando a tabela no PDF
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()

        messagebox.showinfo("Sucesso", f"PDF '{pdf_file}' exportado com sucesso.")

    def visualizar_pdfs(self):
        """Abre uma janela para selecionar e visualizar os PDFs disponíveis."""
        janela_visualizar = Toplevel(self.master)
        janela_visualizar.title("Visualizar PDFs")
        janela_visualizar.geometry("400x300")

        # Listar arquivos PDF no diretório atual
        pdfs = [f for f in os.listdir() if f.endswith('.pdf')]

        # Verificação se há PDFs disponíveis
        if not pdfs:
            messagebox.showinfo("Informação", "Nenhum PDF disponível.")
            janela_visualizar.destroy()
            return

        # Criação de Listbox para mostrar PDFs
        listbox = Listbox(janela_visualizar, selectmode=tk.SINGLE)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Adicionar Scrollbar
        scrollbar = Scrollbar(janela_visualizar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Adicionar PDFs na Listbox
        for pdf in pdfs:
            listbox.insert(tk.END, pdf)

        # Botão para abrir o PDF selecionado
        btn_abrir = Button(janela_visualizar, text="Abrir PDF", command=lambda: self.abrir_pdf(listbox))
        btn_abrir.pack(pady=5)

    def abrir_pdf(self, listbox):
        # Abre o PDF selecionado pelo usuário.
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um PDF para abrir.")
            return

        pdf_selecionado = listbox.get(selecionado)

        # Abrir o PDF de acordo com o sistema operacional
        try:
            if platform.system() == "Windows":
                os.startfile(pdf_selecionado)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open {pdf_selecionado}")
            else:  # Linux
                os.system(f"xdg-open {pdf_selecionado}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o PDF: {e}")



class Cidades:
    def __init__(self, idcidade=0, nomecid="", cep="", UF=""):
        self.idcidade = idcidade
        self.nomecid = nomecid
        self.cep = cep
        self.UF = UF

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                   INSERT INTO cidades (nomecid, cep, UF) 
                   VALUES (?, ?, ?)
               """, (self.nomecid, self.cep, self.UF))
            banco.conexao.commit()
            c.close()
            return "Cidade inserida com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                   UPDATE cidades
                   SET nomecid = ?, cep = ?, UF = ?
                   WHERE idcidade = ?
               """, (self.nomecid, self.cep, self.UF, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def deleteCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {str(e)}"

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades WHERE idcidade = ?", (idcidade,))
            linha = c.fetchone()
            if linha:
                self.idcidade = linha[0]
                self.nomecid = linha[1]
                self.cep = linha[2]
                self.UF = linha[3]
                c.close()
                return "Busca feita com sucesso!"
            else:
                return "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {str(e)}"

    def temClientesAssociados(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT COUNT(*) FROM clientes WHERE idcidade = ?', (self.idcidade,))
            count = c.fetchone()[0]
            c.close()
            return count > 0
        except Exception as e:
            return f"Ocorreu um erro na verificação de clientes associados: {str(e)}"

class ApplicationClientes:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gestão de Clientes")

        # Configuração do formulário
        self.fonte = ("Verdana", "8")
        self.container1 = tk.Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = tk.Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = tk.Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = tk.Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = tk.Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 10
        self.container5.pack()

        self.container6 = tk.Frame(master)
        self.container6["pady"] = 15
        self.container6.pack()

        self.container7 = tk.Frame(master)
        self.container7["pady"] = 15
        self.container7.pack()

        self.container8 = tk.Frame(master)
        self.container8["pady"] = 10
        self.container8.pack(fill=tk.BOTH, expand=True)

        self.titulo = tk.Label(self.container1, text="Informe os dados do cliente:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidcliente = tk.Label(self.container2, text="ID Cliente:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=tk.LEFT)

        self.txtidcliente = tk.Entry(self.container2)
        self.txtidcliente["width"] = 10
        self.txtidcliente["font"] = self.fonte
        self.txtidcliente.pack(side=tk.LEFT)

        self.btnBuscar = tk.Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCliente
        self.btnBuscar.pack(side=tk.RIGHT)

        self.lblnomecli = tk.Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecli.pack(side=tk.LEFT)

        self.txtnomecli = tk.Entry(self.container3)
        self.txtnomecli["width"] = 25
        self.txtnomecli["font"] = self.fonte
        self.txtnomecli.pack(side=tk.LEFT)

        self.lblcpf = tk.Label(self.container4, text="CPF:", font=self.fonte, width=10)
        self.lblcpf.pack(side=tk.LEFT)

        self.txtcpf = tk.Entry(self.container4)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=tk.LEFT)

        self.lbldata_nascimento = tk.Label(self.container5, text="Nascimento:", font=self.fonte, width=15)
        self.lbldata_nascimento.pack(side=tk.LEFT)

        self.txtdata_nascimento = tk.Entry(self.container5)
        self.txtdata_nascimento["width"] = 25
        self.txtdata_nascimento["font"] = self.fonte
        self.txtdata_nascimento.pack(side=tk.LEFT)

        self.lblgenero = tk.Label(self.container6, text="Gênero:", font=self.fonte, width=10)
        self.lblgenero.pack(side=tk.LEFT)

        self.combogenero = ttk.Combobox(self.container6, values=["Masculino", "Feminino"], font=self.fonte, width=23)
        self.combogenero.pack(side=tk.LEFT)
        self.combogenero.current(0)  # Define a opção padrão como "Masculino"

        self.lblcidade = tk.Label(self.container7, text="Cidade:", font=self.fonte, width=10)
        self.lblcidade.pack(side=tk.LEFT)

        self.combocidade = ttk.Combobox(self.container7, values=[], font=self.fonte, width=23)
        self.combocidade.pack(side=tk.LEFT)

        self.bntInsert = tk.Button(self.container7, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCliente
        self.bntInsert.pack(side=tk.LEFT)

        self.bntAlterar = tk.Button(self.container7, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCliente
        self.bntAlterar.pack(side=tk.LEFT)

        self.bntExcluir = tk.Button(self.container7, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCliente
        self.bntExcluir.pack(side=tk.LEFT)

        self.lblmsg = tk.Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        # Configuração da Treeview (Tabela)
        self.columns = ("ID", "Nome", "CPF", "Data de nascimento", "Gênero", "Cidade")
        self.treeview = ttk.Treeview(self.container8, columns=self.columns, show='headings')
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_select)

        # Botão de Sair
        self.btnSair = tk.Button(self.container8, text="Sair", font=self.fonte, width=12, command=self.sairAplicacao)
        self.btnSair.pack(side=tk.BOTTOM, pady=10)

        self.update_treeview()
        self.populate_combobox_cidades(self.combocidade)

        # Botão Exportar PDF
        self.btnExportarPDF = tk.Button(self.container8, text="Exportar PDF", font=self.fonte, width=12,
                                        command=self.exportar_para_pdf)
        self.btnExportarPDF.pack(side=tk.LEFT, padx=10)

        # Botão Visualizar PDFs
        self.btnVisualizarPDF = tk.Button(self.container8, text="Visualizar PDFs", font=self.fonte, width=12,
                                          command=self.visualizar_pdfs)
        self.btnVisualizarPDF.pack(side=tk.LEFT, padx=10)

    def fetch_data_clients(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes")
            rows = c.fetchall()
            c.close()
            return rows
        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []

    def existeClientesPorCidade(idcidade):
        conn = sqlite3.connect('banco.db')  # Altere para o seu banco de dados
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clientes WHERE idcidade = ?', (idcidade,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0

    def fetch_data_cities(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT idcidade, nomecid FROM cidades")
            rows = c.fetchall()
            c.close()
            return rows
        except Exception as e:
            print(f"Erro ao buscar cidades: {e}")
            return []

    def populate_treeview(self, data):
        for row in data:
            self.treeview.insert("", "end", values=row)

    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        data = self.fetch_data_clients()
        self.populate_treeview(data)

    def populate_combobox_cidades(self, combobox):
        cidades = self.fetch_data_cities()
        combobox["values"] = [cidade[1] for cidade in cidades]

    def get_city_id_by_name(self, city_name):
        cidades = self.fetch_data_cities()
        for cid in cidades:
            if cid[1] == city_name:
                return cid[0]
        return None

    def on_treeview_select(self, event):
        selected_item = self.treeview.selection()
        if not selected_item:
            return
        item_values = self.treeview.item(selected_item)["values"]
        if item_values:
            self.txtidcliente.delete(0, tk.END)
            self.txtidcliente.insert(0, item_values[0])
            self.txtnomecli.delete(0, tk.END)
            self.txtnomecli.insert(0, item_values[1])
            self.txtcpf.delete(0, tk.END)
            self.txtcpf.insert(0, item_values[2])
            self.txtdata_nascimento.delete(0, tk.END)
            self.txtdata_nascimento.insert(0, item_values[3])
            self.combogenero.set(item_values[4])
            cidade_id = item_values[5]
            cidades = self.fetch_data_cities()
            for cid in cidades:
                if cid[0] == cidade_id:
                    self.combocidade.set(cid[1])
                    break

    def inserirCliente(self):
        cliente = Clientes()
        cliente.nomecli = self.txtnomecli.get()
        cliente.cpf = self.txtcpf.get()
        cliente.data_nascimento = self.txtdata_nascimento.get()
        cliente.genero = self.combogenero.get()

        cidade_selecionada = self.combocidade.get()
        cidade_id = self.get_city_id_by_name(cidade_selecionada)
        cliente.idcidade = cidade_id

        result = cliente.insertCliente()
        messagebox.showinfo("Resultado", result)

        self.txtidcliente.delete(0, tk.END)
        self.txtnomecli.delete(0, tk.END)
        self.txtcpf.delete(0, tk.END)
        self.txtdata_nascimento.delete(0, tk.END)
        self.combogenero.set('')
        self.combocidade.set('')

        self.update_treeview()

    def alterarCliente(self):
        cliente = Clientes()
        cliente.idcliente = self.txtidcliente.get()
        cliente.nomecli = self.txtnomecli.get()
        cliente.cpf = self.txtcpf.get()
        cliente.data_nascimento = self.txtdata_nascimento.get()
        cliente.genero = self.combogenero.get()

        cidade_selecionada = self.combocidade.get()
        cidade_id = self.get_city_id_by_name(cidade_selecionada)
        cliente.idcidade = cidade_id

        result = cliente.updateCliente()
        messagebox.showinfo("Resultado", result)

        self.txtidcliente.delete(0, tk.END)
        self.txtnomecli.delete(0, tk.END)
        self.txtcpf.delete(0, tk.END)
        self.txtdata_nascimento.delete(0, tk.END)
        self.combogenero.set('')
        self.combocidade.set('')

        self.update_treeview()

    def excluirCliente(self):
        cliente = Clientes()
        cliente.idcliente = self.txtidcliente.get()

        result = cliente.deleteCliente()
        messagebox.showinfo("Resultado", result)

        self.txtidcliente.delete(0, tk.END)
        self.txtnomecli.delete(0, tk.END)
        self.txtcpf.delete(0, tk.END)
        self.txtdata_nascimento.delete(0, tk.END)
        self.combogenero.set('')
        self.combocidade.set('')

        self.update_treeview()

    def excluirCliente(self):
        cliente = Clientes()
        cliente.idcliente = self.txtidcliente.get()

        result = cliente.deleteCliente()
        messagebox.showinfo("Resultado", result)

        self.txtidcliente.delete(0, tk.END)
        self.txtnomecli.delete(0, tk.END)
        self.txtcpf.delete(0, tk.END)
        self.txtdata_nascimento.delete(0, tk.END)
        self.combogenero.set('')
        self.combocidade.set('')

        self.update_treeview()

    def buscarCliente(self):
        cliente = Clientes()
        cliente.idcliente = self.txtidcliente.get()

        result = cliente.selectCliente()
        if result:
            self.txtnomecli.delete(0, tk.END)
            self.txtnomecli.insert(0, result[1])
            self.txtcpf.delete(0, tk.END)
            self.txtcpf.insert(0, result[2])
            self.txtdata_nascimento.delete(0, tk.END)
            self.txtdata_nascimento.insert(0, result[3])
            self.combogenero.set(result[4])
            cidade_id = result[5]
            cidades = self.fetch_data_cities()
            for cid in cidades:
                if cid[0] == cidade_id:
                    self.combocidade.set(cid[1])
                    break
        else:
            messagebox.showwarning("Aviso", "Cliente não encontrado.")

    def exportar_para_pdf(self):
        """Exporta os dados da Treeview para um arquivo PDF."""
        pdf_file = "clientes_exportados.pdf"

        # Capturando os dados da Treeview
        dados = []
        for item in self.treeview.get_children():
            valores = self.treeview.item(item, 'values')
            dados.append(valores)

        # Checando se há dados para exportar
        if not dados:
            messagebox.showwarning("Atenção", "Não há dados para exportar.")
            return

        # Configurando o PDF
        with PdfPages(pdf_file) as pdf:
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.axis('tight')
            ax.axis('off')

            # Cabeçalho e dados da tabela
            colunas = ["ID", "Nome", "CPF", "Data de Nascimento", "Gênero", "Cidade"]
            tabela = ax.table(cellText=dados, colLabels=colunas, cellLoc='center', loc='center')

            # Ajustando a fonte e o layout da tabela
            tabela.auto_set_font_size(False)
            tabela.set_fontsize(10)
            tabela.scale(1.5, 1.5)  # Ajuste de escala conforme necessário

            # Salvando a tabela no PDF
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()

        messagebox.showinfo("Sucesso", f"PDF '{pdf_file}' exportado com sucesso.")

    def visualizar_pdfs(self):
        """Abre uma janela para selecionar e visualizar os PDFs disponíveis."""
        janela_visualizar = Toplevel(self.master)
        janela_visualizar.title("Visualizar PDFs")
        janela_visualizar.geometry("400x300")

        # Listar arquivos PDF no diretório atual
        pdfs = [f for f in os.listdir() if f.endswith('.pdf')]

        # Verificação se há PDFs disponíveis
        if not pdfs:
            messagebox.showinfo("Informação", "Nenhum PDF disponível.")
            janela_visualizar.destroy()
            return

        # Criação de Listbox para mostrar PDFs
        listbox = Listbox(janela_visualizar, selectmode=tk.SINGLE)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Adicionar Scrollbar
        scrollbar = Scrollbar(janela_visualizar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Adicionar PDFs na Listbox
        for pdf in pdfs:
            listbox.insert(tk.END, pdf)

        # Botão para abrir o PDF selecionado
        btn_abrir = Button(janela_visualizar, text="Abrir PDF", command=lambda: self.abrir_pdf(listbox))
        btn_abrir.pack(pady=5)

    def abrir_pdf(self, listbox):
        """Abre o PDF selecionado pelo usuário."""
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um PDF para abrir.")
            return

        pdf_selecionado = listbox.get(selecionado)

        # Abrir o PDF de acordo com o sistema operacional
        try:
            if platform.system() == "Windows":
                os.startfile(pdf_selecionado)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open {pdf_selecionado}")
            else:  # Linux
                os.system(f"xdg-open {pdf_selecionado}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o PDF: {e}")

    def sairAplicacao(self):
        self.master.destroy()



class Clientes:
    def __init__(self, idcliente=0, nomecli="", cpf="", data_nascimento="", genero="", idcidade=None):
        self.idcliente = idcliente
        self.nomecli = nomecli
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.idcidade = idcidade

    def insertCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                INSERT INTO clientes (nomecli, cpf, data_nascimento, genero, idcidade) 
                VALUES (?, ?, ?, ?, ?)
            """, (self.nomecli, self.cpf, self.data_nascimento, self.genero, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cliente inserido com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {str(e)}"

    def updateCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                UPDATE clientes
                SET nomecli = ?, cpf = ?, data_nascimento = ?, genero = ?, idcidade = ?
                WHERE idcliente = ?
            """, (self.nomecli, self.cpf, self.data_nascimento, self.genero, self.idcidade, self.idcliente))
            banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {str(e)}"

    def deleteCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM clientes WHERE idcliente = ?", (self.idcliente,))
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {str(e)}"

    def selectCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes WHERE idcliente = ?", (self.idcliente,))
            linha = c.fetchone()
            if linha:
                self.idcliente = linha[0]
                self.nomecli = linha[1]
                self.cpf = linha[2]
                self.data_nascimento = linha[3]
                self.genero = linha[4]
                self.idcidade = linha[5]
                c.close()
                return linha
            else:
                return None
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {str(e)}"

    @staticmethod
    def existeClientesPorCidade(idcidade):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM clientes WHERE idcidade = ?', (idcidade,))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    app = MainApplication(root)
    root.mainloop()