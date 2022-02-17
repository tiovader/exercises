STATUS_WIN = "W"
STATUS_LOSE = "L"
STATUS_ONGOING = "..."


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.word = word
        self.__guessed__ = {n: False for n in set(word)}

    def guess(self, char):
        if self.get_status() != STATUS_ONGOING:
            raise ValueError('Game Over!')

        try:
            if not self.__guessed__[char]:
                self.__guessed__[char] = char in self.word
            else:
                raise KeyError
        except KeyError:
            self.remaining_guesses -= 1

    def get_masked_word(self):
        return ''.join(n if self.__guessed__[n] else '_' for n in self.word)

    def get_status(self):
        return STATUS_WIN if all(n for n in self.__guessed__.values()) \
            else STATUS_ONGOING if self.remaining_guesses >= 0 \
            else STATUS_LOSE
