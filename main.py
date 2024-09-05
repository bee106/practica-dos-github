import charts
import read_csv
import utils


def run():
  # Leemos el archivo csv
  data = read_csv.read_csv('./olympics2024.csv')
  # Obtenemos el pais que queremos y su data
  country = input('ingrese el pais =>>>')
  result = utils.get_country_data(data,country)
  # Obtenemos la cantidad de medallas del pais
  if len(result) > 0:
    country = result[0]
    labels,values = utils.get_country_paris(country)
    # Generamos la grafica
    charts.generate_bar_chart(labels,values)


if __name__ == '__main__':
  run()