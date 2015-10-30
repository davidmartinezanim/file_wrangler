### Read File of example.txt
# Library
import txt_wrangler as tw
# Constants
file_work = r".\data\example.txt"
# lista que va a almacenar los resultados
results = list()


# Lectura i interpretacio dels fitxers de dades
tw.read_file(results, file_work)
# BORRAR...
print results
print
# BORRAR...

# Presenta los resultados del test
print "===  Results  ".ljust(80, "=")
for line in results:
	print line
print '='*80
