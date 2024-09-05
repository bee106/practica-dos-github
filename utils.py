# obtener pais

def get_country_data(data,country):
  country_data = list(filter(lambda item: item['Country'] == country, data))
  print(country_data)
  return country_data

# Obtener la cantidad de medallas del pais
def get_country_paris(country_data):
  medallas_data = {
      'silver':int(country_data['Silver']),
      'gold':int(country_data['Gold']),
      'bronze':int(country_data['Bronze'])
  }
# Asignamos valores a labels,values para despues graficarlos  
  labels = medallas_data.keys()
  values = medallas_data.values()
  return labels,values 



