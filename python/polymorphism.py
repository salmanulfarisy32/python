class bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly but some connot")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostrich cannot fly")

obj_bird=bird()
obj_spr=sparrow()
obj_ost=ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()