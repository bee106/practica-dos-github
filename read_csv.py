# Importamos modulo csv
import csv
# Declaramos un funcion que nos permita leer el archivo csv
def read_csv(path):

# Leemos el archivo csv
  with open(path,'r') as cvsfile:
    reader = csv.reader(cvsfile)
    header = next(reader)
    data = []
# Creamos un ciclo que nos permita iterar cada fila del csv y creando un diccionario
    for row in reader:
      iterable = zip(header,row)
      country_dict = {key:values for key,values in iterable}
      data.append(country_dict)
    return data






# Establecemos dualidad para que pueda ser ejecutado desde la terminal o en otro archivo
if __name__ == '__main__':
  
  country = input('Ingrese el pais: ')
  data = read_csv('./olympics2024.csv')
  