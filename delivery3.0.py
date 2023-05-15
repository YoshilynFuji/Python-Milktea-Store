import os

clear = lambda: os.system('cls')

#menu list
menu_items = [["A1", "Wintermelon Milktea", 150],
              ["A2", "Hokkaido Milktea", 120], ["A3", "Coffee Milktea", 60],
              ["A4", "Sweet Caramel Milktea", 180],
              ["A5", "Taro Milktea", 150], ["A6", "Brown Sugar Milktea", 90],
              ["A7", "Matcha Milktea", 150],
              ["A8", "Cookies and Cream Milktea", 120],
              ["A9", "Black Forest Milktea", 120],
              ["A10", "Chocolate Milktea", 200]]

cart = []

class SalesClass:
    total = 0
    code = None
    quantity = 0
    fee = 0
    vat = 0
    total_bill = 0

    @staticmethod
    def show_items():
        print("----------------------------------------------\n")
        print("{: >5}   {: <25} {: >10}\n".format("Code", "Name", "Price"))
        for i in menu_items:  # amin ditoy ngatot loop ket iprint na lang tay menu_items
            print("{: >5}   {: <25} {: >10}".format(*i))
        print("\n")
        print("{: >5}   {: <25}".format("E", "Edit an order"))
        print("{: >5}   {: <25}".format("P", "Proceed to Payment"))
        print("----------------------------------------------\n")

    @classmethod
    def extra_fee(cls):
        if not cart:
            cls.fee = 0
        else:
            cls.fee = 30
            #cls.vat = int(cls.total* 0.12)
        
        cls.total_bill = cls.total + cls.fee

    @classmethod
    def receipt(cls):

        print("----------------------------------------------\n")
        print("  {:>25}\n".format("OFFICIAL RECEIPT"))
        print("{: >5} {: >10} {: >10} {: >10}\n".format("Name", "Qty", "Price", "Total"))
        
        for i in cart:
            print("{: >5} {: >10} {: >10} {: >10}".format(*i))
        SalesClass.extra_fee()
        print("\n{: >5} {: >32}".format("Fee", cls.fee))
        #print("{: >5} {: >32}".format("VAT", cls.vat))
        print("{: <25} {: >12}".format("TOTAL", cls.total_bill))
        print("\n")
        print("----------------------------------------------\n")  

    @classmethod
    def payment(cls):
        amount = 0
        while cls.total_bill > amount:
            try:
                amount = 0
                amount = int(input("\nCash Tendered: "))
                if cls.total_bill > amount:
                    print("Insufficient Amount")
            except:
                print("Invalid Input")
                continue
        if cls.total_bill < amount:
            change = amount - cls.total_bill
            print(f"Your Change: {change}")
            
        if cls.total_bill == 0:
            clear()
            print("NO ORDER MADE!!")
            return

        print("----------------------------------------------")  
        print("Kindly provide the following information for delivery\n")
        name = str(input("Name: "))
        address = str(input("Address: "))
        phone_number = str(input("Phone number: "))
        print("----------------------------------------------\n")
        print("Please wait for your order to be delivered")
        print("Thank you!")
        exit()

    @classmethod
    def order(cls, choice):

        try:
            cls.total = cls.total

            choice_split = choice.split(" ") # pwede pa ma improve nagado nga loops feel ko HAHHAA
            cls.code = choice_split[0]  
            cls.quantity = int(choice_split[1])

            if any(cls.code in list for list in cart):  # condition if adda djay nga item ta cart'n
                for j in range(len(cart)):
                    if (cart[j][0] == cls.code):
                        cart[j][1] += cls.quantity
                        cart[j][3] += cart[j][2] * cls.quantity
                        cls.total += cart[j][2] * cls.quantity
            else:
                for i in range(len(menu_items)):  # condition for new order
                    if (menu_items[i][0] == cls.code):
                        temp_cart = [None, None, 0, 0]
                        temp_cart[0] = menu_items[i][0]
                        temp_cart[1] = cls.quantity
                        temp_cart[2] = menu_items[i][2]
                        temp_cart[3] = temp_cart[2] * cls.quantity
                        cls.total += temp_cart[3]
                        cart.append(temp_cart)
            clear()
        except:
            clear()
            print("Invalid Input")
        
    @classmethod
    def edit_order(cls):

        try:
            choice_r = input("Enter Code of order and amount to remove: ").upper()
            choice_split = choice_r.split(" ")
            code = choice_split[0]
            cls.quantity = int(choice_split[1])
        
            if any(code in list for list in cart):  
                for j in range(len(cart)):
                    if (cart[j][0] == code):
                        cart[j][1] -= cls.quantity
                        cart[j][3] -= cart[j][2] * cls.quantity
                        cls.total -= cart[j][2] * cls.quantity
        except:
            clear()
            print("Order does not exist!")
    
while True:
    SalesClass.show_items()
    SalesClass.receipt()


    choice = input("Enter Code of item and amount: ").upper()  
    
    if choice == "E":  # maaramidan function pwede rin improve since nagado nga loops
       SalesClass.edit_order()
       clear()
    elif choice == "P":
        SalesClass.payment()
    else:  # maaramidan function
        SalesClass.order(choice)
    cart =  [subl for subl in cart if subl[1] != 0]