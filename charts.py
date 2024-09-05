# Importamos la libreia matplotlib
import matplotlib.pyplot as plt

# Declaramos funcion para graficar 
def generate_bar_chart(labels,values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()
  