nome = (input('Insira o nome do aluno: ')).upper()
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
if (nota1 < 0) or (nota1 >10) or (nota2 < 0) or (nota2 >10) or (nota3 < 0) or (nota3 >10):
    print('NOTA(S) INVÁLIDA(S) \nPrograma Finalizado Por Erro')
else:
    media = (nota1+nota2+nota3)/3
    if media >= 7:
        print(nome,': APROVADO')
    else:
        if media >=4:
            print(nome,': EM RECUPERAÇÃO')
        else:
            print(nome,': REPROVADO')