nota1 = int(input(''))
nota2 = int(input(''))
nota3 = int(input(''))
media = (nota1 + nota2 + nota3) / 3
if nota3 > 8:
    media+=1
if media > 10:
    media = print('%.2f'%10)
else:
    print('%.2f'%media)
