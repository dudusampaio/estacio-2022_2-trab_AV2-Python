#Exercício 1: Faça função que calcule a área do trapézio

basemaior=float(input('Informe o valor da base maior: '))

basemenor=float(input('Informe o valor da base menor: '))

altura = float(input('Informe o valor da altura: '))

area=((basemaior+basemenor)*altura)/2

print(f'O valor da área desse trapézio é {area:.2f} unidades de área')

