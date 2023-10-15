times = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional', 'Corinthias', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Góias', 'Coritiba', 'América-MG')
print('Primeiros colocados:')

for a in range(5):
    print('{}.{}'.format(a+1,times[a]))
print()

print('Últimos colocados:')
for b in range(15,len(times)):
    print('{}.{}'.format(b+2,times[b]))
print()

print('Ordem alfabética:')
print('{}\n'.format(sorted(times)))

for d in range(len(times)):
    if 'Palmeiras' in (times[d]):
        print ('O Palmeiras está em {}º lugar'.format(d+1))
