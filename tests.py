import unittest
from soundex import letters_to_numbers, truncate_to_three_digits, add_zero_padding, soundex_convert
from morphology import Parser

class TestHW1(unittest.TestCase):

    def setUp(self):
        self.f1 = letters_to_numbers()
        self.f2 = truncate_to_three_digits()
        self.f3 = add_zero_padding()
        self.mparser = Parser()

    def test_letters(self):
        self.assertEqual("".join(self.f1.transduce("washington")[0]), "w25235")
        self.assertEqual("".join(self.f1.transduce("jefferson")[0]), "j1625")
        self.assertEqual("".join(self.f1.transduce("adams")[0]), "a352")
        self.assertEqual("".join(self.f1.transduce("bush")[0]), "b2")


    def test_truncation(self):
        self.assertEqual("".join(self.f2.transduce("a33333")[0]), "a333")
        self.assertEqual("".join(self.f2.transduce("a123456")[0]), "a123")
        self.assertEqual("".join(self.f2.transduce("j612")[0]), "j612")
        self.assertEqual("".join(self.f2.transduce("l5")[0]), "l5")

    def test_padding(self):
        self.assertEqual("".join(self.f3.transduce("z3")[0]), "z300")
        self.assertEqual("".join(self.f3.transduce("j612")[0]), "j612")
        self.assertEqual("".join(self.f3.transduce("c111")[0]), "c111")

    def test_soundex(self):
        self.assertEqual(soundex_convert("jurafsky"), "j612")
        self.assertEqual(soundex_convert("jarovski"), "j612")
        self.assertEqual(soundex_convert("reznik"), "r252")
        self.assertEqual(soundex_convert("euler"), "e460")
        self.assertEqual(soundex_convert("peterson"), "p362")
        self.assertEqual(soundex_convert("ashcroft"), "a226")
        self.assertEqual(soundex_convert("pfister"), "p236")



    def test_morphology(self):
        havocking = list('panicking')
        self.assertEqual(self.mparser.parse(havocking), "panic+present participle form")
        lick = ['p','a','n', 'i', 'c','+present participle form']
        self.assertEqual(self.mparser.generate(lick), "panicking")

if __name__ == '__main__':
    unittest.main()
