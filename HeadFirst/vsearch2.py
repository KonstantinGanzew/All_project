def sear(word):
    """Выводит гласные, найденные в данном слове"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)
