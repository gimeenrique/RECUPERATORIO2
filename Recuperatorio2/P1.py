from arbol_binario import BinaryTree

#1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

pokemon_data = [
    {'nombre': 'Pikachu', 'numero': 25, 'tipo': ['Electrico']},
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipo': ['Pasto', 'Veneno']},
    {'nombre': 'Charizard', 'numero': 6, 'tipo': ['Fuego', 'Volador']},
    {'nombre': 'Jolteon', 'numero': 135, 'tipo': ['Electrico']},
    {'nombre': 'Lycanroc', 'numero': 745, 'tipo': ['Roca']},
    {'nombre': 'Tyrantrum', 'numero': 697, 'tipo': ['Roca', 'Dragon']},
    {'nombre': 'Steelix', 'numero': 208, 'tipo': ['Acero']}
]

nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

#a
for pokemon in pokemon_data:
    nombre_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    numero_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    tipo_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})

#b
num = 25
numero_tree.inorden(num)
nombre = 'Bul'
nombre_tree.search_by_coincidence(nombre)
tipo = 'Electrico'
tipo_tree.inorden(tipo)

# c
def listar_nombres_por_tipo(self, root, tipo):
    if root is not None:
        if tipo in root.value['tipo']:
            print(root.value['nombre'])
        self.listar_nombres_por_tipo(root.left, tipo)
        self.listar_nombres_por_tipo(root.right, tipo)

tipos_a_buscar = ["Agua","Fuego", "Planta","Electrico"]
print("Nombres de Pokémon de tipo Agua:")
tipo_tree.listar_nombres_por_tipo(tipo_tree.root, tipos_a_buscar)

# d
print("Listado de Pokémon en orden ascendente por número:")
numero_tree.inorden()
print("\nListado de Pokémon en orden ascendente por nombre:")
nombre_tree.inorden()
print("Listado de Pokémon por nivel nombre")
nombre_tree.by_level()

# e
print("Datos de Pokémon Jolteon:")
nombre_tree.search_pokemon_by_nombre('Jolteon')
print("\nDatos de Pokémon Lycanroc:")
nombre_tree.search_pokemon_by_nombre('Lycanroc')
print("\nDatos de Pokémon Tyrantrum:")
nombre_tree.search_pokemon_by_nombre('Tyrantrum')

# f
print(f"Total de Pokémon de tipo 'Eléctrico': {tipo_tree.contar('Eléctrico')}")
print(f"Total de Pokémon de tipo 'Acero': {tipo_tree.contar('Acero')}")