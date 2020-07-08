# Autores: Jose Luis Pérez Pérez y Yolanda M. Gimeno Rodríguez
# Fecha:
# Título: Script Main del Open Scorbot.
# Universidad de La Laguna

import gui

###############################################################################
# Se inicializa el programa. En este script se creara el objeto que permitira
# hacer el handle del dispositivo. Se iniciaran los 2 hilos en los que
# se divide el funcionamiento del programa.
###############################################################################


# Inicia la conexion y la interfaz gráfica
gui.main()


#Cierre de los hilos
h1.join()
h2.join()

print("Fin de programa")
sys.exit()
