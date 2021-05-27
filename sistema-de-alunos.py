"""Criando as funções"""

def valida_sexo():
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    while sexo not in 'MF' or sexo == '':
        print('\033[31mDigite apenas M ou F.\033[m')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    return sexo


def quantidade_provas():
    try:
        quantidade = int(input('Digite a quantidade de provas: '))
        while quantidade < 1 or quantidade > 10:
            print('\033[31mDigite apenas entre 1 e 10.\033[m')
            quantidade = int(input('Digite a quantidade de provas: '))
    except Exception as ValueError:
        print('\033[31mDigite apenas entre 1 e 10.\033[m')
        quantidade = int(input('Digite a quantidade de provas: '))
    return quantidade


def valida_nota(posicao):
    try:
        nota = float(input(f'Digite a {posicao}ª nota: '))
        while nota < 0 or nota > 10:
            print('\033[31mDigite apenas notas entre 0 e 10.\033[m')
            nota = float(input(f'Digite a {posicao}ª nota: '))
    except Exception as ValueError:
        print('\033[31mDigite apenas notas entre 0 e 10.\033[m')
        nota = float(input(f'Digite a {posicao}ª nota: '))
    return nota


"""Criando variáveis"""

aprovado = exame = reprovado = 0
mulher_aprovada = homem_aprovado = 0
mulher_exame = homem_exame = 0
mulher_reprovada = homem_reprovado = 0
total_alunos = 0


"""Programa principal"""

print('\033[34m*\033[m'*30)
print('\033[34m  Sistema de notas de alunos\033[m')
print('\033[34m*\033[m'*30)

while True:

    nome = str(input('Nome do aluno: '))
    sexo = valida_sexo()

    quantidade = quantidade_provas()

    lista_notas = []
    for i in range(1, quantidade+1):
        lista_notas.append(valida_nota(i))

    print('')

    media = sum(lista_notas)/len(lista_notas)
    total_alunos+=1

    """Verficando as médias e quantidade de homens e mulheres"""

    if media >= 7:
        aprovado += 1
        if sexo in 'F':
            mulher_aprovada += 1
        else:
            homem_aprovado += 1

    elif media < 7 and media > 4:
        exame = + 1
        if sexo in 'F':
            mulher_exame += 1
        else:
            homem_exame += 1

    elif media <= 4:
        reprovado = + 1
        if sexo in 'F':
            mulher_reprovada += 1
        else:
            homem_reprovado += 1


    """Questionando se continuará o cadastro"""

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resp not in 'SN':
        print('\033[31mDigite apenas N ou S.\033[m')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break

print('')
print(f"\033[34mNo total tivemos {total_alunos} alunos cadastrados.\033[m")
print('')
print(f"Temos {(aprovado * 100) / total_alunos:.1f}% dos alunos aprovados.")
print(f"Sendo {mulher_aprovada} mulher(es) e {homem_aprovado} homem(ns).")
print('')
print(f"Temos {(exame * 100) / total_alunos:.1f}% dos alunos em exame.")
print(f"Sendo {mulher_exame} mulher(es) e {homem_exame} homem(ns).")
print('')
print(f"Temos {(reprovado * 100) / total_alunos:.1f}% dos alunos reprovados.")
print(f"Sendo {mulher_reprovada} mulher(es) e {homem_reprovado} homem(ns).")
