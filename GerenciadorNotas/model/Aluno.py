from .Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_dados(self):
        txt = f"Aluno: {self.nome}"
        txt += f"\nMatrícula: {self.matricula}"
        return txt
