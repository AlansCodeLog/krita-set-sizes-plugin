from krita import *

class MyExtension(Extension):

    def __init__(self, parent):
        # This is initializing the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        for size in range(1,10):
            action = window.createAction("set_size_"+ str(size), "Set Size " + str(size) + "px", "")
            action.triggered.connect(getattr(self, "set_size_"+str(size)))

    def set_size_1(self):
        self.set_size(5)
    def set_size_2(self):
        self.set_size(7)
    def set_size_3(self):
        self.set_size(10)
    def set_size_4(self):
        self.set_size(15)
    def set_size_5(self):
        self.set_size(20)
    def set_size_6(self):
        self.set_size(60)
    def set_size_7(self):
        self.set_size(100)
    def set_size_8(self):
        self.set_size(200)
    def set_size_9(self):
        self.set_size(300)
    def set_size_10(self):
        self.set_size(400)
    def set_size(self, size):
        # Get the document:
        win = Krita.instance().activeWindow()
        view = win.activeView()
        view.setBrushSize(size)


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(MyExtension(Krita.instance()))
