from static.classes.datacontroller.SQLController import SQLCloud


class Controller(SQLCloud):

    def __init__(self):
        SQLCloud.__init__(self)


    def do(self, email, ban=False, stat=False, links=False, to_delete=False, to_root=False):
        print("KeyValue -<[", email, ban, stat, links, to_delete, to_root,"]>-")