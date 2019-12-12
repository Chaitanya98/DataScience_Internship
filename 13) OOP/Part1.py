class Bag :
    size=0
    __contents=[]
    def __init__(self, size) : #Python constructor for the class 
        self.bagSize = size
        self.__contents = []
    def add(self, item) :
        self.__contents.append(item)
    def getContents(self):
        return self.__contents
        
bag1=Bag(5)
bag1.add("Pen")
