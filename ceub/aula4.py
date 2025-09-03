# x = 3 != 3 # verifica se é diferente ou n
# y = 4 != 2
# print(x)
# print(y)

import mysql.connector

cnx = mysql.connector.connect(user='root', password='ceub123456',
                            host='localhost', database='db_teste')
cs = cnx.cursor()
sql = "SELECT * FROM aluno;"
cs.execute(sql, params: [])

total_alunos = 0
soma_medias = 0
for (ra, nome, nota1, nota2) in cs:
    total_alunos += 1
    soma_medias
    print(ra, nome, nota1, nota2)
    media = (nota1 + nota2) / 2
    soma_medias += media
    print(media)
    if media >= 5:
        print('Aprovado')
    else:
        print('Reprovado')

    if media == 0:
        print('Menção = SR')
    elif media < 2:
        print('Menção = II')
    elif media < 5:
        print('Menção = MI')
    elif media < 7:
        print('Menção = MM')
    elif media < 9:
        print('Menção = MS')
    else:
        print('Menção = SS')

    print('-' * 30)

print(f'Total de alunos = {total_alunos}')
print(f'Média geral da turma = {soma_medias / total_alunos}')

cs.close()
cnx.close()