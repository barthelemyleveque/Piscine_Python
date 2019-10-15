class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
    
class Greyjoy(GotCharacter):
    '''Une famille de zinzins dont certains sans zizis '''
    def __init__(self, first_name=True, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Greyjoy"
        self.house_words = "We do not sow."
    
    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        super().__setattr__("is_alive", False)