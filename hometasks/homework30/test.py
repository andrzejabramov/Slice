
# a, b, c = 10, 20, 15
# # a = 10
# # b = 20
# # c = 15
#
#
# s = (a + b + c) / 2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# h = area * 2 / c
# print(area, h)

def test(*args):
    for i in args:
        print(i, type(i))

print(test(1))