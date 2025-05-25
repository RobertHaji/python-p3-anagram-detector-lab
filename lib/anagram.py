# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Sort the letters of the initialized word
        sorted_word = sorted(self.word)
        matches = []

        for candidate in possible_anagrams:
            # Sort the letters of the candidate word
            if sorted(candidate) == sorted_word:
                matches.append(candidate)

        return matches