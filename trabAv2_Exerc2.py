#Exercicio 2: Faça um programa com uma função chamada somaImposto
def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(t,c))
