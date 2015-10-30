######
import txt_wrangler as tw


# Requeriments: current... results.
def main(lines, line_num, current, results):

    if 'load_file' in current:
        # Recogemos el nombre del fichero
        new_filename = current.rpartition('"')[0].rpartition('"')[2]

        # Para cada fichero encontrado, volvemos a llamar a leer el fichero.
        tw.read_file(results, new_filename)
