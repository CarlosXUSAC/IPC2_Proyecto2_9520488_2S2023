class Nodo:
    def __init__(self, valor, espacio):
        self.valor = valor
        self.espacio = espacio
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def agregar_nodo(self, valor, espacio):
        nuevo_nodo = Nodo(valor, espacio)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.longitud += 1

    def cambiar_valor(self, indice, nuevo_valor):
        if 0 <= indice < self.longitud:
            nodo_actual = self.cabeza
            contador = 0
            while contador < indice:
                nodo_actual = nodo_actual.siguiente
                contador += 1
            nodo_actual.valor = nuevo_valor

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(f"Valor: {nodo_actual.valor}, Espacio: {nodo_actual.espacio}")
            nodo_actual = nodo_actual.siguiente

class ListaPrincipal:
    def __init__(self):
        self.listas = []

    def agregar_lista(self, largo):
        nueva_lista = ListaDoblementeEnlazada()
        for _ in range(largo):
            valor = "apagado"  # Valor inicial apagado
            espacio = 1
            nueva_lista.agregar_nodo(valor, espacio)
        self.listas.append(nueva_lista)

    def cambiar_valor(self, lista_idx, nodo_idx, nuevo_valor):
        if 0 <= lista_idx < len(self.listas):
            lista = self.listas[lista_idx]
            lista.cambiar_valor(nodo_idx, nuevo_valor)

    def mostrar_listas(self):
        if not self.listas:
            print("No hay listas disponibles.")
            return

        # Obtener la longitud máxima de una lista enlazada
        max_longitud = max(lista.longitud for lista in self.listas)

        # Crear una matriz para mostrar las listas en orientación vertical invertida
        matriz = [[" " for _ in range(len(self.listas))] for _ in range(max_longitud)]

        # Llenar la matriz con los valores de las listas en el orden deseado
        for i, lista in enumerate(self.listas):
            nodo_actual = lista.cabeza
            j = max_longitud - 1
            while nodo_actual:
                matriz[j][i] = nodo_actual.valor
                nodo_actual = nodo_actual.siguiente
                j -= 1

        # Mostrar la matriz en la orientación deseada
        for fila in matriz:
            print(" | ".join(fila))

if __name__ == "__main__":
    lista_principal = ListaPrincipal()

    num_listas = int(input("Ingrese el número de listas: "))
    largo_lista = int(input("Ingrese el largo de las listas: "))

    for _ in range(num_listas):
        lista_principal.agregar_lista(largo_lista)

    while True:
        lista_principal.mostrar_listas()
        opcion = input("¿Desea cambiar otro nodo? (s/n): ")
        if opcion.lower() != "s":
            break

        lista_idx = int(input("Ingrese el índice de la lista a modificar: "))
        nodo_idx = int(input("Ingrese el índice del nodo a modificar: "))
        nuevo_valor = input("Ingrese el nuevo valor (encendido/apagado): ")

        lista_principal.cambiar_valor(lista_idx, nodo_idx, nuevo_valor)
