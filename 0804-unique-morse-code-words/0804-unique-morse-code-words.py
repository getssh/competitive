class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter_map = {
            "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",
            "e": ".",     "f": "..-.",  "g": "--.",   "h": "....",
            "i": "..",    "j": ".---",  "k": "-.-",   "l": ".-..",
            "m": "--",    "n": "-.",    "o": "---",   "p": ".--.",
            "q": "--.-",  "r": ".-.",   "s": "...",   "t": "-",
            "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",
            "y": "-.--",  "z": "--.."
        }

        res = set()

        for word in words:
            coded = ""
            for let in word:
                coded += letter_map[let]
            res.add(coded)
        
        return len(res)