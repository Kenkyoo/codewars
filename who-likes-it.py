def likes(names):
    l = len(names)
    match l:
        case 0:
            return "no one likes this"
        case 1:
            return f"{str(names[0])} likes this"
        case 2:
            return f"{str(names[0])} and {str(names[1])} like this"
        case 3:
            return f"{str(names[0])}, {str(names[1])} and {str(names[2])} like this"
        case _ if l >= 4:
            return f"{names[0]}, {names[1]} and {l - 2} others like this"


names = ["Peter"]
# names = []
# names = ["Jacob", "Alex"]
# names = ["Max", "John", "Mark"]
# names = ["Alex", "Jacob", "Mark", "Max"]

likes(names)

# Explicacion del codigo
# Esta funcion toma una lista de nombres y devuelve una cadena que indica cuantos nombres hay en la lista y quienes son.# Esta funcion toma una lista de nombres y devuelve una cadena que indica cuantos nombres hay en la lista y quienes son.
