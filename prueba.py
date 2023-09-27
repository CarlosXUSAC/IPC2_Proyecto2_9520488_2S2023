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

    def agregar_nodo(self, valor, espacio):
        nuevo_nodo = Nodo(valor, espacio)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def cambiar_valor(self, indice, nuevo_valor):
        nodo_actual = self.cabeza
        contador = 0
        while nodo_actual:
            if contador == indice:
                nodo_actual.valor = nuevo_valor
                break
            nodo_actual = nodo_actual.siguiente
            contador += 1

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
        if lista_idx < len(self.listas):
            lista = self.listas[lista_idx]
            lista.cambiar_valor(nodo_idx, nuevo_valor)

    def mostrar_listas(self):
        for i, lista in enumerate(self.listas):
            print(f"Lista {i + 1}:")
            lista.mostrar_lista()
            print()

if __name__ == "__main__":
    lista_principal = ListaPrincipal()

    num_listas = int(input("Ingrese el número de listas: "))

    for _ in range(num_listas):
        largo_lista = int(input("Ingrese el largo de la lista: "))
        lista_principal.agregar_lista(largo_lista)

    lista_principal.mostrar_listas()

    lista_idx = int(input("Ingrese el índice de la lista a modificar: "))
    nodo_idx = int(input("Ingrese el índice del nodo a modificar: "))
    nuevo_valor = input("Ingrese el nuevo valor (encendido/apagado): ")

    lista_principal.cambiar_valor(lista_idx, nodo_idx, nuevo_valor)

    lista_principal.mostrar_listas()
