# "__" if you use this, it makes variable private
# __init__ is automatically executed when an object is created
# __del__ is automatically called when an object is out of scope


class store:
    __item = []            # class variable  "private"
    __price = []
    __quantity = []

    def __init__(self):         # it runs auto when class is call
        self.var = 0          # function variable
        self.__count = 0
        self.__total = 8
        self.program()     # it will run program automatically when the function is call

    def get_data(self):
        self.__item.append(int(input("Enter Item Code: ")))
        self.__price.append(int(input("Enter Item price :")))
        self.__quantity.append(int(input("Enter Item quantity :")))
        self.var = int(input("if you want to add item enter 0 \nif you want to stop the enter 1\n:"))

    def calcu_bill(self):
        for i in range(self.__count):
            self.__total = self.__total + (self.__price[i]*self.__quantity[i])
        return self.__total

    def display_data(self):
        print("*"*10, "BILL", "*"*10)
        print("ITEM CODE \t PRICE \t Quantity")
        for i in range(self.__count):
            print(self.__item[i], "\t\t", self.__price[i], "\t\t", self.__quantity[i])
        print("*" * 30)
        print("total : ", self.calcu_bill())

    def program(self):
        while True:
            if self.var == 0:
                self.get_data()
                self.__count += 1

            elif self.var == 1:
                return self.display_data()

            else:
                print("wrong statement")
                self.var = 0
                return self.get_data()


store()

