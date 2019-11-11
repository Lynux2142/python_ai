class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    "A class representing the Stark family. Or when bad things happen to good people."
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Stark'
        self.house_words = 'Winter is Comming'
        self.__dict__['first_name'] = self.first_name
        self.__dict__['is_alive'] = self.is_alive
        self.__dict__['family_name'] = self.family_name
        self.__dict__['house_words'] = self.house_words
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False
