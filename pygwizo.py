#!/usr/bin/env python3


# Contains method checks if word contains a specified letter.
def contains(w, l):
    for s in w:
        if s == l:
            return True
    return False


# Measure value equal to 1
def has_measure_equal_to_1(w):
    cls = Ingest(w)
    if cls.measure == 1:
        return True
    else:
        return False


# Function accepts a string as an argument, checks if it has double consonant
# as suffix and returns a boolean
def has_same_double_consonant(w):
    cls = Ingest(w)
    cc = cls.vowcon.endswith("cc")
    if cc is True:
        word_length = (len(w) - 1)
        letter = w[word_length]
        letter_2 = w[(word_length - 1)]
        if letter == letter_2:
            return True
        else:
            return False
    else:
        return False


# The trim suffix function
def trim_suffix(w, n):
    num = len(n)
    return w[:(len(w) - num)]


class Ingest:
    def __init__(self, word):
        """

        :rtype: returns a list
        """
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
            if collection[num - 1] == "v" and i == "y":
                collection.append("c")
                continue
            elif collection[num - 1] == "c" and i == "y":
                collection.append("v")
                continue

            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                collection.append("v")
            else:
                collection.append("c")

            num += 1

        self.word = word_lower
        # create the vowel consonant pair
        vc = ""
        for i in collection:
            vc += i
        self.vowcon = vc
        self.measure = vc.count("vc")

    # remake
    def thinian(self, word):
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
            if collection[num - 1] == "v" and i == "y":
                collection.append("c")
                continue
            elif collection[num - 1] == "c" and i == "y":
                collection.append("v")
                continue

            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                collection.append("v")
            else:
                collection.append("c")

            num += 1

        self.word = word_lower
        # create the vowel consonant pair
        vc = ""
        for i in collection:
            vc += i
        self.vowcon = vc
        self.measure = vc.count("vc")

    # Method hasvowel returns bool (*v*)
    def has_vowel(self):
        return contains(self.vowcon, "v")

    # Method hasconsonant returns bool (*v*)
    def has_consonant(self):
        return contains(self.vowcon, "c")

    # Measure value is grater than 0
    def measure_greater_than_0(self):
        if self.measure > 0:
            return True
        else:
            return False

    # Measure value is grater than 1
    def measure_greater_than_1(self):
        if self.measure > 1:
            return True
        else:
            return False

    # Function checks if VowCon pattern ends with cvc, where second c is not W, X, Y
    def has_cvc_end_last_not_w_x_y(self, w):
        cls = Ingest(w)
        cvc = cls.vowcon.endswith("cvc")
        word_length = len(cls.word)
        last_letter = self.word[(word_length - 1)]
        w = contains(last_letter, "w")
        x = contains(last_letter, "x")
        y = contains(last_letter, "y")
        if cvc is True and w is False and x is False and y is False:
            return True
        else:
            return False

    # Function checks if word has suffix S or T
    def has_end_s_t(self):
        s = self.word.endswith("s")
        t = self.word.endswith("t")

        if s is True or t is True:
            return True
        else:
            return False

    # Function checks if word has suffix L
    def has_end_l(self):
        l = self.word.endswith("l")
        if l is True:
            return True
        else:
            return

    # Step 1 deals with plurals and past participles. The subsequent steps are
    # much more straightforward.
    # Step 1a rules.
    # ======================================
    def step_1a(self):
        self.thinian(self.word)
        # For SSES suffix. SSES -> SS
        sses = self.word.endswith("sses")
        if sses is True:
            pre = trim_suffix(self.word, "sses")
            wrd = pre + "ss"
            return wrd

        # For IES suffix. IES -> I
        ies = self.word.endswith("ies")
        if ies is True:
            pre = trim_suffix(self.word, "ies")
            wrd = pre + "i"
            return wrd

        # For SS suffix. SS -> SS
        ss = self.word.endswith("ss")
        if ss is True:
            pre = trim_suffix(self.word, "ss")
            wrd = pre + "ss"
            return wrd

        # For SS suffix. S ->
        s = self.word.endswith("s")
        if s is True:
            pre = trim_suffix(self.word, "s")
            wrd = pre
            return wrd

        return self.word

    # Step 1b rules.
    # ======================================
    def step_1b(self):
        self.thinian(self.word)
        # Word Measure (m > 0) and EED suffix. EED -> EE
        eed = self.word.endswith("eed")
        if eed is True and self.measure > 0:
            if len(self.word) == 4:
                return self.word
            else:
                pre = trim_suffix(self.word, "eed")
                wrd = pre + "ee"
                return wrd

        # Word has Vowel and ED suffix. ED ->
        ed = self.word.endswith("ed")
        if ed is True and self.has_vowel() is True:
            if len(self.word) == 4:
                return self.word
            else:
                pre = trim_suffix(self.word, "ed")
                self.word = pre

        # Word has Vowel and ING suffix. ING ->
        ing = self.word.endswith("ing")
        if ing is True and self.has_vowel() is True:
            if len(self.word) == 4:
                return self.word
            else:
                pre = trim_suffix(self.word, "ing")
                self.word = pre

        # If the second or third of the above rules is successful the following is done
        if ed is True:
            # Word has AT suffix. AT -> ATE
            at = self.word.endswith("at")
            if at is True:
                pre = trim_suffix(self.word, "at")
                wrd = pre + "ate"
                return wrd

            # Word has BL suffix. BL -> BLE
            bl = self.word.endswith("bl")
            if bl is True:
                pre = trim_suffix(self.word, "bl")
                wrd = pre + "ble"
                return wrd

            # Word has IZ suffix. IZ -> IZE
            iz = self.word.endswith("iz")
            if iz is True:
                pre = trim_suffix(self.word, "iz")
                wrd = pre + "ize"
                return wrd

        # (*d and not (*L or *S or *Z)) -> single letter at the end
        if ed is True or ing is True:
            if has_same_double_consonant(self.word) is True:
                ll = self.word.endswith("ll")
                ss = self.word.endswith("ss")
                zz = self.word.endswith("zz")
                if ll is True or ss is True or zz is True:
                    return self.word
                else:
                    strlen = len(self.word)
                    last_letter = self.word[:(strlen - 1)]
                    self.word = last_letter
                    return self.word

        # (m=1 and *o) -> E
        if ing is True:
            if has_measure_equal_to_1(self.word) is True and self.has_cvc_end_last_not_w_x_y(self.word):
                pre = self.word + "e"
                return pre

        return self.word

    # Step 1c rules.
    # ======================================
    def step_1c(self):
        self.thinian(self.word)
        # (*v*) Y -> I
        # Word has Vowel and Y suffix. Y -> I
        y = self.word.endswith("y")
        if y is True and self.has_vowel() is True:
            if len(self.word) <= 3:
                return self.word
            else:
                pre = trim_suffix(self.word, "y")
                wrd = pre + "i"
                return wrd
        else:
            return self.word

    # Step 2 rules.
    # ======================================
    def step_2(self):
        self.thinian(self.word)
        if self.measure_greater_than_0() is True:
            # For ATIONAL suffix. ATIONAL -> ATE
            ational = self.word.endswith("ational")
            if ational is True:
                if self.word == "rational":
                    return self.word
                else:
                    pre = trim_suffix(self.word, "ational")
                    wrd = pre + "ate"
                    return wrd

            # For TIONAL suffix. TIONAL -> TION
            tional = self.word.endswith("tional")
            if tional is True:
                if self.word == "rational":
                    return self.word
                else:
                    pre = trim_suffix(self.word, "tional")
                    wrd = pre + "tion"
                    return wrd

            # For ENCI suffix. ENCI -> ENCE
            enci = self.word.endswith("enci")
            if enci is True:
                pre = trim_suffix(self.word, "enci")
                wrd = pre + "ence"
                return wrd

            # For ANCI suffix. ANCI -> ANCE
            anci = self.word.endswith("anci")
            if anci is True:
                pre = trim_suffix(self.word, "anci")
                wrd = pre + "ance"
                return wrd

            # For IZER suffix. IZER -> IZE
            izer = self.word.endswith("izer")
            if izer is True:
                pre = trim_suffix(self.word, "izer")
                wrd = pre + "ize"
                return wrd

            # For ABLI suffix. ABLI -> ABLE
            abli = self.word.endswith("abli")
            if abli is True:
                pre = trim_suffix(self.word, "abli")
                wrd = pre + "able"
                return wrd

            # For ALLI suffix. ALLI -> AL
            alli = self.word.endswith("alli")
            if alli is True:
                pre = trim_suffix(self.word, "alli")
                wrd = pre + "al"
                return wrd

            # For ENTLI suffix. ENTLI -> ENT
            entli = self.word.endswith("entli")
            if entli is True:
                pre = trim_suffix(self.word, "entli")
                wrd = pre + "ent"
                return wrd

            # For ELI suffix. ELI -> E
            eli = self.word.endswith("eli")
            if eli is True:
                pre = trim_suffix(self.word, "eli")
                wrd = pre + "e"
                return wrd

            # For OUSLI suffix. OUSLI -> OUS
            ousli = self.word.endswith("ousli")
            if ousli is True:
                pre = trim_suffix(self.word, "ousli")
                wrd = pre + "ous"
                return wrd

            # For IZATION suffix. IZATION -> IZE
            ization = self.word.endswith("ization")
            if ization is True:
                pre = trim_suffix(self.word, "ization")
                wrd = pre + "ize"
                return wrd

            # For ATION suffix. ATION -> ATE
            ation = self.word.endswith("ation")
            if ation is True:
                pre = trim_suffix(self.word, "ation")
                wrd = pre + "ate"
                return wrd

            # For ATOR suffix. ATOR -> ATE
            ator = self.word.endswith("ator")
            if ator is True:
                pre = trim_suffix(self.word, "ator")
                wrd = pre + "ate"
                return wrd

            # For ALISM suffix. ALISM -> AL
            alism = self.word.endswith("alism")
            if alism is True:
                pre = trim_suffix(self.word, "alism")
                wrd = pre + "al"
                return wrd

            # For IVENESS suffix. IVENESS -> IVE
            iveness = self.word.endswith("iveness")
            if iveness is True:
                pre = trim_suffix(self.word, "iveness")
                wrd = pre + "ive"
                return wrd

            # For FULNESS suffix. FULNESS -> FUL
            fulness = self.word.endswith("fulness")
            if fulness is True:
                pre = trim_suffix(self.word, "fulness")
                wrd = pre + "ful"
                return wrd

            # For OUSNESS suffix. OUSNESS -> OUS
            ousness = self.word.endswith("ousness")
            if ousness is True:
                pre = trim_suffix(self.word, "ousness")
                wrd = pre + "ous"
                return wrd

            # For ALITI suffix. ALITI -> AL
            aliti = self.word.endswith("aliti")
            if aliti is True:
                pre = trim_suffix(self.word, "aliti")
                wrd = pre + "al"
                return wrd

            # For IVITI suffix. IVITI -> IVE
            iviti = self.word.endswith("iviti")
            if iviti is True:
                pre = trim_suffix(self.word, "iviti")
                wrd = pre + "ive"
                return wrd

            # For BILITI suffix. BILITI -> BLE
            biliti = self.word.endswith("biliti")
            if biliti is True:
                pre = trim_suffix(self.word, "biliti")
                wrd = pre + "ble"
                return wrd

        return self.word

    # Step 3 rules.
    # ======================================
    def step_3(self):
        self.thinian(self.word)
        if self.measure_greater_than_0() is True:
            # For ICATE suffix. ICATE -> IC
            icate = self.word.endswith("icate")
            if icate is True:
                pre = trim_suffix(self.word, "icate")
                wrd = pre + "ic"
                return wrd

            # For ATIVE suffix. ATIVE ->
            ative = self.word.endswith("ative")
            if ative is True:
                pre = trim_suffix(self.word, "ative")
                wrd = pre
                return wrd

            # For ALIZE suffix. ALIZE -> AL
            alize = self.word.endswith("alize")
            if alize is True:
                pre = trim_suffix(self.word, "alize")
                wrd = pre + "al"
                return wrd

            # For ICITI suffix. ICITI -> IC
            iciti = self.word.endswith("iciti")
            if iciti is True:
                pre = trim_suffix(self.word, "iciti")
                wrd = pre + "ic"
                return wrd

            # For ICAL suffix. ICAL -> IC
            ical = self.word.endswith("ical")
            if ical is True:
                pre = trim_suffix(self.word, "ical")
                wrd = pre + "ic"
                return wrd

            # For FUL suffix. FUL ->
            full = self.word.endswith("full")
            if full is True:
                pre = trim_suffix(self.word, "full")
                wrd = pre
                return wrd

            # For NESS suffix. NESS ->
            ness = self.word.endswith("ness")
            if ness is True:
                pre = trim_suffix(self.word, "ness")
                wrd = pre
                return wrd

        return self.word

    # Step 4 rules.
    # The suffixes will now be removed
    # ======================================
    def step_4(self):
        self.thinian(self.word)
        if self.measure_greater_than_1() is True:
            # For AL suffix. AL ->
            al = self.word.endswith("al")
            if al is True:
                pre = trim_suffix(self.word, "al")
                wrd = pre
                return wrd

            # For ANCE suffix. ANCE ->
            ance = self.word.endswith("ance")
            if ance is True:
                pre = trim_suffix(self.word, "ance")
                wrd = pre
                return wrd

            # For ENCE suffix. ENCE ->
            ence = self.word.endswith("ence")
            if ence is True:
                pre = trim_suffix(self.word, "ence")
                wrd = pre
                return wrd

            # For ER suffix. ER ->
            er = self.word.endswith("er")
            if er is True:
                pre = trim_suffix(self.word, "er")
                wrd = pre
                return wrd

            # For IC suffix. IC ->
            ic = self.word.endswith("ic")
            if ic is True:
                pre = trim_suffix(self.word, "ic")
                wrd = pre
                return wrd

            # For ABLE suffix. ABLE ->
            able = self.word.endswith("able")
            if able is True:
                pre = trim_suffix(self.word, "able")
                wrd = pre
                return wrd

            # For IBLE suffix. IBLE ->
            ible = self.word.endswith("ible")
            if ible is True:
                pre = trim_suffix(self.word, "ible")
                wrd = pre
                return wrd

            # For ANT suffix. ANT ->
            ant = self.word.endswith("ant")
            if ant is True:
                pre = trim_suffix(self.word, "ant")
                wrd = pre
                return wrd

            # For EMENT suffix. EMENT ->
            ement = self.word.endswith("ement")
            if ement is True:
                pre = trim_suffix(self.word, "ement")
                wrd = pre
                return wrd

            # For MENT suffix. MENT ->
            ment = self.word.endswith("ment")
            if ment is True:
                pre = trim_suffix(self.word, "ment")
                wrd = pre
                return wrd

            # For ENT suffix. ENT ->
            ent = self.word.endswith("ent")
            if ent is True:
                pre = trim_suffix(self.word, "ent")
                wrd = pre
                return wrd

            if self.has_end_s_t() is False:  # hack back works.
                # For ION suffix. ION ->
                ion = self.word.endswith("ion")
                if ion is True:
                    pre = trim_suffix(self.word, "ion")
                    wrd = pre
                    return wrd

            # For OU suffix. OU ->
            ou = self.word.endswith("ou")
            if ou is True:
                pre = trim_suffix(self.word, "ou")
                wrd = pre
                return wrd

            # For ISM suffix. ISM ->
            ism = self.word.endswith("ism")
            if ism is True:
                pre = trim_suffix(self.word, "ism")
                wrd = pre
                return wrd

            # For ATE suffix. ATE ->
            ate = self.word.endswith("ate")
            if ate is True:
                pre = trim_suffix(self.word, "ate")
                wrd = pre
                return wrd

            # For ITI suffix. ITI ->
            iti = self.word.endswith("iti")
            if iti is True:
                pre = trim_suffix(self.word, "iti")
                wrd = pre
                return wrd

            # For OUS suffix. OUS ->
            ous = self.word.endswith("ous")
            if ous is True:
                pre = trim_suffix(self.word, "ous")
                wrd = pre
                return wrd

            # For IVE suffix. IVE ->
            ive = self.word.endswith("ive")
            if ive is True:
                pre = trim_suffix(self.word, "ive")
                wrd = pre
                return wrd

            # For IZE suffix. IZE ->
            ize = self.word.endswith("ize")
            if ize is True:
                pre = trim_suffix(self.word, "ize")
                wrd = pre
                return wrd

        return self.word

    # Step 5a rules.
    # little tidying up
    # ======================================
    def step_5a(self):
        self.thinian(self.word)
        if self.measure_greater_than_1() is True:
            # E suffix. E ->
            e = self.word.endswith("e")
            if e is True:
                if len(self.word) > 4:
                    pre = trim_suffix(self.word, "e")
                    wrd = pre
                    return wrd
                else:
                    return self.word

        if has_measure_equal_to_1(self.word) is True and self.has_cvc_end_last_not_w_x_y(self.word) is True:
            # (m=1 and not *o) E ->
            e = self.word.endswith("e")
            if e is True:
                if len(self.word) > 4:  # this helps the above function.
                    pre = trim_suffix(self.word, "e")
                    wrd = pre
                    return wrd
                else:
                    return self.word
        return self.word

    # Step 5b rules.
    # more tidying up
    # ======================================
    def step_5b(self):
        self.thinian(self.word)
        if self.measure_greater_than_1() is True:
            if has_same_double_consonant(self.word) is True and self.has_end_l() is True:
                w = self.word
                print(self.word)
                str_len = len(w)
                last_letter = w[:(str_len - 1)]
                return last_letter

        return self.word

    # ShallowStem Returns the stem of the word. This method bells out when the word is Changed
    # ======================================
    def shallow_stem(self):
        corpus = self.word
        if len(self.word) > 4:
            stem = self.step_1a()
            if stem != corpus:
                return stem
            stem2 = self.step_1b()
            if stem2 != corpus:
                return stem2
            stem3 = self.step_1c()
            if stem3 != corpus:
                return stem3
            stem4 = self.step_2()
            if stem4 != corpus:
                return stem4
            stem5 = self.step_3()
            if stem5 != corpus:
                return stem5
            stem6 = self.step_4()
            if stem6 != corpus:
                return stem6
            stem7 = self.step_5a()
            if stem7 != corpus:
                return stem7
            stem8 = self.step_5b()
            if stem8 != corpus:
                return stem8

        return corpus

    # ShallowStemmed Returns the Step that was used to stem the word
    # ======================================
    def shallow_stemmed(self):
        corpus = self.word
        if len(self.word) > 4:
            stem = self.step_1a()
            if stem != corpus:
                return "step_1a()"
            stem2 = self.step_1b()
            if stem2 != corpus:
                return "step_1b()"
            stem3 = self.step_1c()
            if stem3 != corpus:
                return "step_1c()"
            stem4 = self.step_2()
            if stem4 != corpus:
                return "step_2()"
            stem5 = self.step_3()
            if stem5 != corpus:
                return "step_3()"
            stem6 = self.step_4()
            if stem6 != corpus:
                return "step_4()"
            stem7 = self.step_5a()
            if stem7 != corpus:
                return "step_5a()"
            stem8 = self.step_5b()
            if stem8 != corpus:
                return "step_5b()"
        corpus = "None {0} is a stem".format(self.word)
        return corpus

    # Deep Stem makes sure that the word goes through every step in the algorithm.
    # Any change made by one step is passed on to the next step
    # ======================================
    def deep_stem(self):
        corpus = self.word
        if len(self.word) > 4:
            stem = self.step_1a()
            if stem != corpus:
                self.word = stem
                corpus = stem
            stem2 = self.step_1b()
            if stem2 != corpus:
                self.word = stem2
                corpus = stem2
            stem3 = self.step_1c()
            if stem3 != corpus:
                self.word = stem3
                corpus = stem3
            stem4 = self.step_2()
            if stem4 != corpus:
                self.word = stem4
                corpus = stem4
            stem5 = self.step_3()
            if stem5 != corpus:
                self.word = stem5
                corpus = stem5
            stem6 = self.step_4()
            if stem6 != corpus:
                self.word = stem6
                corpus = stem6
            stem7 = self.step_5a()
            if stem7 != corpus:
                self.word = stem7
                corpus = stem7
            stem8 = self.step_5b()
            if stem8 != corpus:
                self.word = stem8
            return self.word

        return corpus
