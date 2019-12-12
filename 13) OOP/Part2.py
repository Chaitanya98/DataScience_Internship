from Part1 import Bag

class LaptopBag(Bag):
  def __init__(self,size=5,color='Red'):
    super().__init__(size)
    self.color=color
    
  def delItem(self,item):
    if item in self.__contents:
      self._Bag__contents.remove(item)
      
l1=LaptopBag()
l1.add('Pencil')
l1.add('Book')
print(l1.getContents())
l1.delItem('Book')
print(l1.getContents())
