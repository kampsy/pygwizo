#!/usr/bin/env python3


class Ingest:
    def __init__(self, word):
        collection = []
        # Change word_lowering to lowercase
        word_lower = word.lower()
        num = 0
        for i in word_lower:
            # Check for y at the beginning of the word
            if num == 0:
                if i == "y" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                    collection.append("v")
                else:
                    collection.append("c")
                continue

            # If Y is preceded by a vowel Y becomes a consonant and if Y is preceded
            # by a consonant Y becomes a vowel.
            if collection[num-1] == "v" and i == "y":
                collection.append("c")
                continue
            elif collection[num-1] == "c" and i == "y":
                collection.append("v")
                continue

            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                collection.append("v")
            else:
                collection.append("c")

            num += 1

        self.word = word_lower
        # create the vowel con partern
        vc = ""
        for i in collection:
            vc += i
        self.vowcon = vc
        self.measure = vc.count("vc")

    # Method HasVowel returns bool (*v*)
    def hasvowel(self):
        return self.vowcon
    
if __name__ == "__main__":
    val = Ingest("information")
    print(val.word, val.vowcon, val.measure)
