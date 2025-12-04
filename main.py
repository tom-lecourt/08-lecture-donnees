#### Imports et définition des variables globales
"""
Main module pour la lecture et le traitement de données depuis un fichier CSV.
"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,mode='r',encoding='utf-8') as f:
        l = f.readlines()
    lf = [list(map(int, line.strip().split(';'))) for line in l]
    return lf

def get_list_k(data, k):
    """
    retourne la k-ième liste de data
    
    :param data: Les données sous forme de liste de listes
    :param k: l'indice de la liste à retourner
    """
    l = data[k]
    return l

def get_first(l):
    """
    Obtient le 1er element de la liste
    
    :param l: la liste dont on veut le 1er élément
    """
    return l[0]

def get_last(l):
    """
    Obtient le dernier élément de la liste
    
    :param l: la liste dont on veut le dernier élément
    """
    return l[len(l)-1]

def get_max(l):
    """
    Obtient le maximum de la liste
    
    :param l: la liste dont on veut le maximum
    """
    return max(l)

def get_min(l):
    """
    Obtient le minimum de la liste

    :param l: la liste dont on veut le minimum
    """
    return min(l)

def get_sum(l):
    """
    Obtient la somme des éléments de la liste
    
    :param l: la liste dont on veut la somme
    """
    return sum(l)

#### Fonction principale


def main():
    """
    Fonction principale pour lire les données et effectuer des opérations dessus.
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
    list_k = get_list_k(data, 37)
    print(get_first(list_k))
    print(get_last(list_k))
    print(get_max(list_k))
    print(get_min(list_k))
    print(get_sum(list_k))

if __name__ == "__main__":
    main()
