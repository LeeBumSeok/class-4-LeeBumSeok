class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = "_" * len(word)

    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", str(self.numTries))

    def guess(self, character):
        if character not in self.guessedChars:
            self.guessedChars.append(character)

        if character not in self.secretWord:
            self.numTries += 1
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
            if self.secretWord == self.currentStatus:
                return True



