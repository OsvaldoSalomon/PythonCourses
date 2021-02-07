class Base1:
    x = "base1"


class Base2:
    x = "base2"


class Derived(Base1, Base2):
    pass


print(Derived.x)

print(Derived.mro())
