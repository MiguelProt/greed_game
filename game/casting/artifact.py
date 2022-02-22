from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):

    def __init__(self):
        """Constructs a new Actor."""
        self.__message = ''
        
    def set_message(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

"""from game.casting.gem import Gem
from game.casting.rocks import Rock

class Artifact(Rock, Gem):

    def __init__(self):
        self.__type = ''

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type"""