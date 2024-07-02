class myclass:
    __hidden=0
    def add(self,increment):
        self.__hidden+=increment
        print(self.__hidden)
myobject=myclass()
myobject.add(2)
myobject.add(5)
print(myobject.__hidden)
