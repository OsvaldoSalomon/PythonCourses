class MyRouter(object):
    """This is a class that describes the characteristics of a router."""

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is:", self.routername)
        print("The router model is:", self.model)
        print("The serial number of:", self.serialno)
        print("The IOS version is:", self.ios)
        print("The model and date combined:", self.model + manuf_date)


router1 = MyRouter('R1', '2600', '123456', '12.4')
print(router1)
print(router1.model)
print(router1.ios)
print(router1.serialno)
print(router1.routername)

print("\n")

print(router1.print_router("20181010"))

print(" --------- ")

router2 = MyRouter('R2', '7200', '101010', '12.2')

print(router2.print_router("20190101"))

print(" -------- ")

print("getattr(router2, 'ios')", getattr(router2, "ios"))

setattr(router2, "ios", "12.1")

print("getattr(router2, 'ios')", getattr(router2, "ios"))

print("hasattr(router2, 'ios': ", hasattr(router2, 'ios'))
print("hasattr(router2, 'ios2': ", hasattr(router2, 'ios2'))

print("\n")
print(" ----------- ")


class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(self.model + string)


new_router1 = MyNewRouter("newr1", "1800", "111111", "12.2", "10")
print(new_router1)
print(new_router1.portsno)
print(" ----------- ")

print(new_router1.print_router("20210101"))
print(" ----------- ")
print(new_router1.print_new_router("20210101"))

print(" --------- ")
print(issubclass(MyNewRouter, MyRouter))
