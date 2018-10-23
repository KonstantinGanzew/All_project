def search4vowels(phrase:str) ->set:
    """Возврощает все гласные буквы найденные в фразе"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') ->set:
    """Возврощает множество букв из letters, найденых в указаннй фразе"""
    return set(letters).intersection(set(phrase))
