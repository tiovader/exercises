from enum import IntEnum


class Steps(IntEnum):
    m = 1
    M = 2
    A = 3


CHROMATIC = 'C {} D {} E F {} G {} A {} B'
SHARP = CHROMATIC.format('C#', 'D#', 'F#', 'G#', 'A#').split()
FLAT = CHROMATIC.format('Db', 'Eb', 'Gb', 'Ab', 'Bb').split()
mM_SHARP = 'C G D A E B F# a e b f# c# g# d#'.split()


class Scale:
    def __init__(self, tonic):
        scale = (FLAT, SHARP)[tonic in mM_SHARP]
        idx = scale.index(tonic.capitalize())

        self.scale = [scale[i % 12] for i in range(idx, idx+12)]

    def chromatic(self):
        return self.scale

    def interval(self, intervals):
        return [self.scale[sum(Steps[x] for x in intervals[:i])]
                for i in range(len(intervals))]
