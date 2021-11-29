# Código para convertir el documento generado de las reviews de Amazon, Yelp e Imdb a un formato que se pueda usar dentro de Weka
# El código también hace un preprocesamiento simple del texto, se convierten todos los caracteres a minúsculas

import string

# Se definen los headers requeridos dentro de los archivos usados dentro de Weka
RELATION_BASE_STR = "@relation '{relation_name}'\n"
ATTRIBUTE_BASE_STR = "@attribute Text string\n"
ATTRIBUTE_CLASS_BASE_STR = "@attribute class-att {0,1}\n"
DATA_BASE_STR = "@data\n"

# Se abre el archivo que contiene todas las instancias
def file_read(name):
  try:
    file_iterator = open(name)
    return file_iterator
  except Exception as error:
    print ('No se pudo leer el archivo', error.message)
    return None

# Método que sirve para que se vayan colocando los datos ya modificados
def file_append(name):
  try:
    file_iterator = open(name, "a")
    return file_iterator
  except Exception as error:
    print('No se pudo leer el archivo', error.message)
    return None

# Se colocan los headers que se definieron al principio dentro del nuevo archivo
def add_header(file_to_write, relation_name):
  try:
    file_to_write.write(RELATION_BASE_STR.format(relation_name=relation_name))
    file_to_write.write(ATTRIBUTE_BASE_STR)
    file_to_write.write(ATTRIBUTE_CLASS_BASE_STR)
    file_to_write.write(DATA_BASE_STR)
  except Exception as error:
    print('No se pudo agregar el encabezado', error.message)
    return None

# Se limpian las palabras dentro del archivo, se cambian a minúsculas y se le agregan comillas simples a cada línea porque así lo requiere el formato en Weka
def clean_string(og_string):
  return og_string.lower().replace("'", "").translate(str.maketrans('','', string.punctuation))

# Métodos para recorrer las clases (0, 1) y que estén junto a los strings
def get_class(og_string):
  if (len(og_string) > 1):
    return og_string[-2]
  else:
    return ""

def remove_class(og_string):
  if (len(og_string) > 1):
    return og_string[:-3]
  else:
    return og_string

# Se arma cada string en el nuevo archivo
def assemble_string(class_string, simple_string):
  return f"'{simple_string}',{class_string}\n"

# Se hace lo anterior con todo el texto, cada línea se va limpiando, se obtiene la clase y se acomoda
def rewrite_body(file_to_read, file_to_write):
  for line in file_to_read:
    clean_line = clean_string(line)
    class_string = get_class(clean_line)
    simple_string = remove_class(clean_line)
    string_to_write = assemble_string(class_string=class_string, simple_string=simple_string)
    file_to_write.write(string_to_write)

# Se llaman a los métodos anteriores y se crea el nuevo archivo
def change_text_format(txt_name, arff_name):
  file_to_read = file_read(txt_name)
  file_to_write = file_append(arff_name)

  add_header(file_to_write=file_to_write, relation_name="Reviews")
  rewrite_body(file_to_read=file_to_read, file_to_write=file_to_write)

  file_to_read.close()
  file_to_write.close()

if __name__ == '__main__':
  change_text_format(txt_name="./merged_data.txt", arff_name="./reviews1.arff")