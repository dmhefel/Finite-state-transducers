'''Daniel Hefel'''

from fst import FST
import string

class Parser():

    def __init__(self):
        pass

    def generate(self, analysis):
        """Generate the morphologically correct word

        e.g.
        p = Parser()
        analysis = ['p','a','n','i','c','+past form']
        p.generate(analysis)
        ---> 'panicked'
        """

        # Let's define our first FST
        f1 = FST('morphology-generate')
        vowels = ['a','e','o','u','i']
        not_c= ['a','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        f1.add_state('start')
        f1.initial_state = 'start'
        f1.add_state('one')
        f1.add_state('two')
        f1.add_state('three')
        f1.add_state('four')
        f1.add_state('five')
        f1.set_final('five')
        f1.add_state('six')
        f1.set_final('six')

        for letter in not_c:
            f1.add_arc('start','four', letter, letter)
        for letter in string.ascii_letters:
            f1.add_arc('start','start', letter, letter)
        for letter in vowels:
            f1. add_arc('start','one', letter, letter)
        for letter in string.ascii_letters:
            if letter not in vowels:
                f1.add_arc('start','three', letter, letter)

        f1.add_arc('one','two','c','c')
        f1.add_arc('two','four','','k')
        f1.add_arc('three','four', 'c','c')
        f1.add_arc('four','five','+past form', 'ed')
        f1.add_arc('four','six','+present participle form','ing')




        output = f1.transduce(analysis)[0]
        return ''.join(output)

    def parse(self, word):
        """Parse a word morphologically

        e.g.
        p = Parser()
        word = ['p','a','n','i','c','k','i','n','g']
        p.parse(word)
        ---> 'panic+present participle form'
        """

        # Ok so now let's do the second FST
        f2 = FST('morphology-parse')

        vowels = ['a','e','o','u','i']
        not_c= ['a','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        f2.add_state('start')
        f2.initial_state = 'start'
        f2.add_state('one')
        f2.add_state('two')
        f2.add_state('three')
        f2.add_state('four')
        f2.add_state('five')
        f2.add_state('six')
        f2.add_state('seven')
        f2.add_state('eight')
        f2.set_final('four')
        f2.add_state('nine')
        f2.add_state('ten')
        f2.add_state('eleven')


        f2.add_arc('three','four','d','+past form')
        f2.add_arc('six','four','g','+present participle form')
        f2.add_arc('five','six','n','')
        f2.add_arc('two','three','e','')
        f2.add_arc('two','five','i','')
        f2.add_arc('eight','two','k','')
        f2.add_arc('seven','eight','c','c')
        f2.add_arc('one', 'two', 'c','c')
        f2.add_arc('start', 'eleven', 'l', 'l')
        f2.add_arc('eleven', 'ten','i','i')
        f2.add_arc('ten','nine','c','c')
        f2.add_arc('nine','two','k','k')
        for letter in not_c:
            f2.add_arc('start','two', letter, letter)
        for letter in string.ascii_letters:
            if letter != 'l':
                f2.add_arc('start','start', letter, letter)
        for letter in vowels:
            f2.add_arc('start','seven', letter, letter)
        for letter in string.ascii_letters:
            if letter not in vowels:
                f2.add_arc('start','one', letter, letter)



        output = f2.transduce(word)[0]
        return ''.join(output)
