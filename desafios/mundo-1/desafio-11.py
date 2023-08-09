alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
area = alt * lar
tinta = area / 2
print ('Sua parede tem {}m² e serão usados {}L de tinta para pintá-la.'.format(area, tinta))