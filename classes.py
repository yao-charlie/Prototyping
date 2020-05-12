




class item:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class clothing(item):

    def __init__(self, name, price, weight, material, type, temp_high, temp_low):
        item.__init__(self, name, price, weight)
        self.type = type
        self.temp_high = temp_high
        self.temp_low = temp_low
        self.material = material

'''
class consumable(item):
    def __init__(self, type):
        self.type = type


class potion(consumable):

    def __init__(self, ):

'''