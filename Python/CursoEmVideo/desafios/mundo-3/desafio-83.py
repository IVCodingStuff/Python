exp = (str(input('Digite a expressão: ')))
parenteses = []
for c in exp 
    if c == '(':
        parenteses.append('(')
    elif c ==')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
    if len(parenteses) == 0:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está inválida!')
