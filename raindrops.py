def convert(number):
    factor_sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    string = ''
    for key, value in factor_sounds.items():
        if number % key == 0:
            string += value

    return string or str(number)
