Nome: Sabrina Figueiredo

Disciplina: Tecnologia Orientada a Objetos

Professora: Vanessa Lago Machado


# Descrição do tema e objetivo do projeto:

Tema: Sistema de Gerenciamento de Notas Escolares.

Objetivo: O objetivo do projeto é simular um sistema de gerenciamento voltado para uma instituição de ensino. O sistema trabalha com alunos, disciplinas, professores e avaliações, 
permitindo o cálculo da média final do aluno, exibindo as informações do aluno (quais disciplinas está cursando, as avaliações e resultados de cada disciplina) e notificando o status
do aluno (aprovado, recuperação ou reprovado).


# Diagrama de classes (inserido como imagem ou link):

![Diagrama UML](imagens/diagrama.png)


# Descrição de cada classe e pilar da POO utilizado:

Encapsulamento: Os dados são mantidos dentro das classes e manipulados por métodos específicos, como calcular_media(). Na classe Pessoa também é usado property, getter e setter.

Abstração: Utilização da classe abstrata Pessoa, que representa um conceito genérico. O uso do abstractmethod no exibir_dados() obriga as subclasses a implementar esse método.

Herança: As classes Aluno e Professor são subclasses que herdam atributos e métodos da superclasse Pessoa.

Polimorfismo: O método exibir_dados() é implementado de formas diferentes para Aluno e Professor, aplicando polimorfismo por sobrescrita. Uma vez que os dados necessários de serem exibidos para professores e alunos são diferentes, mesmo os dois sendo subclasses de Pessoa.


# Explicação dos padrões de projeto aplicados (Factory e o adicional):

Factory Pattern: É implementado na classe AvaliacaoFactory. É responsável pro centralizar e padronizar a criação de objetos do tipo Avaliacao.

Observer Pattern(adicional): É implementado na classe Observer e NotificadorEmail. É responsável por notificar os observadores, no caso os alunos, por email quando o status é alterado nas disciplinas.


# Instruções para execução e testes do sistema:

1- Clone o repositório
2- Acesse a pasta do projeto
3- Execute o sistema

Os testes são realizados no main.py que já possui um exemplo de funcionamento.
No main.py é simulado o cadastro do aluno, adição das disciplinas que ele cursa (com informações sobre as avaliações de cada disciplina), o cálculo da média, aplicação da reavaliação caso necessário e alteração do status do aluno com notificação por email.

