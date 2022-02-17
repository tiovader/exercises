from functools import reduce

HEADER = '{0} of beer on the wall, {0} of beer.'.format
APPEND = '{} of beer on the wall.'
END_VERSE = ('Go to the store and buy some more, ' + APPEND,
             'Take it down and pass it around, ' + APPEND) + \
                 ('Take one down and pass it around, ' + APPEND,) * 98
BOTTLES = ('no more bottles', '1 bottle') + \
    tuple('%d bottles' % i for i in range(2, 100))

def recite(start, take=1):
    _recite = reduce(
        list.__add__,
        [[HEADER(BOTTLES[n]).capitalize(),
          END_VERSE[n].format(BOTTLES[n-1]).capitalize(),
          ''] for n in range(start, start - take, -1)])

    return _recite[:-1]
