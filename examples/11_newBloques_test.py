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
# Constants
file_work = r".\data\example.txt"
# lista que va a almacenar los resultados
results = list()
out2 = list()



# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, file_work)

# Extrae la informacion deseada de 'results'
for line in results:
	if line['type'] == 'block':
		out = dict()
		for propert, value in line.items():
			if propert != 'type':
				out[propert] = value
		out2.append(out)

# Presenta los resultados del test
print "===  All Blocks  ".ljust(80, "=")
for line in out2:
	print "Block:"
	for propert, value in line.items():
		print "   ", propert, ":", value
print '='*80
