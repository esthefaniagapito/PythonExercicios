# Calcule a hipotenusa
import math

cateto_oposto = float(input('Cateto oposto:'))
cateto_adjacente = float(input('Cateto_adjacente:'))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa é {}'.format(hipotenusa))