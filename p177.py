#No.1
class Square:
    square_list = []

    def __init__(self, l):
        self.square_list.append(self)
        self.length1 = l
        self.length2 = l
        self.length3 = l
        self.length4 = l

    def __str__(self):
        return "{} by {} by {} by {}".format(self.length1, self.length2, self.length3, self.length4)

s1 = Square(1)
s2 = Square(2)
print(s2.square_list)
print(s2)

#No.3
def check_object(o1, o2):
    if o1 is o2:
        return True
    else:
        return False

print(check_object(s1, s2))
print(check_object(s1, s1))



