#### Imports et définition des variables globales
"""
    import de csv pour faciliter la lecture du fichier
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode = "r", encoding = "utf8") as f:
        r = csv.reader(f, delimiter=";")
        l = list(r)
        return [[int(x) for x in line] for line in l]

def get_list_k(data, k):
    """
        retourne la k-ieme liste
    """
    return data[k]

def get_first(l):
    """
        retourne le permier element
    """
    return l[0]

def get_last(l):
    """
        retourne le dernier element
    """
    return l[-1]

def get_max(l):
    """
        retourne le plus grand element
    """
    return max(l)

def get_min(l):
    """
        retourne le plus petit element
    """
    return min(l)

def get_sum(l):
    """
        fais la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
        Execute un test
    """
    data = read_data(FILENAME)
    print(data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
