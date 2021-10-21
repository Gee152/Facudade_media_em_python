nm = input ('Seu nome é:')

nm = nm.title()

print (nm)

n1 = float (input ('Sua nota 1: '))
n2 = float (input ('Sua nota 2: '))

n3 = float(n1+n2)/2

if n3 >= 6:
    print ('Sua média é', n3, 'você foi aprovado!')
else:
    print ('Sua média é', n3, 'você não foi aprovado!')
