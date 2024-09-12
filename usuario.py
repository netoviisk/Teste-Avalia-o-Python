from banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                INSERT INTO usuarios (nome, telefone, email, usuario, senha) 
                VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {str(e)}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
                UPDATE usuarios 
                SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? 
                WHERE idusuario = ?
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {str(e)}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {str(e)}"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE idusuario = ?", (idusuario,))
            linha = c.fetchone()
            if linha:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
                c.close()
                return "Busca feita com sucesso!"
            else:
                return "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {str(e)}"

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
            return "Cidade cadastrada com sucesso!"
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

class Clientes:
    def __init__(self, idcliente=0, nomecli="", cpf="", data_nascimento="", genero="", idcidade=0):
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
            return "Cliente cadastrado com sucesso!"
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

    def selectCliente(self, idcliente):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes WHERE idcliente = ?", (idcliente,))
            linha = c.fetchone()
            if linha:
                self.idcliente = linha[0]
                self.nomecli = linha[1]
                self.cpf = linha[2]
                self.data_nascimento = linha[3]
                self.genero = linha[4]
                self.idcidade = linha[5]  # Adicionado o ID da cidade
                c.close()
                return "Busca feita com sucesso!"
            else:
                return "Cliente não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {str(e)}"