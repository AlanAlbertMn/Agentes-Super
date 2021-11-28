RELATION_BASE_STR = "@relation '{relation_name}'\n"
ATTRIBUTE_BASE_STR = "@attribute Text string\n"
ATTRIBUTE_CLASS_BASE_STR = "@attribute class-att {0,1}\n"
DATA_BASE_STR = "@data\n"

def read_file(in_filename):
    try:
        in_file = open(in_filename)
        return in_file
    except Exception as error:
        print('No se pudo abrir el archivo', error.message)
        return None

def open_file_append(in_filename):
    try:
        in_file = open(in_filename, "a")
        return in_file
    except Exception as error:
        print('No se pudo abrir el archivo', error.message)
        return None

def add_header(file_to_write, relation_name):
    try:
        file_to_write.write(RELATION_BASE_STR.format(relation_name=relation_name))
        file_to_write.write(ATTRIBUTE_BASE_STR)
        file_to_write.write(ATTRIBUTE_CLASS_BASE_STR)
        file_to_write.write(DATA_BASE_STR)
    except Exception as error:
        print('No se puede agregar el encabezado al archivo', error.message)
        return None

def clean_string(og_string):
    return og_string.lower().replace("'", "")

def get_class(og_string):
    if (len(og_string)>1):
        return og_string[-2]
    else:
        return ""

def remove_class(og_string):
    if (len(og_string) > 1):
        return og_string[:-3]
    else:
        return og_string

def assemble_string(class_string, string_no_class):
    return f"'{string_no_class},{class_string}\n"

def parse_text(file_to_read, file_to_write):
    for line in file_to_read:
        clean_line = clean_string(line)
        class_string = clean_string(line)
        string_no_class = remove_class(clean_line)
        string_to_write = assemble_string(class_string = class_string, string_no_class=string_no_class)
        file_to_write.write(string_to_write)

def text_to_arff(file_name, arff_name):
    file_to_read = read_file(file_name)
    file_to_write = open_file_append(arff_name)

    add_header(file_to_write = file_to_write, relation_name = "Reviews")
    parse_text(file_to_read = file_to_read, file_to_write = file_to_write)

    file_to_read.close()
    file_to_write.close()

if __name__ == '__main__':

    file_name = "merged_data.txt"
    arff_name = "reviews.arff"

    text_to_arff(file_name, arff_name)