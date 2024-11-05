class A:
    def do_something(self):
        print("Method defined in: A")

class B(A):
    def do_something(self):
        print("Method defined in: B")

class C(A):
    def do_something(self):
        print("Method defined in: C")

class D(B, C):
    def do_something(self):
        print("Method defined in: D")

thing = D()
thing.do_something()

    #     A
    #   /   \
    #  B     C
    #   \   /
    #     D
    # Method resolution order(mro)  => D,B,C,A,object