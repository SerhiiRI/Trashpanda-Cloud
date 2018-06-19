class Brain(object):

    def __init__(self, pref_price):
        self.criticalPrice = pref_price + pref_price*0.05
        self.pref_price = pref_price
        self.blad = 1

        # Collections of agent data
        self.AllCollection = list()
        self.PortCollection = dict()

        # Value:
        self.priceValue = 1
        self.prep_PortMean = 0
        self.prep_AllMean = 0

        # Mean Value
        self.PortMeanValue = 0
        self.AllMeanValue = 0
        print("[CLIENT], Money={}".format(pref_price))

    def update(self, port, price):
        self.AllCollection.append(price)
        if port not in self.PortCollection:
            self.PortCollection[port] = list()
        self.PortCollection[port].append(price)
        # print(self.AllCollection)
        # print(self.PortCollection)
        localAllMean = sum(self.AllCollection) / len(self.AllCollection)
        localPortMean = sum(self.PortCollection[port]) / len(self.PortCollection[port])
        # print("Mean by ALL prices = {localMean}".format(localMean=localAllMean))
        # print("Mean by PORT prices = {localMean}".format(localMean=localPortMean))

    def GetHandShackingType(self, port):
        from static.tool.console.vt1000 import BackGround, ForeGround, FormatCode, getTerminalSize
        port = int(port)
        comparator = 100
        try:
            comparator = self.PortCollection[port][-2]
        except:
            comparator = 100
        if port not in self.PortCollection:
            print(BackGround.blue + "START" + FormatCode.reset)
            return "start"
        elif (self.pref_price < self.PortCollection[port][-1]):
            print(BackGround.orange + "ORDER" + BackGround.blue + "->{}".format(
                self.PortCollection[port][-1]) + FormatCode.reset)
            return "order"
        elif (self.pref_price >= self.PortCollection[port][-1]):
            print(BackGround.red + "FINALIZE" + FormatCode.reset)
            print(self.pref_price, " >= ", self.PortCollection[port][-1])
            return "finalize"
        elif (self.blad >= abs(comparator - self.PortCollection[port][-1])) :
            print(BackGround.red + "FINALIZE" + FormatCode.reset)
            print(self.pref_price, " >= ", self.PortCollection[port][-1])
            return "finalize"
        else:
            return "order"
