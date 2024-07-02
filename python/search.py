import re
txt="The rain in spain"
x=re.search("\s",txt)
print("The first white-space charector is located in position:",x.start())