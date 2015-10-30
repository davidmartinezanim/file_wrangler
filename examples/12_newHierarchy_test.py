### Hierarchy of example.txt

# Este es un fichero de ejemplo que utiliza el codigo que tengo hasta ahora.
# Como puedes ver, lo unico que necesitas por ahora es utilizar la funcion
# 'tw.get_blocks_in_file' para conseguir todos los bloques de un archivo.
#
# Deberias ser capaz de utilizar este fichero para probar las dos funciones
# que vas a estar mirando. 'mover' y 'duplicar'.
#
# Como siempre, si tienes alguna duda, comentamelo

# Importamos txt_wrangler (mi modulo) y definimos en namespace tw para no tener
# que escribirlo cada vez. Eso significa que para utilizar funcionalidad de mi
# modulo escribes tw seguido de un punto y el nombre de la funcion
import txt_wrangler as tw
from cue.obj.hitem import HItem
# Constants
file_work = r".\data\example.txt"
# lista que va a almacenar los resultados
results = list()



# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, file_work)

# Extrae la informacion deseada de 'results'
root = HItem(name=file_work.rpartition('\\')[2])
for line in results:
	if line['type'] == 'block':
		section = line['name']
		HItem(name=section, parent=root)

# Presenta los resultados del test
print "===  Hierarchy  ".ljust(80, "=")
print root,
print '='*80
