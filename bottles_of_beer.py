def bottles_of_beer(bob):
    '''
    Prints 99 Bottle of Beer on the Wall lyrics.

    :param bob: Must be a positive integer

    '''
    # first law of recursion : base case
    if bob < 1:
        print('''
            No more bottles of beer on the wall. 
            No more bottles of beer.
            ''')
        return
    tmp = bob
    # second law of recursion : change state and move to base case
    bob -= 1
    print('''
        {} bottles of beer on the wall.
        {} bottles of beer.
        Take one down, pass it around, {} bottles of beer on the wall.
        '''.format(tmp, tmp, bob))
    # third law of recursion : call upon itself
    bottles_of_beer(bob)


bottles_of_beer(99)