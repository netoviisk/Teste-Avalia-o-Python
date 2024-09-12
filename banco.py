import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUsuarios()
        self.createTableCidades()
        self.createTableClientes()

    def createTableUsuarios(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT
        )""")
        self.conexao.commit()
        c.close()

    def createTableCidades(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS cidades (
            idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nomecid TEXT,
            cep TEXT,
            UF TEXT
        )""")
        self.conexao.commit()
        c.close()

    def createTableClientes(self):
        c = self.conexao.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nomecli TEXT,
            cpf TEXT,
            data_nascimento TEXT,
            genero TEXT,
            idcidade INTEGER,
            FOREIGN KEY (idcidade) REFERENCES cidades(idcidade)
        )""")
        self.conexao.commit()
        c.close()