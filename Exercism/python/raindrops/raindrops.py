def convert(num, raindrops=((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))):
    return ''.join(v * (not num % k) for k, v in raindrops) or str(num)
