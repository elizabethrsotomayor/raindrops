def convert(number):
    factor_sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    string = ''
    for factor, sound in factor_sounds.items():
        if not number % factor:
            string += sound

    return string or str(number)
