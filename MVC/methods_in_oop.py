class Pizza():
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return 'Pizza %s'% self.ingredients
    #factory function
    @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomatoes'])

    @classmethod
    def posciutto(cls):
        return  cls(['mozzarella', 'tomatoes', 'ham'])
pizza = Pizza(['cheese', 'tomatoes'])
print (pizza)
print(pizza.margherita())
