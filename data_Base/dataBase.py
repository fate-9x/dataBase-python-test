import json
import pathlib
import os

ADD_DATA = 1
SEARCHER = 2
IDVIEWER = 3
CLOSE = 4

Continue = True


datos = []

ids = []

def Add_data():
	os.system("cls")
	id_data = input("Ingrese el identificador de los datos: ")

	name_data = input("Ingrese el nombre del dato: ")

	content_data = input("Ingrese el contenido del dato: ")

	diccionario = {name_data:content_data}

	persona = [id_data]
	persona.append(diccionario)
	datos.append(persona)
	ids.append(id_data)

def Searcher():
	os.system("cls")

	id_find = input("Ingrese el ID del dato que busca: ")

	for element in datos:
		if element[0] == id_find:
			print(f"{element}")
			input("-"*50)
			break

def IDVierwer():
	os.system("cls")

	for element in ids:
		print(f"\n{element}\n")
		print("-"*50)
	input("Presiona enter para continuar...")

def Recuperate_data():
	if pathlib.Path("dataBase.json").exists():

		with open("dataBase.json", "r")as file:

			database = json.load(file)
		for element in database:
			datos.append(element)


def Save_data():
	with open("dataBase.json", "w")as file:
		json.dump(datos, file, indent=4)

def Recuperate_ID():
	if pathlib.Path("dataID.json").exists():

		with open("dataID.json", "r")as file:

			dataID = json.load(file)
		for element in dataID:
			ids.append(element)


def Save_ID():
	with open("dataID.json", "w")as file:
		json.dump(ids, file, indent=4)


while Continue:
	os.system("cls")

	Recuperate_data()
	Recuperate_ID()

	print(f'''		Menu

{ADD_DATA}) Agregar datos
{SEARCHER}) Buscar datos
{IDVIEWER}) Ver los ID
{CLOSE}) Salir''')
	opt = int(input("Ingrese una opcion: "))
	if opt == ADD_DATA:
		Add_data()

	if opt == SEARCHER:
		Searcher()

	if opt == IDVIEWER:
		IDVierwer()

	if opt == CLOSE:

		Save_data()
		Save_ID()
		Continue = False
