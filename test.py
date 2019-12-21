f = open("/home/shade/Desktop/text.txt", "r")
texto = f.read()
arreglo = texto.split(';')

print arreglo[:2]
print arreglo[2:]

