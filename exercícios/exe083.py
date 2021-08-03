exp = str(input('Digite uma expressão: '))
pilha = []
for s in exp:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        pilha.append(')')
print(pilha)