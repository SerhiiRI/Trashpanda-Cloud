'''
class Brain(object):

    def __init__(self):
        self.__behaviour = dict()
        self.priceValue = 1

    def update(self, ID, compatible, price, yes_no):
        if ID not in self.__behaviour.keys():
            self.__behaviour[ID] = list()
        if yes_no:
            self.__behaviour[ID] = list()
        self.__behaviour[ID].append((compatible, price))
        self.priceValue = (self.priceValue * 1.2) if yes_no else (self.priceValue * 0.95)


    def getprice(self, ID):
        crit_price = 1
        fprice = 1
        for compatible, price in self.__behaviour[ID]:
            crit_price += compatible * 0.99
            fprice += price
        crit_price /= len(self.__behaviour[ID])
        fprice /= len(self.__behaviour[ID])
        fprice = crit_price if fprice < crit_price else fprice
        fprice *= self.priceValue
        return "{:.2f}".format(fprice)

    def getstartprice(self, compatible):
        return "{:.2f}".format(compatible)

'''

class Brain(object):

    def __init__(self):
        self.__behaviour = dict()
        self.priceValue = 1

    def update(self, ID, compatible, price, yes_no):
        if ID not in self.__behaviour.keys():
            self.__behaviour[ID] = list()
        if yes_no:
            self.__behaviour[ID] = list()
        self.__behaviour[ID].append((compatible, price))
        self.priceValue = (self.priceValue * 1.2) if yes_no else (self.priceValue * 0.95)


    def getprice(self, ID):
        crit_price = 1
        fprice = 1
        for compatible, price in self.__behaviour[ID]:
            crit_price += compatible * 0.99
            fprice += price
        crit_price /= len(self.__behaviour[ID])
        fprice /= len(self.__behaviour[ID])
        fprice = crit_price if fprice < crit_price else fprice
        fprice *= self.priceValue
        return "{:.2f}".format(fprice)

    def getstartprice(self, compatible):
        return "{:.2f}".format(compatible)