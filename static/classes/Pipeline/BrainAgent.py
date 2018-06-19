class Brain(object):

    def __init__(self):
        self.__behaviour = dict()
        self.clientValue = dict()
        self.priceValue = 1
        self.criticalPrice = dict()

    def update(self, ID, yes_no):
        if ID not in self.clientValue.keys():
            self.clientValue[ID] = 1
            self.criticalPrice = dict()

        if yes_no:
            self.clientValue[ID] = 1
            self.__behaviour[ID] = list()
        self.clientValue[ID] = (self.clientValue[ID]) * 1.05 if yes_no else (self.clientValue[ID] * 0.95)
        self.priceValue = 1 if yes_no else (1 - self.priceValue * 0.05)

    def generator(self, compat):
        compatible = compat
        x=1
        while(1):
            yield int(compatible/2) + int(compatible / 2) * 1/x
            x += 1


    def getprice(self, compatible, ID):
        if ID not in self.criticalPrice.keys():
            x = self.generator(compatible)
            self.criticalPrice[ID] = tuple((compatible / 2, x))

        fprice = 1
        if ID not in self.__behaviour.keys():
            self.__behaviour[ID] = list()
            self.__behaviour[ID].append((compatible, compatible))
        if ID not in self.clientValue.keys():
            self.clientValue[ID] = 1

        for compatible, price in self.__behaviour[ID]:
            fprice += price
        fprice /= len(self.__behaviour[ID])
        fprice *= 1
        import time
        #fprice = self.criticalPrice[ID] if fprice < self.criticalPrice[ID][1].__next__() else fprice
        final_price = self.criticalPrice[ID][1].__next__() * self.clientValue[ID] * self.priceValue
        self.__behaviour[ID].append((compatible, fprice))
        print("ID:[", ID, "] COmpat:",compatible, " pValue= ", self.priceValue, "% ID_Value:",self.clientValue[ID],"%")
        return "{:.2f}".format(final_price)

    def getstartprice(self, compatible):
        return "{:.2f}".format(compatible)