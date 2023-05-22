listaNombres = ['Harry Houdini','Newton','David Blaine','Hawking','Messi','Teller','Einstein','Pele','Juanes']
magos = ['Harry Houdini', 'David Blaine', 'Teller', 'Juan Tamariz', 'Jorge Blass']
cientificos = ['Newton', 'Hawking', 'Einstein','Galileo Galilei','Nikola Tesla','Charles Darwin']



def  hacer_grandioso(lista):
   return ['El gran ' + nom for nom in lista]

def imprimir_nombres(lista):
    for n in lista:
        print(n)


def main():
    listaMagos, listaCientificos, listaOtros = [],[],[]
    # Separar lista de nombres en magos, científicos y otros
    for n in listaNombres:
        if n in magos:
            listaMagos.append(n)
        elif n in cientificos:
            listaCientificos.append(n)
        else:
            listaOtros.append(n)

    # Imprimir lista completa de nombres antes de ser modificados
    print("\n### Lista completa de nombres ###")
    imprimir_nombres(listaNombres)
    
    # Imprimir los nombres de los magos
    print("\n### Lista de de los magos ###")
    imprimir_nombres(listaMagos)
    
    # Imprimir los nombres de los científicos
    print("\n### Lista de de los científicos ###")
    imprimir_nombres(listaCientificos)
    
    # Imprimir los nombres de los restantes
    print("\n### Lista de de los nombres restantes ###")
    imprimir_nombres(listaOtros)


    # Modificar lista de magos
    listaMagos = hacer_grandioso(listaMagos)
    # Imprimir los nombres de los magos grandiosos
    print("\n### Lista de de los magos grandiosos ###")
    imprimir_nombres(listaMagos)


if __name__=="__main__":
    main()