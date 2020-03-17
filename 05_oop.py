class PlayerCharacter:
    '''
    PlayerCharacter Docstring:
    this part should be the documentation for this class
    '''
    #Class Object attribute (static)
    membership = True

    # this is the constructor
    # self it's the same equivalent to 'this' in js code
    def __init__(self, name, age=0):
        #attributes
        # all attributes and methods are public and can be overridden
        # the only "convention" to indicate a private var is adding and underscore
        self._name = name
        self.age = age

    # declaring a method
    def run(self):
        print('Running')

    def shout(self):
        print(f'My name is {self._name}!')

    '''
    These two methods are the equivalent of static methods in Java
    They can be called referring directly to the class, w/o instantiating an obj
    '''

    @classmethod
    def getPlayer(cls, num1):
        return cls('Mario', num1 * 5)

    #The only difference in this one is that it has no access to the 'cls' attr
    @staticmethod
    def getPlayer2(num1):
        return num1 * 5


print(PlayerCharacter.getPlayer2(2))

# instantiating a new obj
player1 = PlayerCharacter('Elo')
# executing a method
player1.run()
player1.shout()
