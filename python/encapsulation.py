class base:
    def __init__(self):
        self.a="geekforgeeks"
        self.b="geekforgeeksnew"
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Calling private member of base class: ")
        print(self.b)
obj1=base()
print(obj1.b)