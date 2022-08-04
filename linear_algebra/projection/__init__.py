# import numpy as np
#
# A = np.array([
#     [1, 6],
#     [0, 9],
# ])
#
# B = np.array([
#     [3, 0],
#     [3, 3],
# ])
#
# print(np.linalg.eig(A))
# print(np.linalg.eig(B))
# print(np.linalg.det(A))
# print(np.linalg.det(B))
#
# print(np.linalg.eig(np.array([
#     [2, 3 - 3j],
#     [3 + 3j, 5],
# ])))


class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


def generate():
    l = [1, 2, 333]
    print(l)
    print(id(l))
    return l


def callee(arr):
    arr = None  # change obj be point at
    print('arr``````````')
    print(arr)  # none
    print(id(arr))
    print('arr~~~~~~~')
    arr2 = arr
    return arr, arr2


from array import array


class Vector:
    typecode = 'd'

    @staticmethod
    def acc(a,b,c):
        # print(args)
        return

    def __init__(self, comps):
        array(self.typecode, comps)
        pass


if __name__ == '__main__':
    Vector.acc(*range(1, 9))

    # y = Gizmo()*10;
    #
    # print(gizmo)
    l = generate()
    print(l)
    print(id(l))

    print("~~~~~~")
    charles = {"dragon", "postoffice"}
    print(id(charles))

    a1, a2 = callee(charles)
    print("a1,a2")
    print(a1, a2)
    print(id(a1), id(a2))

    lew = charles

    print(id(charles))
    print(charles)
    charles.add("ccx")
    print(charles)
    print(id(charles))

    # 修改内部并不改变id

    # print(id("dragon"))
    # print(id("dragon"))
    # print(id(.3))
    # print(id(.3))
    # print("1 is 1")
    # print("dragon" is "dragon")
    # (==,!=) compare by value , (is,is not) compare by id
    # alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

    # == 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识
    #  a is b as/what c to b
    print(id(lew), id(charles))
