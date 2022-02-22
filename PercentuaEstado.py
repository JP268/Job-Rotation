print('\33[34mSP – R$67.836,43')
print('RJ – R$36.678,66')
print('MG – R$29.229,88')
print('ES – R$27.165,48')
print('Outros – R$19.849,53\33[m')
print('\33[31mTotal = R$180.759,98\33[m')


resposta = str(input('Qual opção deseja saber a porcentagem: ')).lower().strip()
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros
umporcento = total/100

estados = ["sp","rj","mg","es","outros"]

while resposta not in estados:
    print('RESPOSTA INVÁLIDA, DIGITE NOVAMENTE')
    resposta = str(input('Qual Estado deseja saber a porcentagem: ')).lower().strip()

if resposta == "sp":
    porecnt = sp/umporcento
    print('SP = {}%'.format(porecnt))

elif resposta == "rj":
    porecnt = rj/umporcento
    print('RJ = {}%'.format(porecnt))

elif resposta == "mg":
    porecnt = mg/umporcento
    print('MG = {}%'.format(porecnt))

elif resposta == "es":
    porecnt = es/umporcento
    print('ES = {}%'.format(porecnt))

else:
    porecnt = outros/umporcento
    print('OUTROS = {}%'.format(porecnt))
