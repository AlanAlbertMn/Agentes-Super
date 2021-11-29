# Código que combina los archivos de las reviews de Amazon, Imdb y Yelp

# Esta función sirve para abrir los archivos seleccionados y mezclarlos, luego poner todo en un nuevo archivo
def mergefiles(in_filenames, merge_name):
    out_file = open(merge_name,"w+")
    for file in in_filenames:
        in_file = open(file, 'r')
        out_file.write(in_file.read())
        in_file.close()
    out_file.close()

# Se definen todas las variables a usar, los arhivos seleccionados y el nombre del nuevo archivo a escribir con todos las 3000 instancias
if __name__ == "__main__":

    # Archivos de las reviews
    file1="amazon_cells_labelled.txt"
    file2="imdb_labelled.txt"
    file3="yelp_labelled.txt"
    # Se colocan todos los archivos dentro de un arreglo
    in_filenames=[]
    # Se van agregando los datos de los distintos archivos en el arreglo
    in_filenames.append(file1)
    in_filenames.append(file2)
    in_filenames.append(file3)
    '\n'.join(in_filenames)
    # Se crea el nuevo archivo ya con todas las instancias
    merge_name="merged_data.txt"
    mergefiles(in_filenames, merge_name)