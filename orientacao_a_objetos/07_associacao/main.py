import Curso
import Aluno

def main():
    curso1 = Curso.Curso(nome_curso="Python")
    curso2 = Curso.Curso(nome_curso="Java")

    aluno1 = Aluno.Aluno(nome_aluno="Amós da Silva", matricula="1")
    aluno2 = Aluno.Aluno(nome_aluno="teste de Aluno", matricula="2")
    aluno3 = Aluno.Aluno(nome_aluno="João e Maria", matricula="3")
    aluno4 = Aluno.Aluno(nome_aluno="Maria José", matricula="4")
    aluno5 = Aluno.Aluno(nome_aluno="José pereira", matricula="5")
    aluno6 = Aluno.Aluno(nome_aluno="Paulo Oliveira", matricula="6")

    # Inscrevendo alunos no Curso - 1
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    # Inscrevendo alunos no Curso - 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)

    # lista de alunos cruso - 1
    print(f"Curso: {curso1.nome_curso} - Lista de Alunos")
    for aluno in curso1.listar_alunos():
        print(aluno)

    # lista de alunos cruso - 2
    print(f"\nCurso: {curso2.nome_curso} - Lista de Alunos")
    for aluno in curso2.listar_alunos():
        print(aluno)

    
if __name__ == "__main__":
    main()