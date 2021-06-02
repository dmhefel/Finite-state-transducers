'''Daniel Hefel'''
from fst import FST
import string, sys
from fsmutils import compose


def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    #lists of conversions
    vowels = ['a','e','h','i','o','u','w','y']
    q1 = ['b','f','p','v']
    q2 = ['c','g','j','k','q','s','x','z']
    q3 = ['d','t']
    q4 = ['l']
    q5 = ['m','n']
    q6 = ['r']




    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that 'start' is the initial state
    f1.add_state('start')

    f1.initial_state = 'start'


    f1.add_state('one')
    f1.add_state('two')
    f1.add_state('three')
    f1.add_state('four')
    f1.add_state('five')
    f1.add_state('six')
    f1.add_state('seven')
    f1.add_state('eight')




    # Set all the final states
    f1.set_final('one')
    f1.set_final('two')
    f1.set_final('three')
    f1.set_final('four')
    f1.set_final('five')
    f1.set_final('six')
    f1.set_final('seven')
    f1.set_final('eight')


    # Add the rest of the arcs

    for letter in string.ascii_letters:
        if letter.lower() in q1:
            f1.add_arc('start','two',letter,letter)
        elif letter.lower() in q2:
            f1.add_arc('start','three',letter,letter)
        elif letter.lower() in q3:
            f1.add_arc('start', 'four', letter, letter)
        elif letter.lower() in q4:
            f1.add_arc('start', 'five', letter, letter)
        elif letter.lower() in q5:
            f1.add_arc('start', 'six', letter, letter)
        elif letter.lower() in q6:
            f1.add_arc('start', 'seven', letter, letter)
        else:
            f1.add_arc('start', 'one', letter, letter)
        if letter.lower() in vowels:
            f1.add_arc('one', 'eight', letter, '')
            f1.add_arc('two', 'eight', letter, '')
            f1.add_arc('three', 'eight', letter, '')
            f1.add_arc('four', 'eight', letter, '')
            f1.add_arc('five', 'eight', letter, '')
            f1.add_arc('six', 'eight', letter, '')
            f1.add_arc('seven', 'eight', letter, '')
            f1.add_arc('eight','eight',letter, '')

        elif letter.lower() in q1:
            f1.add_arc('two', 'two', letter, '')
            f1.add_arc('one', 'two', letter, '1')
            f1.add_arc('three', 'two', letter, '1')
            f1.add_arc('four', 'two', letter, '1')
            f1.add_arc('five', 'two', letter, '1')
            f1.add_arc('six', 'two', letter, '1')
            f1.add_arc('seven', 'two', letter, '1')
            f1.add_arc('eight','two',letter, '1')

        elif letter.lower() in q2:
            f1.add_arc('three', 'three', letter, '')
            f1.add_arc('one', 'three', letter, '2')
            f1.add_arc('two', 'three', letter, '2')
            f1.add_arc('four', 'three', letter, '2')
            f1.add_arc('five', 'three', letter, '2')
            f1.add_arc('six', 'three', letter, '2')
            f1.add_arc('seven', 'three', letter, '2')
            f1.add_arc('eight','three',letter, '2')

        elif letter.lower() in q3:
            f1.add_arc('four', 'four', letter, '')
            f1.add_arc('one', 'four', letter, '3')
            f1.add_arc('three', 'four', letter, '3')
            f1.add_arc('two', 'four', letter, '3')
            f1.add_arc('five', 'four', letter, '3')
            f1.add_arc('six', 'four', letter, '3')
            f1.add_arc('seven', 'four', letter, '3')
            f1.add_arc('eight','four',letter, '3')

        elif letter.lower() in q4:
            f1.add_arc('five', 'five', letter, '')
            f1.add_arc('four', 'five', letter, '4')
            f1.add_arc('one', 'five', letter, '4')
            f1.add_arc('two', 'five', letter, '4')
            f1.add_arc('three', 'five', letter, '4')
            f1.add_arc('six', 'five', letter, '4')
            f1.add_arc('seven', 'five', letter, '4')
            f1.add_arc('eight','five',letter, '4')

        elif letter.lower() in q5:
            f1.add_arc('six', 'six', letter, '')
            f1.add_arc('five', 'six', letter, '5')
            f1.add_arc('one', 'six', letter, '5')
            f1.add_arc('two', 'six', letter, '5')
            f1.add_arc('three', 'six', letter, '5')
            f1.add_arc('four', 'six', letter, '5')
            f1.add_arc('seven', 'six', letter, '5')
            f1.add_arc('eight','six',letter, '5')

        elif letter.lower() in q6:
            f1.add_arc('seven', 'seven', letter, '')
            f1.add_arc('six', 'seven', letter, '6')
            f1.add_arc('one', 'seven', letter, '6')
            f1.add_arc('two', 'seven', letter, '6')
            f1.add_arc('three', 'seven', letter, '6')
            f1.add_arc('four', 'seven', letter, '6')
            f1.add_arc('five', 'seven', letter, '6')
            f1.add_arc('six', 'seven', letter, '6')
            f1.add_arc('eight','seven', letter, '6')


    return f1

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.initial_state = '1'
    f2.set_final('1')
    f2.add_state('2')
    f2.set_final('2')
    f2.add_state('3')
    f2.set_final('3')
    f2.add_state('4')
    f2.set_final('4')
    f2.add_state('5')
    f2.set_final('5')
    #for the letter in the beginning
    for letter in string.ascii_letters:
        f2.add_arc('1', '2', letter, letter)
    #for the numbers
    for i in range(1,7):

        f2.add_arc('2', '3', str(i), str(i))
        f2.add_arc('3', '4', str(i), str(i))
        f2.add_arc('4', '5', str(i), str(i))
        f2.add_arc('5', '5', str(i),'')


    return f2

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
    f3.initial_state = '1'
    f3.set_final('4')
    for letter in string.ascii_letters:
        f3.add_arc('1', '1', letter, letter)
    f3.add_arc('1', '4', '', '000')
    f3.add_arc('2', '4', '', '00')
    f3.add_arc('3', '4', '', '0')

    for i in range(1,7):
        f3.add_arc('1', '2', str(i), str(i))
        f3.add_arc('2', '3', str(i), str(i))
        f3.add_arc('3', '4', str(i), str(i))



    return f3

def soundex_convert(name_string):
    """Combine the three FSTs above and use it to convert a name into a Soundex"""
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()
    x= compose(name_string, f1,f2,f3)
    final = ''
    for item in x[0]:
        final+=item
    return final

'''if __name__ == '__main__':
    user_input = input().strip()

    if user_input:
        print("%s -> %s" % (user_input, soundex_convert(list(user_input))))'''
letters_to_numbers()
